'''
Tests pour les structures de données utilisées dans le projet. À vérifier avant chaque commit.
'''

import unittest
from utilites import *
from algorithmes import *

TAILLE_TEST = (3,4)

class TestInitialisationPseudoLabyrinthe(unittest.TestCase):
    def test_connexions_vides_initialisation(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)   
        for noeud in pseudo_labyrinthe.get_noeuds():
            self.assertTrue(noeud.get_connexions()==[])

class TestVoisins(unittest.TestCase):
    def test_get_voisins(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        noeud_premier: Noeud = pseudo_labyrinthe.get_noeud_par_id((0,0))
        self.assertTrue(type(noeud_premier.get_voisins(pseudo_labyrinthe))==list)

class TestAjouteConnexions(unittest.TestCase):
    def test_ajoute_connexions_vide(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        for noeud in pseudo_labyrinthe.get_noeuds():
            self.assertTrue(len(noeud.get_connexions())<=4)

    @unittest.skip
    def test_ajoute_connexions_labyrinthe_random(self):
        pseudo_labyrinthe: PseudoLabyrinthe = construit_random_labyrinthe(TAILLE_TEST)
        for noeud in pseudo_labyrinthe.get_noeuds():
            self.assertTrue(len(noeud.get_connexions())<=4)

    def test_ajoute_une_connexion_a_plein(self):
        # Chaque Noeud est connecté a lui-même.
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        debut: Noeud = pseudo_labyrinthe.get_noeud_par_id((0,0))
        noeud_a_ajouter: Noeud = pseudo_labyrinthe.get_noeud_par_id((0,1))
        debut.ajoute_connexions(noeud_a_ajouter)

        self.assertTrue(len(debut.get_connexions())==1)
        self.assertTrue(type(debut.get_connexions()[0])==Noeud)
        self.assertTrue(len(noeud_a_ajouter.get_connexions())==0)

unittest.main()