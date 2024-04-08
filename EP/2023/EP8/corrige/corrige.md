# **Epreuves Pratiques**
## SUJET 8 - Corrigé

**Exercice 1**

```Python
def recherche(caractere,mot):
    s=0
    for c in mot:
        if caractere==c:
            s=s+1
    return s

```

**Exercice 2**

```Python
Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p,solution ,i)
    else :
        return rendu_glouton(arendre, solution, i+1)
```