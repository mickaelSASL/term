<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 10


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

Écrire une fonction maxi qui prend en paramètre une liste `tab` de nombres entiers et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la première apparition de ce maximum dans la liste.

Exemple :
```Python
>>>	maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
```


**Exercice 2 (4 points)**

Cet exercice utilise des piles qui seront représentées en Python par des listes (type `list`). On rappelle que l’expression `T1 = list(T)` fait une copie de `T` indépendante de `T`, que l’expression `x = T.pop()` enlève le sommet de la pile `T` et le place dans la variable `x` et, enfin, que l’expression `T.append(v)`place la valeur `v` au sommet de la pile `T`.

Compléter le code Python de la fonction `positif` ci-dessous qui prend une pile T de nombres entiers en paramètre et qui renvoie la pile des entiers positifs dans le même ordre, sans modifier la variable `T`.


```Python
def positif(T):
    T2 = ...(T)
    T3 = ...
    while T2 != []:
        x = ...
        if ... >= 0:
            T3.append(...)
    T2=[]
    while T3 != ...:
        x = T3.pop()
        ...
    print('T = ',T)
    return T2
```

Exemple :
```Python
>>>	positif([-1,0,5,-3,4,-6,10,9,-8 ]) 
T = [-1, 0, 5, -3, 4, -6, 10, 9, -8] 
[0, 5, 4, 10, 9]
```