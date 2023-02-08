from utilites import *

N = 4
M = 4

pl = PseudoLabyrinthe((N,M))
noeuds = pl.get_noeuds()


for noeud in noeuds:
    noeud_id = noeud.get_id()
    if noeud_id[1]%2 == 0:
        if noeud_id[0]==N-1 and noeud_id[1]<M-2:
            noeud_a_ajouter = pl.get_noeud_par_id((noeud_id[0]+1, noeud_id[1]))
            noeud.ajoute_connexions(noeud_a_ajouter)
        else:
            noeud_a_ajouter = pl.get_noeud_par_id((noeud_id[0], noeud_id[1]+1))
            noeud.ajoute_connexions(noeud_a_ajouter)
    
    else:
        if noeud_id[0]==0 and noeud_id[1]<M-2:
            noeud_a_ajouter = pl.get_noeud_par_id((noeud_id[0]+1, noeud_id[1]))
            noeud.ajoute_connexions(noeud_a_ajouter)

        else:
            noeud_a_ajouter = pl.get_noeud_par_id((noeud_id[0], noeud_id[1]-1))
            noeud.ajoute_connexions(noeud_a_ajouter)

pl.construit()
