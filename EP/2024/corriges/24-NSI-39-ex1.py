# 2024 NSI sujet 39 - ex 1

def recherche(elt, tab):
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == elt:
            return i
    return None

print(recherche(1, [2, 3, 4])) # renvoie None
print(recherche(1, [10, 12, 1, 56])) #2
print(recherche(1, [1, 0, 42, 7])) #0
print(recherche(1, [1, 50, 1])) #2
print(recherche(1, [8, 1, 10, 1, 7, 1, 8])) #5