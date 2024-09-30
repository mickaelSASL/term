# 2023 sujet 6 - ex1


def recherche(tab, n):
    indice_solution = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution

# Les Tests

print(recherche([5, 3],1))
print(recherche([5, 3],5))
print(recherche([2,3,5,2,4],2))