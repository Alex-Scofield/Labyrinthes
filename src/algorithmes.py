'''
Algorithmes.
'''

from utilites import *

def construit_pseudo_2D():
    pass

def verifie_connexite(pseudo_labyrinthe: PseudoLabyrinthe) -> bool:
    '''
    Application de l'algorithme bfs pour vérifier si un PseudoLabyrinthe est connexe.
    @param pseudo_labyrinthe: labyrinthe à vérifier.
    @return bool; true si le labyrinthe est connexe, false si non.
    '''

    visites = []
    queue = []
    debut = pseudo_labyrinthe.get_noeud_par_id((0,0))
    visites.append(debut)
    queue.append(debut)
    while queue != []:
        noeud_actuel = queue.pop(0)
        for connexion in noeud_actuel.get_connexions():
            if connexion not in visites:
                visites.append(connexion)
                queue.append(connexion)

    for noeud in pseudo_labyrinthe.get_noeuds():
        if noeud not in visites:
            return False
    
    return True


def verifie_labytinthe(pseudo_labyrinthe: PseudoLabyrinthe) -> bool:
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
