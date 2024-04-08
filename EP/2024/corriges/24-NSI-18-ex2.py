# NSI pratique 2024 sujet 18 - ex2

def dichotomie(tab, x):
    """
    tab : tableau dâ€™entiers triÃ© dans lâ€™ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2 # ou debut + (fin-debut)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

# tests
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))


#tests
for n1 in range(-3,4):
    for n2 in range (-3,4):
        print((n1, n2),multiplication(n1, n2),multiplication2(n1, n2),multiplication3(n1, n2))