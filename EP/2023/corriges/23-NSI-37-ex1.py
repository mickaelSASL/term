# 2023 sujet 37 - ex1

def recherche(elt, tab):
    for i in range(len(tab)-1, -1, -1):
        # on parcourt le tableau à l'envers
        # Attention aux indices
        if tab[i] == elt:
            return i
    return -1

# Autre solution en parcourant le tableau dans l'ordre

def recherche2(elt,tab):
        indice = -1
        for i in range(len(tab)):
            if tab[i] == elt:
                indice = i
        return indice
 
# Les Tests

print(recherche(1, [2, 3, 4]))
print(recherche2(1, [2, 3, 4]))
print('---')
print(recherche(1, [10, 12, 1, 56]))
print(recherche2(1, [10, 12, 1, 56]))
print('---')
print(recherche(1, [1, 0, 42, 7]))
print(recherche2(1, [1, 0, 42, 7]))
print('---')
print(recherche(1, [1, 50, 1]))
print(recherche2(1, [1, 50, 1]))
print('---')
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))
print(recherche2(1, [8, 1, 10, 1, 7, 1, 8]))
