# 2022 -sujet 11 - ex1
#Écrire une fonction recherche qui prend en paramètres un tableau tab de nombres entiers triés par ordre croissant
# et un nombre entier n, et qui effectue une recherche dichotomique du nombre entier n dans le tableau non vide tab.
# Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le tableau, -1 sinon.
def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab) - 1
    while ind_debut <= ind_fin:
        ind_milieu = (ind_debut + ind_fin) // 2
        if tab[ind_milieu] == n:
            return ind_milieu
        elif tab[ind_milieu] < n:
            ind_debut = ind_milieu + 1
        else:
            ind_fin = ind_milieu - 1
    return -1

(tab, n)=([-10,-5,0,2,3,5,20],5)
print((tab, n),recherche(tab, n))

(tab, n)=([2, 3, 4, 5, 6],3)
print((tab, n),recherche(tab, n))

(tab, n)=([2, 3, 4, 6, 7],5)
print((tab, n),recherche(tab, n))

(tab, n)=([2, 3, 4, 6, 7],2)
print((tab, n),recherche(tab, n))

(tab, n)=([2, 3, 4, 6, 7],7)
print((tab, n),recherche(tab, n))