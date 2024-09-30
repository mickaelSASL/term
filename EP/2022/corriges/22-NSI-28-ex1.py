#2022 - sujet 28 - ex1
def moyenne(tab):
    somme = 0
    for val in tab:
        somme += val
    return somme / len(tab)

print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))