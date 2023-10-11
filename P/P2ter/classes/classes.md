# Lemmings 🏃🏻🧍🚶🤸  

## Définition des classes

![](/img/drawit-diagram-11.png)
### Classe Jeu
La casse principale

`Jeu` contient un attribut `grille` contenant un tableau de cases (instances de `Case`) à deux dimensions , et un attribut `lemmings`  contenant la liste des Lemmings actuellement en jeu.
Son constructeur initialise la grille, par exemple à partir d’une carte donnée par un fichier texte d’un format inspiré du suivant, où le caractère

`"#"` représente un mur, `"I"` représente l’entrée et `"O"` la sortie : 
```
#I###############
#               #
#####  ##########
#         #     #
#   #######     #
#               O
######  #########
     #  #
     ####
```

Cette classe fournit notamment (mais pas uniquement !) les méthodes suivantes :

* `afficher(self)` affiche la carte avec les positions et directions de tous les lemmings en jeu ;
* `tour(self)` fait « agir » chaque lemming une fois et affiche le nouvel état du jeu ;
dans cette méthode, il faut « regarder » ce qui se trouve autour de chaque lemming (mur, trou, …) afin de le faire agir en conséquence …
* `demarrer(self)` lance une boucle infinie attendant des commandes de l’utilisateur.
*Exemples de commandes : « + » pour ajouter un lemming, « q » pour quitter le jeu, "Entrée" pour jouer un tour,….*
* …
 

### Classe Lemming
Une classe

`Lemming` avec des attributs entiers positifs `l` et `c` indiquant la position (**ligne** et **colonne**) où se trouve le lemming dans la grille, et un attribut `d` indiquant sa direction, valant `1` si le lemming se dirige vers la droite et `-1` si le lemming se dirige vers la gauche.
Cette classe fournit en outre les méthodes suivantes :

* `__str__ (self)` renvoie `'>'` ou `'<'` selon la direction du lemming ;
* `avancer(self)` déplace le lemming, dans la bonne direction, droite ou gauche (selon la direction dans laquelle il se trouve – changement de colonne) ;
* `retourner(self)` retourne le lemming (changement de direction) ;
* `tomber(self)` fait tomber le lemming (changement de ligne);
…

> ATTENTION : le lemming ne regarde pas ou il va → ce n’est pas lui qui décide quoi faire s’il y a un mur en face, un autre lemming, un trou, … Tout ceci est géré par la méthode `tour` du jeu.
 

### Classe Case
La classe

`Case` contient un attribut `terrain` contenant le caractère représentant la caractéristique de la case (mur, vide, sortie, entrée … comme dans le fichier texte décrivant la grotte), et un attribut `lemming` contenant l’éventuel lemming présent dans cette case et `None` si la case est libre.
Cette classe fournit notamment les méthodes suivantes :

* `__str__ (self)` renvoie le caractère à afficher pour représenter cette case ou son éventuel occupant ;
* `estLibre(self)` renvoie `True` si la case est peut recevoir un lemming (elle n’est ni un mur, ni occupée par un lemming) ;
* `liberer(self)` retire le lemming présent dans la case ;
* `occuper(self, lem)` place le lemming `lem` sur la case ;
* …