'''
Module contenant les différents méthodes d'affichage de labyrinthes.
'''

from utilites import *


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
cote = ["haut", "droite", "gauche", "bas"]


def positionsMurs(n: Noeud) -> list:
    connexions = n.get_connexions()
    vectors = [(node[0]-n.get_id()[0], node[1]-n.get_id()[1])
               for node in connexions]
    murs = []
    for v in directions:
        if v not in vectors:
            # pour un affichage verbeux switch directions pour cote avant []
            murs.append(directions[directions.index(v)])
    return murs


# code probablement orienté sage, on verra
def dessineNoeud(n: Noeud) -> None:
    murs = positionsMurs(n)
    lines = []
    for m in murs:
        if m == (-1, 0):
            lines.append([n.get_id(), (n.get_id()[0], n.get_id()[1]+1)])
        elif m == (1, 0):
            lines.append([(n.get_id()[0]+1, n.get_id()[1]),
                         (n.get_id()[0]+1, n.get_id()[1]+1)])
        elif m == (0, 1):
            lines.append([(n.get_id()[0], n.get_id()[1]+1),
                         (n.get_id()[0]+1, n.get_id()[1]+1)])
        elif m == (0, -1):
            lines.append([n.get_id(), (n.get_id()[0]+1, n.get_id()[1]+1)])

    for line in lines:
        line2d(line)
        
        
def afficheLaby(L : PseudoLabyrinthe):
        for n in L.get_noeuds():
            dessineNoeud(n)



n = Noeud((3, 4), [(4, 4), (3, 3), (3, 5)])
print(positionsMurs(n))
