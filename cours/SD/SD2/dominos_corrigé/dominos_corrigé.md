```Python
    import random

    class JeuDeDomino:
        """ Classe JeuDeDomino """

        def __creerJeu(self):
            """ Pour créer un jeu de 28 pièces toutes différentes """
            jeu = []
            for i in range(7):
                for j in range(i+1):
                    jeu.append(Domino(i, j))
            return jeu

        def __init__(self):
            """ Constructeur """
            self.__Jeu = self.__creerJeu()
            self.__NbPieces = 28

        def Melanger(self):
            """ Mélange aléatoirement le jeu de dominos """
            random.shuffle(self.__Jeu)

        def AfficherJeu(self):
            """ Affiche toutes les pièces du jeu ou la pioche si il y eu distribution """
            for el in self.__Jeu:
                el.AfficherDomino()

        def Distribuer(self, nb_joueur):
            """ Extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos """
            jeu_joueur = []
            if nb_joueur == 2:
                nb_domino = 7
            else:
                nb_domino = 6

            for i in range(nb_domino):
                dom = self.__Jeu.pop(0)
                jeu_joueur.append(dom)
                self.__NbPieces = self.__NbPieces - 1

            return jeu_joueur

    class Domino:
        def __init__(self, ptg, ptd):
            self._cote_gauche = ptg
            self._cote_droit = ptd


        def AfficherDomino(self):
            if self.EstDouble():
                print(" --- ")
                print("| " + str(self._cote_gauche) + " |")
                print("|---|")
                
                print("| " + str(self._cote_gauche) + " |")
                print(" --- ")
            else:
                print(" ------- ")
                print("| " + str(self._cote_gauche) + " | " + str(self._cote_droit) + " |")
                print(" ------- ")
                
                
        def Nb_points(self):
            return self._cote_gauche + self._cote_droit

        def EstBlanc(self):
            return self._cote_gauche == 0 or self._cote_droit == 0

        def EstDouble(self):
            return self._cote_gauche == self._cote_droit

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