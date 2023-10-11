# **Epreuves Pratiques**
## SUJET 17 - Corrigé

**Exercice 1**

```Python
def RechercheMin(tab):
    mini=tab[0]
    ind = 0
    for i in range(len(tab)):
        if tab[i]<mini:
            mini=tab[i]
            ind=i
    return ind
```


**Exercice 2**

```Python
def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j-1
    return tab
```