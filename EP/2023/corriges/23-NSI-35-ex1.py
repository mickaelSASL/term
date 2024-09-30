# 2023 sujet 35 - ex1

def xor(a,b):
    resultat = []
    for i in range(len(a)):
        if a[i]==b[i]:
            resultat.append(0)
        else:
            resultat.append(1)
    return resultat
 
# autre solution

def xor2(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(tab1[i] ^ tab2[i])
    return resultat

# Les Tests

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

print(xor(a,b),xor2(a,b))
print(xor(c,d),xor2(c,d))