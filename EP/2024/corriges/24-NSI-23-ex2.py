# NSI pratique 2024 sujet - ex2

def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses :
        i = 0
        while i <= nb_boites and boites[i] + masse > c:
            # Tant qu'on a pas atteint la premiÃ¨re boite vide
            #et que la masse ne rentre pas on avance dans la liste de boites.
            i = i + 1
        if i == nb_boites + 1:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1

# Tests
print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))