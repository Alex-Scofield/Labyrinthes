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

class TestCopieLabyrinthes(unittest.TestCase):
    def test_copie_vide(self):
        pl1 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        pl2 = pl1.copie()
        self.assertTrue(nb_murs(pl2)==0)
    
    def test_copie(self):
        pl1 = PseudoLabyrinthe(TAILLE_TEST)
        pl1.ajoute_murs((pl1.get_noeud_par_id((0,0)), pl1.get_noeud_par_id((0,1))))
        pl2 = pl1.copie()
        pl1.supprime_murs((pl1.get_noeud_par_id((0,0)), pl1.get_noeud_par_id((0,1))))
        self.assertTrue(nb_murs(pl1)!=nb_murs(pl2))


class TestEgaliteLabyrinthes(unittest.TestCase):
    def test_egaux_vides(self):
        pl1 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        pl2 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        self.assertEqual(pl1, pl2)
    
    def test_egaux_remplis(self):
        pl1 = PseudoLabyrinthe(TAILLE_TEST)
        pl2 = PseudoLabyrinthe(TAILLE_TEST)
        self.assertEqual(pl1,pl2)

    def test_egaux_un_mur(self):
        pl1 = PseudoLabyrinthe(TAILLE_TEST)
        pl1.ajoute_murs((pl1.get_noeud_par_id((0,0)), pl1.get_noeud_par_id((0,1))))
        pl2 = PseudoLabyrinthe(TAILLE_TEST)
        pl2.ajoute_murs((pl2.get_noeud_par_id((0,0)), pl2.get_noeud_par_id((0,1))))
        self.assertEqual(pl1, pl2)

    def test_differents_vide_rempli(self):
        pl1 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        pl2 = PseudoLabyrinthe(TAILLE_TEST)
        self.assertNotEqual(pl1, pl2)

    def test_differents_un_mur(self):
        pl1 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        pl1.ajoute_murs((pl1.get_noeud_par_id((0,0)), pl1.get_noeud_par_id((1,0))))
        pl2 = construit_pseudo_labyrinthe_vide(TAILLE_TEST)
        pl2.ajoute_murs((pl2.get_noeud_par_id((0,0)), pl2.get_noeud_par_id((0,1))))
        self.assertTrue(pl1!=pl2)
    
    def test_different_sizes(self):
        pl1 = PseudoLabyrinthe((3,2))
        pl2 = PseudoLabyrinthe((3,3))
        self.assertNotEqual(pl1,pl2)

class TestGetNoeudParId(unittest.TestCase):
    def setUp(self) -> None:
        self.pseudo_labyrinthe = PseudoLabyrinthe((4,4))

    def test_get_noeud_par_id(self):
        noeud = self.pseudo_labyrinthe.get_noeud_par_id((2,3))
        self.assertEqual(noeud.get_id(),(2,3))

    def test_get_noeud_par_id_erreur(self):
        self.assertRaises(ValueError, self.pseudo_labyrinthe.get_noeud_par_id, (4,2))

class TestVoisins(unittest.TestCase):
    def test_get_voisins_est_list(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        noeud_premier: Noeud = pseudo_labyrinthe.get_noeud_par_id((0,0))
        self.assertTrue(type(noeud_premier.get_voisins(pseudo_labyrinthe))==list)
    
    def test_get_voisins_tailles(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        for noeud in pseudo_labyrinthe.get_noeuds():
            self.assertTrue(len(noeud.get_voisins(pseudo_labyrinthe))<=4)
    
    def test_get_voisins_normal(self):
        pseudo_labyrinthe = PseudoLabyrinthe((4,4))
        noeud_test = pseudo_labyrinthe.get_noeud_par_id((2,2))
        voisins_id = [voisin.get_id() for voisin in noeud_test.get_voisins(pseudo_labyrinthe)]
        self.assertTrue(set(voisins_id)=={(1,2),(3,2), (2,1),(2,3)})
    
    def test_get_voisins_cas_extreme(self):
        pseudo_labyrinthe = PseudoLabyrinthe((3,2))
        noeud_test = pseudo_labyrinthe.get_noeud_par_id((2,1))
        voisins_id = [voisin.get_id() for voisin in noeud_test.get_voisins(pseudo_labyrinthe)]
        self.assertTrue(set(voisins_id)=={(1,1), (2,0)})

class TestAjouteConnexions(unittest.TestCase):
    def test_ajoute_connexions_vide(self):
        pseudo_labyrinthe = PseudoLabyrinthe(TAILLE_TEST)
        for noeud in pseudo_labyrinthe.get_noeuds():
            self.assertTrue(len(noeud.get_connexions())<=4)
            
    def test_ajoute_connexions_labyrinthe_random(self):
        pseudo_labyrinthe: PseudoLabyrinthe = construit_random_labyrinthe_supprime(TAILLE_TEST)
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