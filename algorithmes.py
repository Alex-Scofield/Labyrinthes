'''
Algorithmes.
'''

from utilites import *
import random

def verifie_connexite(pseudo_labyrinthe: PseudoLabyrinthe, recursive: bool = True) -> bool:
    '''
    Application de l'algorithme bfs pour vérifier si un PseudoLabyrinthe est connexe.
    @param pseudo_labyrinthe: labyrinthe à vérifier.
    @return bool: true si le labyrinthe est connexe, false si non.
    '''

    visites = []
    queue = []
    debut = pseudo_labyrinthe.get_noeud_par_id((0,0))
    visites.append(debut)
    queue.append(debut)
    while queue != []:
        noeud_actuel: Noeud = queue.pop(0)
        for connexion in noeud_actuel.get_connexions():
            if connexion not in visites:
                visites.append(connexion)
                queue.append(connexion)
    
    if len(visites)!=len(pseudo_labyrinthe.get_noeuds()):
        return False
    
    return True

def nb_murs(pl:PseudoLabyrinthe)->int:
    """
    Compte le nombre de murs dans un Pseudo-Labyrinthe enceinte excluse
    @param pl: PseudoLabyrinthe dont on souhaite compter les murs
    @return int; le nombre de murs de pl
    """
    connex=[]
    visites=[]
    for noeud in pl.get_noeuds():
        visites.append(noeud)
        for connexion in noeud.get_connexions():
            if connexion not in visites:
                connex.append(connexion)
                
    return 2*pl.get_taille()[0]*pl.get_taille()[1]-pl.get_taille()[0]-pl.get_taille()[1] - len(connex)

def verifie_labyrinthe(pl: PseudoLabyrinthe) -> bool:
    '''
    Vérifie si un PseudoLabyrinthe est un Labyrinthe.
    @param pl: PseudoLabyrinthe à vérifier.
    @return bool; true si c'est un labyrinthe, false si non. 
    '''
    if not verifie_connexite(pl) or nb_murs(pl)!=2*pl.get_taille()[0]*pl.get_taille()[1]-pl.get_taille()[0]-pl.get_taille()[1]-(pl.get_taille()[0]*pl.get_taille()[1]-1):
        return False
    return True


def construit_pseudo_labyrinthe_vide(taille: tuple):
    '''
    Construit un PseudoLabyrinthe où tous les connexions sont faites.
    @param taille: tuple contenant la taille du PseudoLabyrinthe à construire.
    @return PseudoLabyrinthe sans murs.
    '''

    pseudo_labyrinthe = PseudoLabyrinthe(taille)

    for noeud in pseudo_labyrinthe.get_noeuds():
        voisins = noeud.get_voisins(pseudo_labyrinthe)
        for voisin in voisins:
            noeud.ajoute_connexions(voisin)
    
    return pseudo_labyrinthe


def construit_random_Pseudolabyrinthe_ajoute(taille: tuple) -> PseudoLabyrinthe:
    '''
    Construit un Pseudolabyrinthe random de la taille donée en ajoutant des murs.
    @param taille: tuple contenant la taille du labyrinthe à construire.
    @return PseudoLabyrinthe random de cette taille.
    '''

    pl = construit_pseudo_labyrinthe_vide(taille)
    nbmurs= random.randint(0,2*taille[0]*taille[1]-taille[0]-taille[1])

    for i in range(len(nbmurs)):
        noeud: Noeud = random.choice(pl.get_noeuds())
        voisin_choisi: Noeud = random.choice(noeud.get_voisins(pl)) 
        pl.ajoute_murs((noeud, voisin_choisi))

    return pl

def construit_random_pseudolabyrinthes_supprime(taille:tuple) -> PseudoLabyrinthe:
    '''
    Construit un PseudoLabyrinthe random, de la taille donée.
    @param taille: tuple, taille du PseudoLabyrinthe.
    @return PseudoLabyrinthe random de la taille donée.
    '''
    pl = PseudoLabyrinthe(taille)
    nmurs = random.randint(2*taille[0]*taille[1]-taille[0]-taille[1])
    for noeud in pl.get_noeuds():
        voisin = random.choice(noeud.get_voisins(pl))
        pl.supprime_murs((noeud, voisin))
    return pl


# Pour l'instant renvoie PseudoLabyrinthe

def construit_random_labyrinthe(taille: tuple) -> PseudoLabyrinthe:
    '''
    Construit un labyrinthe random de la taille donée.
    @param taille: tuple contenant la taille du labyrinthe à construir.
    @return Labyrinthe random de cette taille.
    '''

    import random

    pseudo_labyrinthe = construit_pseudo_labyrinthe_vide(taille)

    while not(verifie_labyrinthe(pseudo_labyrinthe)):
        noeud: Noeud = random.choice(pseudo_labyrinthe.get_noeuds())
        voisin_choisi: Noeud = random.choice(noeud.get_voisins(pseudo_labyrinthe)) 
        if voisin_choisi not in noeud.get_connexions():
            pseudo_labyrinthe.ajoute_murs((noeud, voisin_choisi))
            if not(verifie_connexite(pseudo_labyrinthe)):
                noeud.ajoute_connexions(voisin_choisi)
        
    return pseudo_labyrinthe 


def construit_matrice_labyrinthes(taille: tuple) -> list:
    '''
    Construit tous les PseudoLabyrinthes d'une taille donnée.
    @param taille: taille des PseudoLabyrinthe à construir
    @return list avec tous les PseudoLabyrinthes en forme de matrice de murs valides de la taille donée.
    '''

    from itertools import chain, combinations

    murs_total = []
    for i in range(taille[0]):
        for j in range(taille[1]):
            if i+1<taille[0] and ((i+1,j),(i,j)) not in murs_total:
                    murs_total.append(((i, j),(i+1,j)))
            if j+1<taille[1] and ((i,j+1),(i,j)) not in murs_total:
                murs_total.append(((i, j),(i,j+1)))
            if i-1>0 and ((i-1,j),(i,j)) not in murs_total:
                murs_total.append(((i, j),(i-1,j)))
            if j-1>0 and ((i,j-1),(i,j)) not in murs_total:
                murs_total.append(((i, j),(i,j-1)))

    return list(chain.from_iterable(combinations(murs_total, r) for r in range(len(murs_total)+1)))

def murs_to_PseudoLabyrinthe(collection_murs: tuple, taille:tuple):
    '''
    Convert une collection de murs en des PseudoLabyrinthes.
    @param collection_murs: tuple contenant les murs à ajouter.
    @param taille: taille du PseudoLabyrinthe.
    '''

    pseudo_labyrinthe = construit_pseudo_labyrinthe_vide(taille)
    for mur in collection_murs:
        noeud1 = pseudo_labyrinthe.get_noeud_par_id(mur[0])
        noeud2 = pseudo_labyrinthe.get_noeud_par_id(mur[1])
        pseudo_labyrinthe.ajoute_murs((noeud1, noeud2))
    return pseudo_labyrinthe

def get_PseudoLabyrinthes(taille: tuple):
    matrice = construit_matrice_labyrinthes(taille)
    liste = []
    for pl in matrice:
        liste.append(murs_to_PseudoLabyrinthe(pl, taille))
    return liste

def filtre_liste_PseudoLabyrinthe(pseudo_labyrinthes: list):
    liste_labyrinthes = []
    for pl in pseudo_labyrinthes:
        if verifie_labyrinthe(pl):
            liste_labyrinthes.append(pl)
    return liste_labyrinthes

def get_Labyrinthes(taille: tuple):
    return filtre_liste_PseudoLabyrinthe(get_PseudoLabyrinthes(taille))
            