'''
Construction de structures de données utiles.
'''


class PseudoLabyrinthe():
    '''
    Un PseudoLabyrinthe de taille m*n est une graphe avec m*n noeuds où chaque
    noeud ne peut se connecter qu'à ses voisins.
    @atribute taille: tuple contant les dimensions du pseudo_labyrinthes.

    @attribute __noeuds: liste de Noeuds.

    @method construit: Construction d'un PseudoLabyrinthe.
    @method verifie_pseudo: Vérifie que les connexions entre les noeuds sont valides.
    @method verifie_noeuds: Vérifie que les noeuds sont les casses du PseudoLabyrinthe.
    '''

    def __init__(self, taille: tuple) -> None:
        self.__noeuds = []
        self.__taille = taille

        for i in range(self.__taille[0]):
            for j in range(self.__taille[1]):
                self.__noeuds.append(Noeud((i, j)))

    def construit(self, noeuds: list) -> None:
        '''
        Construction d'un PseudoLabyrinthe.
        @param noeuds: liste de noeuds à utiliser.
        '''

        self.__noeuds = noeuds
        self.verifie()

    def get_noeud_par_id(self, id: tuple):
        '''
        Renvoie le Noeud se trouvant à la position id.
        @param id: tuple.
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
        Vérifie que les noeuds de self.__noeuds ont des id valides, et qu'ils remplissent
        le PseudoLabyrinthe. Ce ne devrait pas être nécessaire après avoir utiliser le
        construct.
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

    def verifie(self):
        '''
        Vérifie que l'objet et un PseudoLabyrinthe valide, lance erreurs si non.
        '''
        self.verifie_noeuds()
        self.verifie_connexions()

    def get_noeuds(self):
        '''
        Getter pour la liste de noeuds du PseudoLabyrinthe.
        '''

        return self.__noeuds
    
    def get_taille(self):
        '''
        Renvoie la taille du PseudoLabyrinthe.
        '''

        return self.__taille



class Labyrinthe(PseudoLabyrinthe):
    '''
    Labyrinthe vérifiant les deux proprietés expliquées au sujet.
    '''

    pass


class Noeud():
    '''
    Un Noeud est un objet qui se correspond à une case d'un PseudoLabyrinthe.
    @atribute __id: tuple contenant la position du noeud.
    @atribute __connexions: liste de noeuds. Il n'y a pas de vérifications ici.
    '''

    def __init__(self, id: tuple, connexions=[]) -> None:
        self.__id = id
        self.__connexions = connexions

    def get_id(self) -> tuple:
        '''
        Getter pour self.__id.
        '''

        return self.__id

    def get_connexions(self) -> list:
        '''
        Getter pour self.__connexions.
        '''

        return self.__connexions

    # Ajouter des vérifications.

    def ajoute_connexions(self, *args):
        '''
        Ajoute des connexions à self.__connexions. Vérifie que les connexions sont valides.
        @param *args: Liste d'autres Noeud.
        '''

        for arg in args:
            if(type(arg)!= Noeud):
                raise TypeError(f"{arg} est de type {type(arg)} est ce n'est pas un noeud.")

            if abs(self.__id[0]-arg.get_id()[0]) > 1 or abs(self.__id[1]-arg.get_id()[1]) > 1:
                raise ValueError(
                    f"On ne peut pas connecter noeuds {self.__id} et {arg.get_id()}.")
            if self.__id == arg.get_id():
                raise ValueError(
                    f"On ne peut pas connecter noeud {self.get_id()} avec lui même.")

            self.__connexions.append(arg)

    def supprime_connexions(self, *args) -> None:
        '''
        Supprime des connexions de self.__connexions.
        @param *args: Liste d'autres Noeud.
        '''

        for arg in args:
            if arg not in self.__connexions:
                raise ValueError(
                    f"Noeud {arg.get_id()} n'est pas connecté à {self.__id}.")
            self.__connexions.remove(arg)

    def get_voisins(self, pseudo_labyrinthe: PseudoLabyrinthe) -> list:
        '''
        Trouve les voisins du noeud dans le PseudoLabyrinthe donné comme paramètre.
        @param pseudo_labyrinthe: PseudoLabyrinthe où se trouve le Noeud.
        @return list contenant les noeuds voisins du noeud en question dans pseudo_labyrinthe.
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
