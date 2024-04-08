# NSI pratique 2024 sujet 15 - ex1

def moyenne(tab):
    somme = 0
    for valeur in tab:
        somme += valeur
    return somme / len(tab)

# tests
print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))