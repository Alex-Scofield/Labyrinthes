'''
Module contenant les différents méthodes d'affichage de labyrinthes.
'''

from utilites import *
import algorithmes
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
cote = ["haut", "droite", "gauche", "bas"]


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
cote = ["haut", "droite", "gauche", "bas"]


def dessineNoeud(n: Noeud, murs: list) -> None:
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
            lines.append([n.get_id(), (n.get_id()[0]+1, n.get_id()[1])])
    return lines


def afficheLaby(pl: PseudoLabyrinthe) -> list:
    plot = line2d([(0, 0), (0, 0)], xmin=0, xmax=pl.get_taille()[0], ymin=0, ymax=pl.get_taille()[1])
    for n in pl.get_noeuds():
        connexions = n.get_connexions()
        nid = n.get_id()
        vectors = [(node.get_id()[0]-nid[0], node.get_id()[1]-nid[1]) for node in connexions]
        murs = []
        for v in directions:
            if v not in vectors:
                murs.append(directions[directions.index(v)])
        for m in murs:
            if (0<=nid[0]+m[0]<pl.get_taille()[0] and 0<=nid[1]+m[1]<pl.get_taille()[1]):
                if n in pl.get_noeud_par_id((nid[0]+m[0],nid[1]+m[1])).get_connexions():
                    murs.remove(m)
        lines = dessineNoeud(n, murs)
        for line in lines:
            plot += line2d(line)
    return plot
