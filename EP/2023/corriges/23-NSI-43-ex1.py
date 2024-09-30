# 2023 sujet 43 - ex1

def ecriture_binaire_entier_positif(n):
    # cas particulier pour n = 0
    if n == 0:
        return [0]
    # cas général
    b = []
    while n != 0:
        b.append(n % 2)
        n = n // 2
    b.reverse()
    return b
 
 
# Les Tests

n=0
print(n,ecriture_binaire_entier_positif(n))
print('----------')
n=2
print(n,ecriture_binaire_entier_positif(n))
print('----------')
n=105
print(n,ecriture_binaire_entier_positif(n))
print('----------')