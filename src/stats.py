'''
Statistiques de la géneration de pseudolabyrinthes et labyrinthes.
'''

from utilites import *
from algorithmes import *
import numpy as np
import matplotlib.pyplot as plt
import random

TAILLE = (2,2)
N = 1000

def plot_uniforme(taille: tuple, N=100000):
    pseudolabyrinthes = get_PseudoLabyrinthes(taille)
    longueur = len(pseudolabyrinthes)
    x = np.arange(0, longueur)
    y = np.zeros(longueur)
    for i in range(N):
        choix = random.randint(0, longueur-1)
        y[choix] += 1
    plt.scatter(x, y)
    plt.ylim(0,N)
    plt.show()
        


print("ÑEÑEÑE")
pseudolabyrinthes = get_PseudoLabyrinthes(TAILLE)
#pseudolabyrinthes = get_Labyrinthes(TAILLE)
longueur = len(pseudolabyrinthes)

proportion = 0
prop2 = 0
x = np.arange(longueur)
y = np.zeros(longueur)

print("HIHIHI")
for i in range(N):
    construit = construit_random_pseudo_labyrinthe_ajoute(TAILLE)
    for j in range(longueur):
        if construit == pseudolabyrinthes[j]:
            y[j] += 1
            if j == 0:
                proportion += 1

    b = 0
    for noeud in construit.get_noeuds(): 
        b += len(noeud.get_connexions())
    if b==2*(2*TAILLE[0]*TAILLE[1]-TAILLE[0]-TAILLE[1]):
        prop2 += 1

print("HOHOHO")
plt.scatter(x, y)
plt.show()
print(proportion/N)
print(prop2/N)

plot_uniforme(TAILLE)