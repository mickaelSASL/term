# **Epreuves Pratiques**
## SUJET 2 - Corrigé

**Exercice 1**

```Python
def moyenne(tab):
    N=len(tab)
    if N==0:
        return "erreur"
    else :
        s = 0
        moy = 0
        for v in tab :
            s=s+v
        moy = s/N
        return moy
```

**Exercice 2**

```Python
def tri(tab):
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i]=valeur
            j= j-1
    return tab
```
