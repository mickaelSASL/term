# 2022 sujet 31 - ex1
def recherche(a, t):
    nb = 0
    for element in t:
        if element == a:
            nb += 1
    return nb

print(recherche(5,[]))
print(recherche(5,[-2, 3, 4, 8]))
print(recherche(5,[-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5,[-2, 5, 3, 5, 4, 5]))