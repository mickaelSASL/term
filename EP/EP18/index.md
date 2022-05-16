<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 18


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et tab un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt` dans `tab` si `elt` est dans `tab` et `-1` sinon.



Exemples :
```Python
>>>	recherche(1, [2, 3, 4])
-1
>>>	recherche(1, [10, 12, 1, 56])
2
>>>	recherche(50, [1, 50, 1])
1
>>>	recherche(15, [8, 9, 10, 15])
3
```


**Exercice 2 (4 points)**

On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un tableau `tab` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans le tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de listes python.


```Python 
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = ...
    while a < ... and i>=0: 
      l[i+1] = ...
      l[i] = a
      i = ...
    return l
```


Compléter la fonction `insere` ci-dessus.

Exemples :
```Python
>>>	insere(3,[1,2,4,5])
[1, 2, 3, 4, 5]
>>>	insere(10,[1,2,7,12,14,25]) 
[1, 2, 7, 10, 12, 14, 25]
>>>	insere(1,[2,3,4])
[1, 2, 3, 4]
```