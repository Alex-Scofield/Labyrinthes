'''
Tests pour les algorithmes implantés.
'''

import unittest
from algorithmes import *
from utilites import *

class TestVerifications(unittest.TestCase):
    def test_verifie_connexite(self):
        taille = (3,3)
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(taille)
        self.assertFalse(verifie_connexite(pseudo_labyrinthe_sans_murs))

class TestConstructions(unittest.TestCase):
    def test_construit_random_labyrinthe(self):
        taille = (3,3)
        labyrinthe_construit = construit_random_labyrinthe(taille)
        self.assertTrue(verifie_labyrinthe(labyrinthe_construit))

    def test_construit_pseudo_labyrinthe_vide(self):
        taille = (3,3)
        labyrinthe_construit = construit_pseudo_labyrinthe_vide(taille)
        self.assertTrue(not(verifie_labyrinthe(labyrinthe_construit)))
        for noeud in labyrinthe_construit.get_noeuds():
            for voisin in noeud.get_voisins(labyrinthe_construit):
                self.assertIn(voisin, noeud.get_connexions())


suite = unittest.TestSuite()
suite.addTest(TestVerifications("test_verifie_connexite"))
runner = unittest.TextTestRunner()
runner.run(suite)
