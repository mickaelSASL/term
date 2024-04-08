# NSI pratique 2024 sujet 12 - ex1

def tri_selection(tab):
    for i in range(len(tab)-1):
        indice_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab


 
# Les Tests

print(tri_selection([1, 52, 6, -9, 12]))
 
print(tri_selection([1, 52, 6, -9, -12]))

print(tri_selection([100, 52, 6, -9, 12]))