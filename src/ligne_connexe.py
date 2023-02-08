'''
Exemple basique de labyrinthe avec première ligne connexe, où le reste des cases sont separées.
'''

from utilites import *
import algorithmes

N = 5
M = 5

pl = PseudoLabyrinthe((N,M))

for noeud in pl.get_noeuds():
    noeud_id = noeud.get_id()
    if noeud_id[0]==0 and noeud_id[1]<M-2:
        noeud_a_ajouter = pl.get_noeud_par_id((noeud_id[0], noeud_id[1]+1))

# Vérifions que pl n'est pas connexe
assert not algorithmes.verifie_connexite(pl)