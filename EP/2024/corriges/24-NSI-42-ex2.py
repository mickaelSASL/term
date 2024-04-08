# 24-NSI-42 Ex2
def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""
    debut = 0
    fin = len(tab)
    while debut <= fin and len(tab)>0:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m+1
        else:
            fin = m-1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1)
)
print(dichotomie([], 28)
)
