

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