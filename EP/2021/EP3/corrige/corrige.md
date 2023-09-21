# **Epreuves Pratiques**
## SUJET 3 - Corrigé

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
**Exercice 1(bis) avec récursivité**

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
def dichotomie(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False
```
