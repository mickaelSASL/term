# **Epreuves Pratiques**
## SUJET 9 - Corrigé

**Exercice 1**

```Python
def conv_bin(n):
    b=[]
    bit=0
    while n > 0:
        b.append(n%2)
        n=n//2
        bit=bit+1
    b.reverse()
    return (b,bit)
```

**Exercice 2**

```Python
def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp= T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


def tri_bulles_bis(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if T[j] < T[j-1]:
                temp= T[j]
                T[j] = T[j-1]
                T[j-1] = temp
    return T
```