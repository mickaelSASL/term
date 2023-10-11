# **Epreuves Pratiques**
## SUJET 3


[Corrigé](corrige.md)


**Exercice 1 (4 points)**
Programmer la fonction `multiplication`, prenant en paramètres deux nombres entiers `n1` et `n2`, et qui renvoie le produit de ces deux nombres.
Les seules opérations autorisées sont l’addition et la soustraction.

Exemples :
```Python
>>>	multiplication(3,5)
15
>>>	multiplication(-4,-8)
32
>>>	multiplication(-2,6)
-12
>>>	multiplication(-2,0)
0
```

**Exercice 2 (4 points)**

Recopier et compléter sous Python la fonction suivante en respectant la spécification. On ne recopiera pas les commentaires.

```Python
def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...

        if x > tab[m]:
             = m + 1
        else:
            fin = ...
    return ...
```

Exemples :
```Python
>>>	dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
True
>>>	dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) 
False
```