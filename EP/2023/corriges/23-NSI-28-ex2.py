# 2023 sujet 28 - ex2

#Le but de l'exercice est de compléter une fonction qui détermine si une valeur est présente
#dans un tableau de valeurs triées dans l'ordre croissant.
#L'algorithme traite le cas du tableau vide et il est écrit pour que la recherche dichotomique
#ne se fasse que dans le cas où la valeur est comprise entre les valeurs extrêmes du
#tableau.
#On distingue les trois cas qui renvoient False en renvoyant False, 1, False, 2 et
#False, 3.
#Compléter l'algorithme de dichotomie donné ci-après.


def dichotomie(tab, x):
    """
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

# tests

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1))
print(dichotomie([],28))
