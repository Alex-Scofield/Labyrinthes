'''
Construction de structures de données utiles.
'''

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class PseudoLabyrinthe():
    '''
    Un PseudoLabyrinthe de taille m*n est une graphe avec m*n noeuds où chaque
    noeud ne peut se connecter qu'à ses voisins.

    Parameters
    ----------
    taille : tuple
        Taille du PseudoLabyrinthe à construir.

    Attributes
    ----------
    taille : tuple
        Contient les dimensions du pseudo_labyrinthes.
    __noeuds : list of Noeud
        Liste de Noeuds.
    '''

    def __init__(self, taille: tuple) -> None:
        self.__noeuds = []
        self.__taille = taille

        for i in range(self.__taille[0]):
            for j in range(self.__taille[1]):
                self.__noeuds.append(Noeud((i, j), connexions=[]))

    def construit(self, noeuds: list) -> None:
        '''
        Construit un PseudoLabyrinthe à partir d'une liste de Noeuds.

        Parameters
        ----------
        noeuds : list of Noeud
            Liste de noeuds à utiliser.

        Raises
        ------
        ValueError
            Si le résultat n'est pas un PseudoLabyrinthe valide.
        '''

        self.__noeuds = noeuds
        self.verifie()

    def get_noeud_par_id(self, id: tuple):
        '''
        Renvoie le Noeud se trouvant à la position id.

        Parameters
        ----------
        id : tuple
            Position du Noeud à chercher

        Returns
        -------
        Noeud
            Noeud à la position demandée.
        
        Raises
        ------
        ValueError
            Si l'id n'est pas valide.
        '''

        if id[0] < 0 or id[1] < 0 or id[0] >= self.__taille[0] or id[1] >= self.__taille[1]:
            raise ValueError(f"{id} n'est pas une position valide.")

        for i in range(self.__taille[0]):
            for j in range(self.__taille[1]):
                for noeud in self.__noeuds:
                    if noeud.get_id() == (id[0], id[1]):
                        return noeud

    def verifie_noeuds(self) -> None:
        '''
        Vérifie que les Noeud de self.__noeuds ont des id valides, et qu'ils remplissent
        le PseudoLabyrinthe.

        Raises
        ------
        ValueError
            Si les conditions ne sont pas satisfaites.
        '''

        for noeud in self.__noeuds:
            noeud_id = noeud.get_id()
            for i in range(len(noeud_id)):
                if noeud_id[i] < 0 or noeud_id >= self.__taille[i]:
                    raise ValueError(
                        f"La position de {noeud} n'est pas valide.")

        for i in range(len(self.__taille[0])):
            trouve = False
            for j in range(len(self.__taille[1])):
                for noeud in self.__noeuds:
                    if noeud.get_id() == (i, j):
                        trouve = True
            if not trouve:
                raise ValueError(f"Il reste de noeuds à placer.")

    def verifie_connexions(self) -> None:
        '''
        Vérifie que les connexions entre les noeuds de self.__noeuds sont valides.

        Raises
        ------
        ValueError
            Si les connexions ne sont pas possibles.
        '''

        for noeud in self.__noeuds:
            for connexion in noeud.get_connexions():
                noeud_id = noeud.get_id()
                connexion_id = connexion.get_id()

                if noeud_id == connexion_id:
                    raise ValueError(f"{noeud} est connexe à lui-même.")

                if abs(noeud_id[0]-connexion_id[0]) > 1 or abs(noeud_id[1]-connexion_id[1]) > 1:
                    raise ValueError(
                        f"Connexion directe entre deux noeuds pas contigus.")
    
    def verifie_bidirectionel(self) -> None:
        '''
        Vérifie qu'un PseudoLabyrinthe est bidirectionel.

        Raises
        ------
        ValueError
            Si le PseudoLabyrinthe courant n'est pas bidirectionel.
        '''

        for noeud in self.get_noeuds():
            for connexion in noeud.get_connexions():
                if noeud not in connexion.get_connexions():
                    raise ValueError("PseudoLabyrinthe non bidirectionel.")

    def ajoute_murs(self, *args) -> None:
        '''
        Procédure qui ajoute un mur entre les noeuds donnés comme paramètres deux par deux.
        
        Parameters
        ----------
        *args : tuple of Noeud
            Tuples de Noeuds à connecter deux par deux.
        '''
        for arg in args:
            noeud1 = arg[0]
            noeud2 = arg[1]
            if noeud2 in noeud1.get_connexions():
                noeud1.supprime_connexions(noeud2)
            if noeud1 in noeud2.get_connexions():
                noeud2.supprime_connexions(noeud1)
    
    def supprime_murs(self, *args) -> None:
        '''
        Procédure qui supprime le mur eventuel entre deux noeuds.

        Parameters
        ----------
        *args : tuple of Noeud
            Tuples de Noeuds dont on veut supprimer le mur.
        '''
        for arg in args:
            noeud1 = arg[0]
            noeud2 = arg[1]
            if noeud2 not in noeud1.get_connexions():
                noeud1.ajoute_connexions(noeud2)
            if noeud1 not in noeud2.get_connexions():
                noeud2.ajoute_connexions(noeud1)

    def bidirectionalise(self) -> None:
        '''
        Procédure qui bidirectionalise toutes les connexions entre noeuds du PseudoLabyrinthe.

        Notes
        -----
        Ne devrait pas être nécessaire avec l'implementation bidirectionelle.
        '''
        for noeud in self.get_noeuds():
            for connexion in noeud.get_connexions():
                if noeud not in connexion.get_connexions():
                    connexion.ajoute_connexions(noeud)

    def supprime_connexions_redoublantes(self) -> None:
        '''
        Supprime les connexions rédoublantes dans tous les noeuds du PseudoLabyrinthe courant.
        '''
        for noeud in self.get_noeuds():
            noeud.supprime_connexions_redoublantes()

    def verifie(self):
        '''
        Vérifie que l'objet courant est un PseudoLabyrinthe valide.

        Raises
        ------
        ValueError
            Si le PseudoLabyrinthe n'est pas valide.
        '''
        self.verifie_noeuds()
        self.verifie_connexions()
        self.verifie_bidirectionel()

    def get_noeuds(self):
        '''
        Getter pour la liste de noeuds du PseudoLabyrinthe.

        Returns
        -------
        list of Noeud
            self.__noeuds
        '''
        return self.__noeuds

    def get_taille(self):
        '''
        Renvoie la taille du PseudoLabyrinthe.
        
        Returns
        -------
        tuple
            self.__taille
        '''

        return self.__taille

    def copie(self):
        '''
        Copie le PseudoLabyrinthe courant.

        Returns
        -------
        PseudoLabyrinthe
            Copie du PseudoLabyrinthe courant.
        '''
        pl = PseudoLabyrinthe(self.get_taille())
        for noeud in self.get_noeuds():
            for connexion in noeud.get_connexions():
                pl.get_noeud_par_id(noeud.get_id()).ajoute_connexions(pl.get_noeud_par_id(connexion.get_id()))
        return pl
            
    
    def __eq__(self, autre) -> bool:
        '''
        Vérifie si deux PseudoLabyrinthes sont isomorphes.

        Returns
        -------
        bool
            True s'ils sont isomorphes, False sinon.
        '''
        if self.get_taille() != autre.get_taille():
            return False
        copie_self = self.copie()
        copie_self.bidirectionalise() # Ceci ne devrait plus être nécessaire.
        copie_autre = autre.copie()
        copie_autre.bidirectionalise()
        for i in range(self.get_taille()[0]):
            for j in range(self.get_taille()[1]):
                noeud_self = copie_self.get_noeud_par_id((i, j))
                noeud_autre = copie_autre.get_noeud_par_id((i,j))
                liste_connexions_self = []
                liste_connexions_autre = []
                for connexion in noeud_self.get_connexions():
                    liste_connexions_self.append(connexion.get_id())
                for connexion in noeud_autre.get_connexions():
                    liste_connexions_autre.append(connexion.get_id())
                
                if set(liste_connexions_self)!=set(liste_connexions_autre):
                    return False
        return True

    def __ne__(self, autre):
        return not(self==autre)

class Noeud():
    '''
    Un Noeud est un objet qui se correspond à une case d'un PseudoLabyrinthe.
    
    Parametres
    ----------
    id : tuple 
        Contient la position du noeud.
    connexions : liste de noeuds
        Noeuds connexes au Noeud courant

    Attributes
    ----------
    __id : tuple 
        Contient la position du noeud.
    __connexions : liste de noeuds
        Noeuds connexes au Noeud courant
    '''

    def __init__(self, id: tuple, connexions=[]) -> None:
        self.__id = id
        self.__connexions = connexions

    def get_id(self) -> tuple:
        '''
        Getter pour self.__id.

        Returns
        -------
        tuple
            self.__id
        '''

        return self.__id

    def get_connexions(self) -> list:
        '''
        Getter pour self.__connexions.

        Returns
        -------
        list
            self.__connexions
        '''

        return self.__connexions


    def ajoute_connexions(self, *args):
        '''
        Ajoute des connexions à self.__connexions. Vérifie que les connexions sont valides.

        Notes
        -----
        Dans la plupart des cas utiliser ajoute_murs et ne pas ajoute_connexions.

        Parameters
        ----------
        *args : list of Noeud
        '''

        TUPLES_VALIDES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for arg in args:
            if(type(arg) != Noeud):
                raise TypeError(
                    f"{arg} est de type {type(arg)} est ce n'est pas un noeud.")

            substraction = tuple(
                map(lambda i, j: i - j, arg.get_id(), self.get_id()))
            if substraction not in TUPLES_VALIDES:
                raise ValueError(
                    f"On ne peut pas connecter tuple {arg.get_id()} avec {self.get_id()}.")

            self.__connexions.append(arg)

    def supprime_connexions(self, *args) -> None:
        '''
        Supprime des connexions de self.__connexions.

        Parametres
        ----------
        *args : Liste of Noeud
        '''

        for arg in args:
            if arg not in self.__connexions:
                raise ValueError(
                    f"Noeud {arg.get_id()} n'est pas connecté à {self.__id}.")
            self.__connexions.remove(arg)
    
    def supprime_connexions_redoublantes(self) -> None:
        '''
        Supprime les connexions rédoublantes du Noeud.
        '''
        self.__connexions = list(set(self.get_connexions()))

    def get_voisins(self, pseudo_labyrinthe: PseudoLabyrinthe) -> list:
        '''
        Trouve les voisins du noeud dans le PseudoLabyrinthe donné comme paramètre.

        Parameters
        ----------
        pseudo_labyrinthe: PseudoLabyrinthe 
            PseudoLabyrinthe où se trouve le Noeud.

        Returns
        -------
        list 
            Contient les noeuds voisins du noeud en question dans pseudo_labyrinthe.
        '''

        voisins = []
        try:
            voisins.append(pseudo_labyrinthe.get_noeud_par_id(
                (self.get_id()[0]-1, self.get_id()[1])))
        except ValueError:
            pass

        try:
            voisins.append(pseudo_labyrinthe.get_noeud_par_id(
                (self.get_id()[0], self.get_id()[1]-1)))
        except ValueError:
            pass

        try:
            voisins.append(pseudo_labyrinthe.get_noeud_par_id(
                (self.get_id()[0]+1, self.get_id()[1])))
        except ValueError:
            pass

        try:
            voisins.append(pseudo_labyrinthe.get_noeud_par_id(
                (self.get_id()[0], self.get_id()[1]+1)))
        except ValueError:
            pass

        return voisins