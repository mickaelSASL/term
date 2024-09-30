#2022 - sujet 26 - ex1
def RechercheMin(tab):
    indice_min = 0
    for i in range(len(tab)):
        if tab[i] < tab[indice_min]:
            indice_min = i
    return indice_min

print(RechercheMin([5]))
print(RechercheMin([2, 4, 1]))
print(RechercheMin([5, 3, 2, 2, 4]))