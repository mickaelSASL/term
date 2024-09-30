# 2023 sujet 33 - ex1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre, lettre):
    fils_gauche = arbre[lettre][0]
    fils_droit = arbre[lettre][1]

    if fils_gauche != '' and fils_droit != '':
        return 1 + taille(arbre, fils_gauche) + taille(arbre, fils_droit)

    if fils_gauche != '' and fils_droit == '':
        return 1 + taille(arbre, fils_gauche)

    if fils_gauche == '' and fils_droit != '':
        return 1 + taille(arbre, fils_droit)

    else:
        return 1
 
 
# Les Tests

print(taille(a, 'F'))
