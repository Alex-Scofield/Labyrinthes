'''
Algorithmes.
'''

from utilites import *
import random

def verifie_connexite(pseudo_labyrinthe: PseudoLabyrinthe) -> bool:
    '''
    Application de l'algorithme bfs pour vérifier si un Pseudo-Labyrinthe est connexe.
    
    Parameters
    ----------
    pseudo_labyrinthe : PseudoLabyrinthe
        Labyrinthe à vérifier.

    Returns
    -------
    bool 
        True si le labyrinthe est connexe, False sinon.
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
    Compte le nombre de murs dans un Pseudo-Labyrinthe, enceinte exclue

    Parameters
    ----------
    pl : PseudoLabyrinthe 
        Pseudo-labyrinthe dont on souhaite compter les murs
    
    Returns
    -------
    int
        Le nombre de murs de pl
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

    Parameters
    ----------
    pl : PseudoLabyrinthe 

    Returns
    -------
    bool
        True si c'est un labyrinthe, False si non. 
    '''
    if not verifie_connexite(pl) or nb_murs(pl)!=2*pl.get_taille()[0]*pl.get_taille()[1]-pl.get_taille()[0]-pl.get_taille()[1]-(pl.get_taille()[0]*pl.get_taille()[1]-1):
        return False
    return True


def construit_pseudo_labyrinthe_vide(taille: tuple):
    '''
    Construit un PseudoLabyrinthe dans lequel toutes les connexions sont faites.

    Parameters
    ----------
    taille : tuple 
        Tuple contenant la taille du PseudoLabyrinthe à construire.
    
    Returns
    -------
    PseudoLabyrinthe
        Un Pseudo-labyrinthe sans murs.
    '''

    pseudo_labyrinthe = PseudoLabyrinthe(taille)

    for noeud in pseudo_labyrinthe.get_noeuds():
        voisins = noeud.get_voisins(pseudo_labyrinthe)
        for voisin in voisins:
            noeud.ajoute_connexions(voisin)
    
    return pseudo_labyrinthe


def construit_random_pseudo_labyrinthe_ajoute(taille: tuple) -> PseudoLabyrinthe:
    '''
    Construit un Pseudolabyrinthe random de la taille donée en ajoutant des murs.

    Parameters
    ----------
    taille : tuple 
        Un tuple contenant la taille du labyrinthe à construire.

    Returns
    -------
    PseudoLabyrinthe random de cette taille.
    '''

    pl = construit_pseudo_labyrinthe_vide(taille)
    nbmurs= random.randint(0,2*taille[0]*taille[1]-taille[0]-taille[1])

    for i in range(len(nbmurs)):
        noeud: Noeud = random.choice(pl.get_noeuds())
        voisin_choisi: Noeud = random.choice(noeud.get_voisins(pl)) 
        pl.ajoute_murs((noeud, voisin_choisi))

    return pl

def construit_random_pseudo_labyrinthe_supprime(taille:tuple) -> PseudoLabyrinthe:
    '''
    Construit un Pseudo-labyrinthe random, de taille donnée.

    Parameters
    ----------
    taille : tuple
        taille du PseudoLabyrinthe.

    Returns
    -------
    PseudoLabyrinthe 
        pseudo-labyrinthe random de la taille voulue.
    '''
    pl = PseudoLabyrinthe(taille)
    nmurs = random.randint(2*taille[0]*taille[1]-taille[0]-taille[1])
    for noeud in pl.get_noeuds():
        voisin = random.choice(noeud.get_voisins(pl))
        pl.supprime_murs((noeud, voisin))
    return pl



def construit_random_labyrinthe_supprime(taille: tuple) -> PseudoLabyrinthe:
    '''
    Construit un labyrinthe random de taille donnée.

    Parameters
    ----------
    taille : tuple 
        Un tuple contenant la taille du labyrinthe à construire.
    
    Returns
    -------
    PseudoLabyrinthe
        Un labyrinthe random de cette taille.
    '''

    pl = PseudoLabyrinthe(taille) 

    
    for i in range(taille[0]*taille[1]-1):
        noeud: Noeud = random.choice(pl.get_noeuds())
        voisin_choisi: Noeud = random.choice(noeud.get_voisins(pl)) 
        pl.supprime_murs((noeud, voisin_choisi))
    
    
    while not(verifie_labyrinthe(pl)):
        noeud3: Noeud = random.choice(pl.get_noeuds())
        voisin_choisi3: Noeud = random.choice(noeud3.get_voisins(pl)) 
        pl.ajoute_murs((noeud3, voisin_choisi3))
        noeud2: Noeud = random.choice(pl.get_noeuds())
        voisin_choisi2: Noeud = random.choice(noeud2.get_voisins(pl)) 
        pl.supprime_murs((noeud2, voisin_choisi2))
        
    return pl 


def construit_matrice_labyrinthes(taille: tuple) -> list:
    '''
    Construit tous les PseudoLabyrinthes d'une taille donnée.

    Parameters
    ----------
    taille : tuple
        Taille des pseudo-labyrinthes à construire.
        
    Returns
    -------
    list 
        Une liste contenant tous les PseudoLabyrinthes sous forme de matrice de murs valides de la taille donnée.
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
    Converti une collection de murs en des pseudo-labyrinthes.

    Parameters
    ----------
    collection_murs: tuple 
        Un tuple contenant les murs à ajouter.
    
    taille : tuple
        taille du pseudo-labyrinthe.

    Returns
    -------
    PseudoLabyrinthe
        Le pseudo-labyrinthe construit à partir de collection_murs.
    '''

    pseudo_labyrinthe = construit_pseudo_labyrinthe_vide(taille)
    for mur in collection_murs:
        noeud1 = pseudo_labyrinthe.get_noeud_par_id(mur[0])
        noeud2 = pseudo_labyrinthe.get_noeud_par_id(mur[1])
        pseudo_labyrinthe.ajoute_murs((noeud1, noeud2))
    return pseudo_labyrinthe

def get_PseudoLabyrinthes(taille: tuple):
    '''
    Transforme les éléments de la matrice de murs de construit_matrice_labyrinthe en pseudo-labyrinthes pour une taille donnée.

    Parameters
    ----------
    taille : tuple
        Taille des pseudo-labyrinthes à construire.

    Returns
    -------
    list
        liste des pseudo-labyrinthes construits
    '''
    matrice = construit_matrice_labyrinthes(taille)
    liste = []
    for pl in matrice:
        liste.append(murs_to_PseudoLabyrinthe(pl, taille))
    return liste

def filtre_liste_PseudoLabyrinthe(pseudo_labyrinthes: list):
    '''
    Extrait les labyrinthes d'une liste de pseudo-labyrinthes.

    Parameters
    ----------
    pseudo-labyrinthes : list
        Une liste de pseudo-labyrinthes
    
    Returns
    -------
    list
        Une liste contenant les labyrinthes de pseudo_labyrinthes
    '''
    liste_labyrinthes = []
    for pl in pseudo_labyrinthes:
        if verifie_labyrinthe(pl):
            liste_labyrinthes.append(pl)
    return liste_labyrinthes

def get_Labyrinthes(taille: tuple):
    '''
    Consruit tous les labyrinthes pour une taille donnée.

    Parameters
    ----------
    taille : tuple
        Taille des labyrinthes à construire

    Returns
    -------
    list
        Une liste contenant tous les labyrinthes de taille taille. 
    '''
    return filtre_liste_PseudoLabyrinthe(get_PseudoLabyrinthes(taille))
            