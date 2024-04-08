# **Epreuves Pratiques**
## SUJET 21 - Corrigé

**Exercice 1**

```Python
def nb_repetitions(elt,tab):
    nbre=0
    for v in tab:
        if v==elt:
            nbre=nbre+1
    return nbre
```

**Exercice 2**

```Python
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a>0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a
```