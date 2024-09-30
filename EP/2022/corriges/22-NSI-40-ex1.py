# 2022 sujet 40 - ex1

def recherche(elt, tab):
    tab_indices = []
    for i in range(len(tab)):
        if tab[i] == elt:
            tab_indices.append(i)
    return tab_indices        

print(recherche(3, [3, 2, 1, 3, 2, 1]))

print(recherche(4, [1, 2, 3]))