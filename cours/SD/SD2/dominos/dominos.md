Le domino est un jeu très ancien constitué de 28 pièces toute différentes. Sur chacune de ces pièces, il y a deux cotés qui sont constitués de 0 (blanc) à 6 points noirs. Lorsqué les 2 cotés possèdent le même nombre de points, on l’appelle domino double. 

1. Proposer un classe Domino permettant de représenter une pièce. Les objets seront initialisés avec les valeurs des deux côtés (gauche et droite). On définira des méthodes pour tester si le domino est double ou blanc. On implémentera également une méthode pour compter le nombre de points sur un domino. 
On ajoutera également une méthode qui affiche les valeurs des deux faces de manière horizontale pour un domino classique et de manière verticale pour un domino double comme le montre la figure ci-dessous.

```
 ------- 
| 5 | 4 |
 ------- 
 --- 
| 1 |
|   |
| 1 |
 --- 
```


2. Proposer une classe JeuDeDomino permettant de manipuler le jeu de domino complet. On créera une méthode pour mélanger le jeu et pour distribuer selon 2 joueurs ou plus. 

3. En utilisant cette classe, on affichera le jeu de 2 joueurs ainsi que le jeu restant (la pioche). Pour chaque joueur, on affichera le nombre 
de points dans le jeu.



```python
import random

class JeuDeDomino:
    """ Classe JeuDeDomino """

    def __creerJeu(self):
        """ Pour créer un jeu de 28 pieces toutes différentes """
        jeu = []
        for i in range(7):
            for j in range(i + 1):
                jeu.append(Domino(i, j))
        return jeu

    def __init__(self):
        """ Constructeur """
        self.__Jeu = ...
        self.__NbPieces = ...

    def Melanger(self):
        """ Mélange aléatoirement le jeu de dominos """
        random.shuffle(...)

    def AfficherJeu(self):
        """ Affiche toutes les pièces du jeu ou la pioche si il y eu distribution """
        ...

    def Distribuer(self, nb_joueur):
        """ Extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos """
        ...


class Domino:
    """ Classe Domino """

    def __init__(self, ptg, ptd):
        """ Constructeur """
        self.__cote_gauche = ...
        self.__cote_droit = ...

    def AfficherDomino(self):
        """ Affiche les 2 faces du Domino """
        ...

    def Nb_points(self):
        """ retourne la somme des points présents sur les 2 côtés """
       ...

    def EstBlanc(self):
        """ teste si le domino possède un blanc : 0 sur un des côtés """
        ...

    def EstDouble(self):
        """ teste si le domino est double : même nombre sur les 2 côtés """
        ...



monjeu = JeuDeDomino()
monjeu.Melanger()

jeu1 = monjeu.Distribuer(2)
print("joueur1")
points_joueur1 = 0
nb_domino_blc_1 = 0
nb_dominos_double_1 = 0
for i in range(len(jeu1)):
    jeu1[i].AfficherDomino()
    points_joueur1 += jeu1[i].Nb_points()
    if jeu1[i].EstDouble():
        nb_dominos_double_1 += 1
    if jeu1[i].EstBlanc():
        nb_domino_blc_1 += 1
print("points :", points_joueur1, "points possibles : dont", nb_domino_blc_1, "blanc(s) et", nb_dominos_double_1, "double(s)")

jeu2 = monjeu.Distribuer(2)
print("joueur2")
points_joueur2 = 0
nb_domino_blc_2 = 0
nb_dominos_double_2 = 0
for i in range(len(jeu2)):
    jeu2[i].AfficherDomino()
    points_joueur2 += jeu2[i].Nb_points()
    if jeu2[i].EstDouble():
        nb_dominos_double_2 += 1
    if jeu2[i].EstBlanc():
        nb_domino_blc_2 += 1
print("points :", points_joueur2, "points possibles : dont", nb_domino_blc_2, "blanc(s) et", nb_dominos_double_2, "double(s)")

print("pioche")
monjeu.AfficherJeu()


```