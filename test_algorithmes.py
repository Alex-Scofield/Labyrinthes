'''
Tests pour les algorithmes implantés.
'''

import unittest
from algorithmes import *
from utilites import *

TAILLE_TEST = (8, 3)


class TestVerificationsConnexite(unittest.TestCase):
    def test_verifie_connexite_vide(self):
        taille = (3, 3)
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(taille)
        self.assertTrue(verifie_connexite(pseudo_labyrinthe_sans_murs))

    def test_carre_ne_pas_connexe(self):
        pl2 = construit_pseudo_labyrinthe_vide((4, 3))
        n1 = pl2.get_noeud_par_id((1, 1))
        n2 = pl2.get_noeud_par_id((1, 0))
        pl2.ajoute_murs((n1, n2), (pl2.get_noeud_par_id((1, 1)), pl2.get_noeud_par_id((1, 2))), (pl2.get_noeud_par_id(
            (1, 1)), pl2.get_noeud_par_id((2, 1))), (pl2.get_noeud_par_id((1, 1)), pl2.get_noeud_par_id((0, 1))))
        self.assertFalse(verifie_connexite(pl2))

    def test_verifie_connexite_murs(self):
        pseudo_labyrinthe_plein = PseudoLabyrinthe(TAILLE_TEST)
        self.assertFalse(verifie_connexite(pseudo_labyrinthe_plein))

    def test_verifie_connexite_pseudo(self):
        pl2 = construit_pseudo_labyrinthe_vide((3, 2))
        pl2.ajoute_murs((pl2.get_noeud_par_id((0, 0)), pl2.get_noeud_par_id(
            (0, 1))), (pl2.get_noeud_par_id((2, 0)), pl2.get_noeud_par_id((2, 1))))
        self.assertTrue(verifie_connexite(pl2))


class TestVerificationsLabyrinthe(unittest.TestCase):
    def test_verifie_labyrinthe(self):
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(
            TAILLE_TEST)
        self.assertFalse(verifie_labyrinthe(pseudo_labyrinthe_sans_murs))


class TestVerificationsLabyrinthe(unittest.TestCase):
    def test_verifie_not_labyrinthe_vide(self):
        taille = (3, 3)
        pseudo_labyrinthe_sans_murs = construit_pseudo_labyrinthe_vide(taille)
        self.assertFalse(verifie_labyrinthe(pseudo_labyrinthe_sans_murs))

    def test_carre_ne_pas_labyrinthe(self):
        pl2 = construit_pseudo_labyrinthe_vide((4, 3))
        n1 = pl2.get_noeud_par_id((1, 1))
        n2 = pl2.get_noeud_par_id((1, 0))
        pl2.ajoute_murs((n1, n2), (pl2.get_noeud_par_id((1, 1)), pl2.get_noeud_par_id((1, 2))), (pl2.get_noeud_par_id(
            (1, 1)), pl2.get_noeud_par_id((2, 1))), (pl2.get_noeud_par_id((1, 1)), pl2.get_noeud_par_id((0, 1))))
        self.assertFalse(verifie_labyrinthe(pl2))

    def test_verifie_labyrinthe_pseudo(self):
        pl2 = construit_pseudo_labyrinthe_vide((3, 2))
        pl2.ajoute_murs((pl2.get_noeud_par_id((0, 0)), pl2.get_noeud_par_id(
            (0, 1))), (pl2.get_noeud_par_id((2, 0)), pl2.get_noeud_par_id((2, 1))))
        self.assertTrue(verifie_labyrinthe(pl2))


class TestConstructions(unittest.TestCase):
    # @unittest.skip
    def test_construit_random_labyrinthe(self):
        taille = (2, 2)
        labyrinthe_construit = construit_random_labyrinthe(taille)
        self.assertTrue(verifie_labyrinthe(labyrinthe_construit))

    def test_construit_pseudo_labyrinthe_vide(self):
        taille = (3, 3)
        labyrinthe_construit = construit_pseudo_labyrinthe_vide(taille)
        self.assertTrue(not(verifie_labyrinthe(labyrinthe_construit)))
        for noeud in labyrinthe_construit.get_noeuds():
            for voisin in noeud.get_voisins(labyrinthe_construit):
                self.assertIn(voisin, noeud.get_connexions())


unittest.main()
