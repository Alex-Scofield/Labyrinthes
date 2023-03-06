from utilites import *
from algorithmes import *
import random


def construit_random_pseudolabyrinthes_supprime(taille: tuple) -> PseudoLabyrinthe:
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
