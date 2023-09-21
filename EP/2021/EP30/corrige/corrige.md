# **Epreuves Pratiques**
## SUJET 30 - Corrigé

**Exercice 1**

```Python
def multiplication(n1,n2):
    s=0
    if n1<0 :
        a=-n1
    else :
        a=n1
    if n2<0 :
        b=-n2
    else :
        b=n2

    for i in range(a):
        s=s+b
    if (n1>0 and n2<0) or (n2>0 and n1<0): 
        return -s
    else :
        return s
```

** OU **

```Python
def multiplication(n1,n2):
    s=0
    if n1==0 or n2==0:
        return 0
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    for i in range(n2):
        s = s+n1
    return s
```
**Exercice 2**

```Python
def chercher(T,n,i,j):
    if i < 0 or j>=len(T) :
        print("Erreur")
        return None    
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m+1 , j)
    elif T[m] > n  :
        return chercher(T, n, i , m-1 )
    else :
        return m 
```