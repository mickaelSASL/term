# 2022 - sujet 20 - ex2
#Compléter la fonction est_magique qui prend en paramètre un carré et qui renvoie
# la valeur de la somme si ce carré est magique, False sinon.
class Carre:
    def __init__(self, tableau = [[]]):
        # Attention ici la variable est modifiée par la fonction
        self.ordre = len(tableau)
        self.valeurs = tableau

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])

    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0) 

    #test de la somme de chaque ligne
    for i in range(1,n):
        #Par la peine de tester la ligne d'indice 0,
        # elle a servi à calculer la somme de référence s   .
        if carre.somme_ligne(i) != s:
            return False
    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s: #
            return False
    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s: #
        # La diagonale principale se caractérise par des indices
        # de lignes et de colonne identiques.
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
    return s   #

c=Carre([[1, 1],
        [1, 1]])
Carre.affiche(c)
print(est_magique(c))

c=Carre([[2, 9, 4],
         [7, 5, 3],
        [6, 1, 8]])
Carre.affiche(c)
print(est_magique(c))

c=Carre([[4, 5, 16, 9],
         [14, 7, 2, 11],
         [3, 10, 15, 6],
         [13, 12, 8, 1]])
Carre.affiche(c)
print(est_magique(c))