<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 26

[Corrigé](corrige.md)

**Exercice 1 (4 points)**

Écrire une fonction `occurrence_max` prenant en paramètres une chaîne de caractères `chaine` et qui renvoie le caractère le plus fréquent de la chaîne. La chaine ne contient que des lettres en minuscules sans accent.

On pourra s’aider du tableau

```Python
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
```
et du tableau `occurrence` de 26 éléments où l’on mettra dans `occurrence[i]` le nombre d’apparitions de `alphabet[i]`dans la chaine. Puis on calculera l’indice `k` d’un maximum du tableau `occurrence` et on affichera `alphabet[k]`.

Exemple :
```Python

>>>	ch = ‘je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique’

>>>	occurrence_max(ch)
‘e’
```

**Exercice 2 (4 points)**

On considère une image en 256 niveaux de gris que l’on représente par une grille de nombres, c’est-à-dire une liste composée de sous-listes toutes de longueurs identiques.

La largeur de l’image est donc la longueur d’une sous-liste et la hauteur de l’image est le nombre de sous-listes.

Chaque sous-liste représente une ligne de l’image et chaque élément des sous-listes est un entier compris entre 0 et 255, représentant l’intensité lumineuse du pixel.

Compléter le programme ci-dessous :

```Python
def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return ...

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return ...

def negatif(image):
    '''renvoie le négatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(...):
            L[i][j] = ...
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inférieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(...):
            if image[i][j] < ... : #correction
                L[i][j] = ...
            else:
                L[i][j] = ...
    return L

```

Exemple :

```Python
>>> img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

>>> nbLig(img)
4

>>> nbCol(img)
5

>>> negatif(img)
[[235, 221, 1, 110, 249], [232, 131, -32, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]

>>> binaire(img,120)
[[0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1,
1]]
```
