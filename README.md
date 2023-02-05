# Readme #
*Author: Alex Scofield*

Une petite explication du projet et de notre façon de travailler.

# Architecture #

# LaTeX #

On va inclure nos recherches mathématiques dans le document d'Overleaf suivant: https://www.overleaf.com/2477192356khgysjbwtdxc


# GitHub #
Pour la gestion de versions on va utiliser Git. Ceci nous permet de revenir à une version précedante du projet si quelque chose ne marche pas et nous permet de travailler en différentes *branches* si nécessaire.

## Voici une petite guide ##

*Note: Chaque fois que vous voyez quelque chose entre {}, substituyez-le pour ce qui soit rélevant*

Pour acceder au répertoire la première fois, utilisez la commande suivante:
```console
$ git clone 
```

Chaque fois que vous commencez à travailler vous devez utiliser la commande suivante:
```console
$ git pull
```
Cela vous permet d'acceder aux documents qui se trouvent dans le serveur GitHub.

Quand vous ayez fini de travailler, utilisez les commande suivantes:
```console
$ git add {fichiers à ajouter}
```
*Si vous voulez ajouter tous les fichiers vous pouvez écrire:*
```console
$ git add -a
```
Ensuite vous devez vérifier vos changements. Pour cela, utiliser la commande:
```console
$ git commit -m "{votre message}"
```
N'hésitez surtout pas à écrire des longs messages pour que le reste de l'equipe sache ce que vous avez fait.

La commande commit n'actualise le répertoire que localement. Pour que les changements aient lieu, vous devez effectuer cette dernière commande:
```console
$ git push
```

Pour l'instant cela suffit. Si plus tard on a besoin d'autres fonctionnalités de *Git* j'ajouterai l'information.

# Documentation #
Pour documenter notre code on va utiliser epydoc (c'est un peu comme le javadocs qu'on utilise en cours).  
https://epydoc.sourceforge.net/epytext.html