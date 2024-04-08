# 2024 NSI sujet 36 - ex 1

def recherche(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme

print(recherche('e', "sciences")) #2 
print(recherche('i',"mississippi")) #4 
print(recherche('a',"mississippi")) #0