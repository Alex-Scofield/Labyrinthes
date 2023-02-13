'''
Algorithmes.
'''

from utilites import *

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


def verifie_labyrinthe(pseudo_labyrinthe: PseudoLabyrinthe) -> bool:
    '''
    Vérifie si un PseudoLabyrinthe est un Labyrinthe.
    @param pseudo_labyrinthe: PseudoLabyrinthe à vérifier.
    @return bool; true si c'est un labyrinthe, false si non. 
    '''

    if not verifie_connexite(pseudo_labyrinthe):
        return False
    
    for noeud in pseudo_labyrinthe.get_noeuds():
        visites = []
        for connexion in noeud.get_connexions(): # Cela fonctionne, mais on va parcourir les connexions deux fois.
            if connexion not in visites:
                noeud.supprime_connexions(connexion)
                if verifie_connexite(pseudo_labyrinthe):
                    return False
                noeud.ajoute_connexions(connexion)
                visites.append(connexion)
                
    return True

# Pour l'instant renvoie PseudoLabyrinthe
def construit_random_labyrinthe(taille: tuple) -> PseudoLabyrinthe:
    '''
    Construit un labyrinthe random de la taille donée.
    @param taille: tuple contenant la taille du labyrinthe à construir.
    @return Labyrinthe random de cette taille.
    '''

    import random

    pseudo_labyrinthe = PseudoLabyrinthe(taille)

    while not(verifie_labyrinthe(pseudo_labyrinthe)):
        noeud: Noeud = random.choice(pseudo_labyrinthe.get_noeuds())
        voisin_choisi: Noeud = random.choice(noeud.get_voisins(pseudo_labyrinthe)) 
        if voisin_choisi not in noeud.get_connexions():
            noeud.ajoute_connexions(voisin_choisi)
            if not(verifie_connexite(pseudo_labyrinthe)):
                noeud.supprime_connexions(voisin_choisi)
        
    return pseudo_labyrinthe 

def construit_pseudo_labyrinthe_vide(taille: tuple):
    '''
    Construit un PseudoLabyrinthe où tous les connexions sont faites.
    @param taille: tuple contenant la taille du PseudoLabyrinthe à construire.
    @return PseudoLabyrinthe sans murs.
    '''

    pseudo_labyrinthe = PseudoLabyrinthe(taille)

    for noeud in pseudo_labyrinthe.get_noeuds():
        noeud:Noeud
        noeud.ajoute_connexions(noeud.get_voisins(pseudo_labyrinthe))
    
    return pseudo_labyrinthe
