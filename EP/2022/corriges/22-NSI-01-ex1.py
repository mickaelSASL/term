# 2022 Sujet 1 ex 1
def recherche(caractere, mot):
    somme = 0
    for lettre in mot:
        if lettre == caractere:
            somme += 1
    return somme

# test
print(recherche('e', "sciences"))

print(recherche('i',"mississippi"))
print(recherche('a',"mississippi"))