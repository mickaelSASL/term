# 2022 -sujet 8 - ex2
# On considère la fonction insere ci-dessous qui prend en argument un entier a et un tableau tab d'entiers triés par ordre croissant.
# Cette fonction insère la valeur a dans le tableau et renvoie le nouveau tableau.
# Les tableaux seront représentés sous la forme de listes python.
#
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    # La ligne 2 a pour but de faire une copie du tableau tab afin de ne pas le modifier.
    # On aurait pu utiliser copy.
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        #On échange a avec le précédent
        # tant qu'il est inférieur et que le début de liste n'est pas atteint.
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l


(a, tab)=(-2,[-3,10,20,30,40])
print(insere(a, tab))
(a, tab)=(40,[-3,10,20,30,40])
print(insere(a, tab))
(a, tab)=(50,[-3,10,20,30,40])
print(insere(a, tab))