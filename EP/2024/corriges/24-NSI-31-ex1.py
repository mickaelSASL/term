# Sujet 31 #

# Exercice 1

def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n1 == 0:
        return 0
    if n1 == 1:
        return n2
    else:
        return n2 + multiplication(n1-1, n2)
    
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

# Exerice 2

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))