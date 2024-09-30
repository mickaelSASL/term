# 2022 Sujet 4 ex 1
def recherche(tab):
    solution = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            solution.append((tab[i], tab[i+1]))
    return solution

print(recherche([1, 4, 3, 5]))

print(recherche([1, 4, 5, 3]))
 
print(recherche([7, 1, 2, 5, 3, 4]))
 
print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))