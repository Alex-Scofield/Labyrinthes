'''
Tests pour les algorithmes implantés.
'''

import unittest
from src.utilites import *
from src.algorithmes import *

class TestVerifications(unittest.TestCase):
    def test_verifie_connexite(self):
        taille = (3,3)
        pseudo_labyrinthe_sans_murs = PseudoLabyrinthe(taille)
        self.assertFalse(verifie_connexite(pseudo_labyrinthe_sans_murs))

class TestConstructions(unittest.TestCase):
    def test_construit_random_labyrinthe(self):
        taille = (3,3)
        labyrinthe_construit = construit_random_labyrinthe(taille)
        self.assertTrue(verifie_labyrinthe(labyrinthe_construit))

if __name__ == "__main__":
    unittest.main()