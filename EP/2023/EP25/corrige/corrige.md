# **Epreuves Pratiques**
## SUJET 25 - Corrigé

**Exercice 1**

```Python
def recherche(tab):
    couples=[]
    n = len(tab)
    for i in range(n-1):
        if tab[i]==tab[i+1]-1 :
            couples.append((tab[i],tab[i+1]))
    return couples
```

**Exercice 2**

```Python
def propager(M, i, j, val):
    if M[i][j]== 0:
        return

    M[i][j]=val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)
```