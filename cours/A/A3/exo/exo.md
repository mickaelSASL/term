---
hide:
  - navigation
  - toc
---

# **A3 : Méthode Diviser pour Régner**

[Retour](../)
[Corrigé](exo_corrige.md)

## Exercice 1 (bac)

**Question 1**

a. Quel est l’ordre de grandeur du coût, en nombre de comparaisons, de l’algorithme de tri fusion pour une liste de longueur `n` ?

b. Citer le nom d’un autre algorithme de tri. Donner l’ordre de grandeur de son coût, en nombre de comparaisons, pour une liste de longueur `n`. Comparer ce coût à celui du tri fusion. Aucune justification n’est attendue.

L’algorithme de tri fusion utilise deux fonctions `moitie_gauche` et `moitie_droite` qui prennent en argument une liste `L` et renvoient respectivement :

* la sous-liste de `L` formée des éléments d’indice strictement inférieur à `len(L)//2` ;

* la sous-liste de `L` formée des éléments d’indice supérieur ou égal à `len(L)//2`. On rappelle que la syntaxe `a//b` désigne la division entière de `a` par `b`.

> Par exemple,
```Python
>>> L = [3, 5, 2, 7, 1, 9, 0]
>>> moitie_gauche(L)
[3, 5, 2]
>>> moitie_droite(L)
[7, 1, 9, 0]
>>> M= [4, 1, 11, 7]
>>> moitie_gauche(M)
[4, 1]
>>> moitie_droite(M)
[11, 7]
```

L’algorithme utilise aussi une fonction `fusion` qui prend en argument deux listes triées `L1` et `L2` et renvoie une liste `L` triée et composée des éléments de `L1` et `L2`.

On donne ci-dessous le code python d’une fonction récursive `tri_fusion` qui prend en argument une liste `L` et renvoie une nouvelle liste triée formée des éléments de `L`.

```Python
def tri_fusion(L):
         n = len(L)
         if n<=1 :
                 return L
         print(L)
         mg = moitie_gauche(L)
         md = moitie_droite(L)
         L1 = tri_fusion(mg)
         L2 = tri_fusion(md)
         return fusion(L1, L2)
```

**Question 2**
Donner la liste des affichages produits par l’appel suivant : `tri_fusion([7, 4, 2, 1, 8, 5, 6, 3])`  

**Question 3**
Écrire la fonction `moitie_droite`.

**Question 4**
On donne ci-dessous une version incomplète de la fonction `fusion`.

```Python
def fusion(L1, L2):
    L = []
    n1 = len(L1)
    n2 = len(L2)
    i1 = 0
    i2 = 0
    while i1 < n1 or i2 < n2 :
        if i1 >= n1:
            L.append(L2[i2])
            i2 = i2 + 1
        elif i2 >= n2:
            L.append(L1[i1])
            i1 = i1 + 1
        else:
           e1 = L1[i1]
           e2 = L2[i2]

...
...

    return L
```

> * Si aucun des deux indices n’est valide, la boucle `while` est interrompue ;  
* Si `i1` n’est plus un indice valide, on va ajouter à `L` les éléments de `L2` à partir de l’indice `i2` ;  
* Si `i2` n’est plus un indice valide, on va ajouter à `L` les éléments de `L1` à partir de l’indice `i1` ;  
* Sinon, le plus petit élément non encore traité est ajouté à `L` et on décale l’indice correspondant.  

Écrire les instructions manquantes des lignes 17 à 22 permettant d’insérer dans la liste `L` les éléments des listes `L1` et `L2` par ordre croissant.

## Exercice 2 (bac)

Dans un tableau Python d'entiers `tab`, on dit que le couple d’indices `(i, j)` forme une inversion lorsque  `i < j` et `tab[i] > tab[j]`. On donne ci-dessous quelques exemples. 
> * Dans le tableau `[1, 5, 3, 7]`, le couple d’indices `(1,2)` forme une inversion car `5 > 3`.  
Par contre, le couple `(1,3)` ne forme pas d'inversion car `5 < 7`.  Il n’y a qu’une inversion dans ce tableau. 
* Il y a trois inversions dans le tableau `[1, 6, 2, 7, 3]`, à savoir les couples d'indices `(1, 2)`, `(1, 4)` et `(3, 4)`. 
* On peut compter six inversions dans le tableau `[7, 6, 5, 3]` : les couples d'indices `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)` et `(2, 3)`. 
On se propose dans cet exercice de déterminer le nombre d’inversions dans un tableau quelconque. 
 
** Questions préliminaires **  
1.	Expliquer pourquoi le couple `(1, 3)` est une inversion dans le tableau `[4, 8, 3, 7]`.  
2.	Justifier que le couple `(2, 3)` n’en est pas une. 
 
### Partie A : Méthode itérative 
Le but de cette partie est d’écrire une fonction itérative `nombre_inversion` qui renvoie le nombre d’inversions dans un tableau. Pour cela, on commence par écrire une fonction `fonction1` qui sera ensuite utilisée pour écrire la fonction `nombre_inversion`.  

1. On donne la fonction suivante. 
 
```Python
def fonction1(tab, i):
    nb_elem = len(tab)
    cpt = 0
    for j in range(i+1, nb_elem):
        if tab[j] < tab[i]: 
            cpt += 1
    return cpt 
```

a. Indiquer ce que renvoie la fonction1(tab, i) dans les cas suivants. 
* Cas n°1 : `tab = [1, 5, 3, 7]` et `i = 0`. 
* Cas n°2 : `tab = [1, 5, 3, 7]` et `i = 1`. 
* Cas n°3 : `tab = [1, 5, 2, 6, 4]` et `i = 1`. 
 
b. Expliquer ce que permet de déterminer cette fonction. 
 
 
2. En utilisant la fonction précédente, écrire une fonction `nombre_inversion(tab)` qui prend en argument un tableau et renvoie le nombre d’inversions dans ce tableau. On donne ci-dessous les résultats attendus pour certains appels. 

```Python 
>>> nombre_inversions([1, 5, 7]) 
0 
>>> nombre_inversions([1, 6, 2, 7, 3]) 
3 
>>> nombre_inversions([7, 6, 5, 3]) 
6 
```

3.	Quelle est l’ordre de grandeur de la complexité en temps de l'algorithme obtenu ? Aucune justification n'est attendue. 
 
 
### Partie B : Méthode récursive 
 
Le but de cette partie est de concevoir une version récursive de la fonction `nombre_inversion`.  
On définit pour cela des fonctions auxiliaires. 
1.	Donner le nom d’un algorithme de tri ayant une complexité meilleure que quadratique. 
 
Dans la suite de cet exercice, on suppose qu’on dispose d'une fonction `tri(tab)` qui prend en argument un tableau et renvoie un tableau contenant les mêmes éléments rangés dans l'ordre croissant. 
 
2. Écrire une fonction `moitie_gauche(tab)` qui prend en argument un tableau `tab` et renvoie un nouveau tableau contenant la moitié gauche de `tab`. Si le nombre d'éléments de `tab` est impair, l'élément du centre se trouve dans cette partie gauche. On donne ci-dessous les résultats attendus pour certains appels. 

```Python
>>> moitie_gauche([]) 
[] 
>>> moitie_gauche([4, 8, 3]) 
[4, 8] 
>>> moitie_gauche ([4, 8, 3, 7]) 
[4, 8] 
```
 
Dans la suite, on suppose qu’on dispose de la fonction `moitie_droite(tab)` qui renvoie la moitié droite sans l’élément du milieu. 

3.	On suppose qu’une fonction `nb_inv_tab(tab1, tab2)` a été écrite. Cette fonction renvoie le nombre d’inversions du tableau obtenu en mettant bout à bout les tableaux `tab1` et `tab2`, à condition que `tab1` et `tab2` soient triés dans l’ordre croissant.  On donne ci-dessous deux exemples d’appel de cette fonction : 

```python 
>>> nb_inv_tab([3, 7, 9], [2, 10]) 
3 
>>> nb_inv_tab([7, 9, 13], [7, 10, 14]) 
3 
```

En utilisant la fonction `nb_inv_tab` et les questions précédentes, écrire une fonction récursive `nb_inversions_rec(tab)` qui permet de calculer le nombre d'inversions dans un tableau. Cette fonction renverra le même nombre que `nombre_inversions(tab)` de la partie A. On procédera de la façon suivante :  
 
* Séparer le tableau en deux tableaux de tailles égales (à une unité près). 
* Appeler récursivement la fonction `nb_inversions_rec` pour compter le nombre d’inversions dans chacun des deux tableaux. 
* Trier les deux tableaux (on rappelle qu'une fonction de tri est déjà définie). 
* Ajouter au nombre d'inversions précédemment comptées le nombre renvoyé par la fonction `nb_inv_tab` avec pour arguments les deux tableaux triés. 
