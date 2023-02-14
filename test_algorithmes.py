'''
Tests pour les algorithmes implantés.
'''

import unittest
from algorithmes import *
from utilites import *

TAILLE_TEST=(8,3)

class TestVerificationsConnexite(unittest.TestCase):
    def test_verifie_connexite_murs(self):
        pseudo_labyrinthe_plein = PseudoLabyrinthe(TAILLE_TEST)
        self.assertFalse(verifie_connexite(pseudo_labyrinthe_plein))

    def test_verifie_connexite_sans_murs(self):
        taille = (3,3)
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(taille)
        self.assertTrue(verifie_connexite(pseudo_labyrinthe_sans_murs))
    
class TestVerificationsLabyrinthe(unittest.TestCase):
    def test_verifie_labyrinthe(self):
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        self.assertFalse(verifie_labyrinthe(pseudo_labyrinthe_sans_murs))


class TestConstructions(unittest.TestCase):
    @unittest.skip
    def test_construit_random_labyrinthe(self):
        taille = (3,3)
        labyrinthe_construit = construit_random_labyrinthe(taille)
        self.assertTrue(verifie_labyrinthe(labyrinthe_construit))

    @unittest.skip
    def test_construit_pseudo_labyrinthe_vide(self):
        taille = (3,3)
        labyrinthe_construit = construit_pseudo_labyrinthe_vide(taille)
        self.assertTrue(not(verifie_labyrinthe(labyrinthe_construit)))
        for noeud in labyrinthe_construit.get_noeuds():
            for voisin in noeud.get_voisins(labyrinthe_construit):
                self.assertIn(voisin, noeud.get_connexions())


unittest.main()
