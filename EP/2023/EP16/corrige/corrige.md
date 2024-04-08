# **Epreuves Pratiques**
## SUJET 16 - Corrigé

**Exercice 1**

```Python
def moyenne (tab):
    s=0
    n = len(tab)
    for v in tab:
        s=s+v
    moy = s/n
    return moy
```

**Exercice 2**

```Python
def dec_to_bin(a):
    bin_a = str(a%2)
    a=a//2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a
```