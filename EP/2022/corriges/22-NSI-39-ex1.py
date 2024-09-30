# 2022 sujet 39 - ex1

def moyenne(tab):
    somme = 0
    for val in tab:
        somme += val
    return somme / len(tab)

print(moyenne([10,20,30,40,60,110]))