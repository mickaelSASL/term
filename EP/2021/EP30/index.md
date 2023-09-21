<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 30

[Corrigé](corrige.md)

**Exercice 1 (4 points)**

Programmer la fonction `multiplication` prenant en paramètres deux nombres entiers `n1` et `n2`, et qui renvoie le produit de ces deux nombres.

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

Soit `T` un tableau non vide d'entiers triés dans l'ordre croissant et `n` un entier.

La fonction `chercher`, donnée à la page suivante, doit renvoyer un indice où la valeur `n` apparaît éventuellement dans `T`, et `None` sinon.

Les paramètres de la fonction sont :
-	`T`, le tableau dans lequel s'effectue la recherche ;

-	`n`, l'entier à chercher dans le tableau ;
-	`i`, l'indice de début de la partie du tableau où s'effectue la recherche ;
-	`j`, l'indice de fin de la partie du tableau où s'effectue la recherche.

La fonction chercher est une fonction récursive basée sur le principe de la **« recherche par dichotomie »**.

Le code de la fonction commence par vérifier `si 0 <= i et j < len(T)`. Si cette condition n’est pas vérifiée, elle affiche `"Erreur"` puis renvoie `None`.


Recopier et compléter le code de la fonction chercher proposée ci-dessous :

```Python
    def chercher(T,n,i,j):
        if i < 0 or ??? :
            print("Erreur")
            return None
        if i > j :
 
            return None
        m = (i+j) // ???
        if T[m] < ??? :
            return chercher(T, n, ??? , ???)

        elif ??? :
            return chercher(T, n, ??? , ??? )
        else :

            return ???
```

L’exécution du code doit donner :

```Python
>>>	chercher([1,5,6,6,9,12],7,0,10) 
Erreur
>>>	chercher([1,5,6,6,9,12],7,0,5)
>>>	chercher([1,5,6,6,9,12],9,0,5)
4
>>>	chercher([1,5,6,6,9,12],6,0,5)
2 

```
