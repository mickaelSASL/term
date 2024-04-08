# **Epreuves Pratiques**
## SUJET 22 - Corrigé

**Exercice 1**

```Python
def recherche (a,t):
    nbr=0
    for v in t:
        if v==a:
            nbr=nbr+1
    return nbr


```

**Exercice 2**

```Python
def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due 
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i-1
    return rendu
```