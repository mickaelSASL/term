---
hide:
  - navigation
  - toc
---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
[Retour](../../)


# **Calcul de la taille d'un arbre binaire**

## Principe
> L'arbre est parcouru récursivement en additionnant :
> 
> 1 + taille du sous-arbre gauche + taille du sous-arbre droit
> 
> (1 représente la taille de la racine).

## Algorithme

```
VARIABLES
T : arbre
x : noeud

DEBUT
TAILLE(T) :
  si T ≠ vide :
    x ← T.racine
    renvoyer 1 + TAILLE(x.gauche) + TAILLE(x.droit)
  sinon :
    renvoyer 0
  fin si
FIN
```

## Implémentation en Python

```Python
def taille(T: tree):
    if T != None:
        return 1 + taille(T.left) + taille(T.right)
    else:
        return 0
```