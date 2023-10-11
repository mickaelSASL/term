# **Epreuves Pratiques**
## SUJET 9 - Corrigé

**Exercice 1**

```Python
def moyenne(l):
    s=0
    n = 0
    for nc in l:
        note = nc[0]
        coef = nc[1]
        s=s+note*coef
        n = n+coef
    return s/n
```

**Exercice 2**

```Python
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
```