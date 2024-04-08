# 2024 NSI sujet - ex 1

def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(tab1[i] ^ tab2[i])
    return resultat

#ou ---------

def ou_exc(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 0
 
def ou_exclusif2(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(ou_exc(tab1[i],tab2[i]))
    return resultat

print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
#[1, 1, 0, 1, 1, 0, 0, 1]
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))
#[1, 1, 1, 0]
print(ou_exclusif2([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
#[1, 1, 0, 1, 1, 0, 0, 1]
print(ou_exclusif2([1, 1, 0, 1], [0, 0, 1, 1]))
#[1, 1, 1, 0]

