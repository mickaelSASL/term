# 2022 sujet 36 - ex1
def recherche(tab, n):
    indice_solution = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution


tab, n=  [5, 3],1 
print(tab,n,recherche(tab, n))

tab, n=  [2, 4],2 
print(tab,n,recherche(tab, n))

tab, n=  [2,3,5,2,4],2 
print(tab,n,recherche(tab, n))