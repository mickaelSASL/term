# Sujet 30 #

# Exercice 1

def fusion(tab1, tab2):
    tableau = []
    while tab1 != [] and tab2 != []:
        if tab1[0] <= tab2[0]:
            tableau.append(tab1.pop(0))
        else:
            tableau.append(tab2.pop(0))
    while tab1 != []:
        tableau.append(tab1.pop(0))
    while tab2 != []:
        tableau.append(tab2.pop(0))
    return tableau

print(fusion([3, 5], [2, 5]))
print(fusion([4], [2, 6]))
print(fusion([], []))
print(fusion([1, 2, 3], []))

# Exercice 2

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]
    
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIV"))

