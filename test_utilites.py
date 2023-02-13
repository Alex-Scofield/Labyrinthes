'''
Tests pour les structures de données utilisées dans le projet. À vérifier avant chaque commit.
'''

import unittest
from utilites import *

TAILLE_TEST = (3,4)

class TestVoisins(unittest.TestCase):
    def test_get_voisins(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        noeud_premier: Noeud = pseudo_labyrinthe.get_noeud_par_id((0,0))
        self.assertTrue(type(noeud_premier.get_voisins(pseudo_labyrinthe))==list)

unittest.main()