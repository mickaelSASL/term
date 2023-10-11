# **Epreuves Pratiques**
## SUJET 4 - Corrigé

**Exercice 1**

```Python
def moyenne(tab):
    s = 0
    for v in tab:
        s=s+v
    moy=s/len(tab)
    return moy

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5
```


**Exercice 2**

```Python
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab)==0:
        return False,1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or x>tab[len(tab)-1]:
        return False,2
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1			
    return False,3
```