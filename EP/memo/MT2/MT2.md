---
hide:
  - navigation
  - toc
---

[Retour](../../)


# **Calcul de la hauteur d'un arbre binaire**

## Principe
> L'arbre est parcouru récursivement en prenant le sous-arbre le plus grand à chaque noeud interne.

## Algorithme

```
VARIABLES
T : arbre
x : noeud

DEBUT
HAUTEUR(T) :
  si T ≠ vide :
    x ← T.racine
    renvoyer 1 + max(HAUTEUR(x.gauche), HAUTEUR(x.droit))
  sinon :
    renvoyer 0
  fin si
FIN
```

## Implémentation en Python

```Python
def hauteur(T: tree):
    if T != None:
        return 1 + max(hauteur(T.left), hauteur(T.right))
    else:
        return 0
```
