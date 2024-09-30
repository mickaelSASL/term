# 2023 sujet 31 - ex1

def recherche(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme
 
 
# Les Tests
caractere='e'
chaine='sciences'
print(caractere,chaine,recherche(caractere, chaine))
print('---------------------')
caractere='i'
chaine='mississippi'
print(caractere,chaine,recherche(caractere, chaine))
print('---------------------')
caractere='a'
chaine='mississippi'
print(caractere,chaine,recherche(caractere, chaine))
print('---------------------')