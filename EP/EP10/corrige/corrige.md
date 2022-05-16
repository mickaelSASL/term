# **Epreuves Pratiques**
## SUJET 10 - Corrigé

**Exercice 1**

```Python
def maxi(tab):
    m = tab[0]
    ind = 0
    for i in range(1,len(tab)):
        if tab[i]>m:
            m=tab[i]
            ind=i
    return (m,ind)
```

**Exercice 2**

```Python
def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2
```