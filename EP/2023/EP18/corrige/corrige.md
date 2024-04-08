# **Epreuves Pratiques**
## SUJET 18 - Corrigé

**Exercice 1**

```Python
def recherche(elt,tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
```

**Exercice 2**

```Python
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < l[i] and i>-1:
        l[i+1] = l[i]
        l[i] = a
        i = i-1
    return l
```