# **Epreuves Pratiques**
## SUJET 9 - Corrigé

**Exercice 1**

```Python
def maxi(tab):
    m=tab[0]
    ind=0
    for i in range(1,len(tab)):
        if tab[i]>m:
            m=tab[i]
            ind=i
    return (m,ind)
```

**Exercice 2**

```Python
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j=j+1
        if j == g:
            trouve = True
        i=i+1
    return trouve
```