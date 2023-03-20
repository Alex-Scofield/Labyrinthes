# Labyrinthes package

## Submodules

## Labyrinthes.affichage module

## Labyrinthes.algorithmes module

## Labyrinthes.conf module

## Labyrinthes.constrandom module

## Labyrinthes.exemple_random module

## Labyrinthes.gui module

## Labyrinthes.ligne_connexe module

## Labyrinthes.pseudo_serpent module

## Labyrinthes.test_algorithmes module

## Labyrinthes.test_utilites module

## Labyrinthes.utilites module

Construction de structures de données utiles.


### _class_ Labyrinthes.utilites.Noeud(id: tuple, connexions=[])
Bases : `object`

Un Noeud est un objet qui se correspond à une case d’un PseudoLabyrinthe.

id

    Contient la position du noeud.

connexions

    Noeuds connexes au Noeud courant


#### \__id()
Contient la position du noeud.


* **Type**

    tuple



#### \__connexions()
Noeuds connexes au Noeud courant


* **Type**

    liste de noeuds



#### ajoute_connexions(\*args)
Ajoute des connexions à self.__connexions. Vérifie que les connexions sont valides.

### Notes

Dans la plupart des cas utiliser ajoute_murs et ne pas ajoute_connexions.


* **Paramètres**

    **\*args** (*list of Noeud*) – 



#### get_connexions()
Getter pour self.__connexions.


* **Renvoie**

    self.__connexions



* **Type renvoyé**

    list



#### get_id()
Getter pour self.__id.


* **Renvoie**

    self.__id



* **Type renvoyé**

    tuple



#### get_voisins(pseudo_labyrinthe: PseudoLabyrinthe)
Trouve les voisins du noeud dans le PseudoLabyrinthe donné comme paramètre.


* **Paramètres**

    **pseudo_labyrinthe** (*PseudoLabyrinthe*) – PseudoLabyrinthe où se trouve le Noeud.



* **Renvoie**

    Contient les noeuds voisins du noeud en question dans pseudo_labyrinthe.



* **Type renvoyé**

    list



#### supprime_connexions(\*args)
Supprime des connexions de self.__connexions.



```
*
```

args : Liste of Noeud


#### supprime_connexions_redoublantes()
Supprime les connexions rédoublantes du Noeud.


### _class_ Labyrinthes.utilites.PseudoLabyrinthe(taille: tuple)
Bases : `object`

Un PseudoLabyrinthe de taille m\*n est une graphe avec m\*n noeuds où chaque
noeud ne peut se connecter qu’à ses voisins.


* **Paramètres**

    **taille** (*tuple*) – Taille du PseudoLabyrinthe à construir.



#### taille()
Contient les dimensions du pseudo_labyrinthes.


* **Type**

    tuple



#### \__noeuds()
Liste de Noeuds.


* **Type**

    list of Noeud



#### ajoute_murs(\*args)
Procédure qui ajoute un mur entre les noeuds donnés comme paramètres deux par deux.


* **Paramètres**

    **\*args** (*tuple of Noeud*) – Tuples de Noeuds à connecter deux par deux.



#### bidirectionalise()
Procédure qui bidirectionalise toutes les connexions entre noeuds du PseudoLabyrinthe.

### Notes

Ne devrait pas être nécessaire avec l’implementation bidirectionelle.


#### construit(noeuds: list)
Construit un PseudoLabyrinthe à partir d’une liste de Noeuds.


* **Paramètres**

    **noeuds** (*list of Noeud*) – Liste de noeuds à utiliser.



* **Lève**

    **ValueError** – Si le résultat n’est pas un PseudoLabyrinthe valide.



#### copie()
Copie le PseudoLabyrinthe courant.


* **Renvoie**

    Copie du PseudoLabyrinthe courant.



* **Type renvoyé**

    PseudoLabyrinthe



#### get_noeud_par_id(id: tuple)
Renvoie le Noeud se trouvant à la position id.


* **Paramètres**

    **id** (*tuple*) – Position du Noeud à chercher



* **Renvoie**

    Noeud à la position demandée.



* **Type renvoyé**

    Noeud



* **Lève**

    **ValueError** – Si l’id n’est pas valide.



#### get_noeuds()
Getter pour la liste de noeuds du PseudoLabyrinthe.


* **Renvoie**

    self.__noeuds



* **Type renvoyé**

    list of Noeud



#### get_taille()
Renvoie la taille du PseudoLabyrinthe.


* **Renvoie**

    self.__taille



* **Type renvoyé**

    tuple



#### supprime_connexions_redoublantes()
Supprime les connexions rédoublantes dans tous les noeuds du PseudoLabyrinthe courant.


#### supprime_murs(\*args)
Procédure qui supprime le mur eventuel entre deux noeuds.


* **Paramètres**

    **\*args** (*tuple of Noeud*) – Tuples de Noeuds dont on veut supprimer le mur.



#### verifie()
Vérifie que l’objet courant est un PseudoLabyrinthe valide.


* **Lève**

    **ValueError** – Si le PseudoLabyrinthe n’est pas valide.



#### verifie_bidirectionel()
Vérifie qu’un PseudoLabyrinthe est bidirectionel.


* **Lève**

    **ValueError** – Si le PseudoLabyrinthe courant n’est pas bidirectionel.



#### verifie_connexions()
Vérifie que les connexions entre les noeuds de self.__noeuds sont valides.


* **Lève**

    **ValueError** – Si les connexions ne sont pas possibles.



#### verifie_noeuds()
Vérifie que les Noeud de self.__noeuds ont des id valides, et qu’ils remplissent
le PseudoLabyrinthe.


* **Lève**

    **ValueError** – Si les conditions ne sont pas satisfaites.


## Module contents
