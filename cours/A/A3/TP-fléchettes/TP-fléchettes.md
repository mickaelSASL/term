## TP : Jeu de fléchettes

**Objectif : Calculer les points**  
![](Secteurcible.gif)
![](cible.png)

* Chaque joueur débute avec un capital de 501 points.  
* On lance alors une volée de trois fléchettes, on additionne le score de ces dernières et soustrait le résultat à son capital pour arriver le premier à zéro exactement (sans dépasser).  
* Il faut également atteindre zéro avec un "double".

Selon ces règles, à partir du score de 141 points, il est possible de d'atteindre 0.

Ecrire la fonction `compte_points` prenant en paramètre en entier `score` représentant le score du joueur avant le jet de ses 3 fléchettes. La fonction renvoie une liste contenant les scores qu'il est possible d'atteindre avec les 3 fléchettes.

Utilisez la méthode "Diviser pour règner" : il

