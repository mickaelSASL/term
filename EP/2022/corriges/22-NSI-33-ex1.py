# 2022 sujet 33 - ex1

def convertir(T):
    poids =  len(T)-1
    valeur = 0
    for elt in T:
        valeur += 2**poids * elt
        poids -=1
    return valeur

T=[1, 0, 1, 0, 0, 1, 1]
print(T,convertir(T))

T=[1, 0, 0, 0, 0, 0, 1, 0]
print(T,convertir(T))