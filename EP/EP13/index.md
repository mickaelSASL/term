<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 13


[Corrigé](corrige.md)



**Exercice 1 (4 points)**

Écrire une fonction `tri_selection` qui prend en paramètre une liste `tab` de nombres entiers et qui renvoie le tableau trié par ordre croissant. On utilisera l’algorithme suivant :

* on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice 0 ;
* on recherche le second plus petit élément du tableau, et on l'échange avec l'élément d'indice 1 ;
* on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.



Exemple :
```Python
>>>	tri_selection([1,52,6,-9,12])
[-9, 1, 6, 12, 52]
```


**Exercice 2 (4 points)**


Le jeu du « plus ou moins » consiste à deviner un nombre entier choisi entre 1 et 99.  

Un élève de NSI décide de le coder en langage Python de la manière suivante :
* le programme génère un nombre entier aléatoire compris entre 1 et 99 ;
* si la proposition de l’utilisateur est plus petite que le nombre cherché, l’utilisateur en est averti. Il peut alors en tester un autre ;
* si la proposition de l’utilisateur est plus grande que le nombre cherché, l’utilisateur en est averti. Il peut alors en tester un autre ;
* si l’utilisateur trouve le bon nombre en 10 essais ou moins, il gagne ;
* si l’utilisateur a fait plus de 10 essais sans trouver le bon nombre, il perd.

> La fonction `randint` est utilisée. Si `a` et `b` sont des entiers, `randint(a,b)` renvoie un nombre entier compris entre `a` et `b`.

Compléter le code ci-dessous et le tester :

```Python
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,...)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : ")) 
    compteur = ...
    while nb_mystere != ... and compteur < ... :
        compteur = compteur + ...
        if nb_mystere ... nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",...)
        print("Nombre d'essais: ",...)
    else:
        print ("Perdu ! Le nombre était ",...)
```