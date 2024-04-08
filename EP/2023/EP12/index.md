<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 12


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

Écrire une fonction `maxi` qui prend en paramètre une liste tab de nombres entiers et qui renvoie un couple donnant le plus grand élément de cette liste ainsi que l’indice de la première apparition de ce maximum dans la liste.

Exemple :
```Python
>>>	maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
```



**Exercice 2 (4 points)**

La fonction `recherche` prend en paramètres deux chaines de caractères gene et seq_adn et renvoie True si on retrouve gene dans seq_adn et False sinon.

Compléter le code Python ci-dessous pour qu’il implémente la fonction recherche.

```Python
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
    j = 0
    while j < g and gene[j] == seq_adn[i+j]:
    ...
    if j == g:
    trouve = True
    ...
    return trouve
```

Exemples :

>>>	recherche("AATC", "GTACAAATCTTGCC")
True

>>>	recherche("AGTC", "GTACAAATCTTGCC") False

