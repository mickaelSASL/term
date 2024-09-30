# 2023 sujet 13 - ex1 fd

# Écrire en langage Python une fonction recherche prenant comme paramètres une
# variable a de type numérique (float ou int) et un tableau tab (de type list) et qui
#  renvoie le nombre d'occurrences de a dans tab.

def recherche(a,tab):
    '''In  : a float ou int
       Out : int, nb d'occurrences de a dans tab.
       '''
    compteur =0
    for element in tab:
        if element==a:
            compteur+=1
    return compteur
        
# tests

(a, tab)=(5, [])
print((a, tab),recherche(a, tab))
print('---------------------')
(a, tab)=(5, [-2, 3, 4, 8])
print((a, tab),recherche(a, tab))
print('---------------------')
(a, tab)=(5, [-2, 3, 1, 5, 3, 7, 4])
print((a, tab),recherche(a, tab))
print('---------------------')
(a, tab)=(5, [-2, 5, 3, 5, 4, 5])
print((a, tab),recherche(a, tab))
print('---------------------')