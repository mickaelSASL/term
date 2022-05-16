---
hide:
  - navigation
  - toc
---
# **Epreuves Pratiques**
## SUJET +2



## Exercice 1 :

Un groupe d’amis est allé au restaurant et souhaite partager équitablement la note.

Ce que doit chacun des amis est contenu dans un dictionnaire contenant son nom et son montant.

Exemple : ```{"Henry": 12, "Thierry": 15}```

**Écrire** une fonction `partager` qui prend en paramètre un dictionnaire non vide associant les montants de chaque ami, et qui renvoie la somme totale, ainsi que la valeur moyenne que chacun devra payer, au centime près.

```Python
groupe = {"Henry": 12,
          "Thierry": 15,
          "Samir": 20,
          "Sylvain": 13}

assert partager(groupe) == (60, 15.0)


groupe = {"Henry": 12,
          "Thierry": 15,
          "Samir": 20}

assert partager(groupe) == (47, 15.67)
```

_Rappel_ : la fonction `round` permet d'arrondir un nombre réel avec le nombre de décimales souhaité.

```
>>> round(40.532469, 3)
40.532
```

## Exercice 2 :

On souhaite utiliser un arbre binaire de recherche afin de classer des noms par ordre alphabétique.

Cet ABR sera implémenté par une classe **Noeud**.

La fonction `inserer` doit permettre d'insérer un mot donné à un arbre. Elle prend en paramètre l'arbre ainsi que le mot à insérer, et renvoie l'arbre modifié.

La fonction `afficher` doit permettre d'afficher par ordre alphabétique les mots contenus dans un ABR passé en paramètre. 

```python
class Noeud:
    def __init__(self, mot, gauche=None, droite=None):
        self.gauche = gauche
        self.droite = droite
        self.mot = mot

def inserer(arbre_binaire, mot):
    '''Insère un élément dans l'arbre binaire de recherche.'''
    if arbre_binaire is None :
        arbre_binaire = ...
    elif mot < arbre_binaire.mot :
        arbre_binaire.gauche = ...
    elif  mot > arbre_binaire.mot :
        arbre_binaire.droite = ...
    return arbre_binaire



def afficher(arbre_binaire):
    '''Affiche les mots par ordre alphabétique.'''
    if arbre_binaire ... :
        afficher(...)
        print(...)
        afficher(...)

arbre = None
arbre = inserer(arbre, "kiwi")
arbre = inserer(arbre, "pomme")
arbre = inserer(arbre, "abricot")
arbre = inserer(arbre, "mangue")
arbre = inserer(arbre, "poire")
afficher(arbre)


```
**Compléter** les fonctions *récursives* `parcours` et `recherche` afin qu'elles respectent leurs spécifications.

```python
arbre = None
arbre = inserer(arbre,"kiwi")
arbre = inserer(arbre,"pomme")
arbre = inserer(arbre,"abricot")
arbre = inserer(arbre,"mangue")
arbre = inserer(arbre,"poire")
afficher(arbre)
```