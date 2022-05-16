---
hide:
  - navigation
  - toc
---

[Retour](../../)


# **Parcours d'un arbre binaire en ordre *infixe***

## Principe
> L'arbre est parcouru récursivement dans l'ordre :  
> 
> * Sous-Arbre Gauche  
> * Racine  
> * Sous-Arbre Droit  


## Algorithme
```
VARIABLES
T : arbre
x : noeud

DEBUT
PARCOURS-INFIXE(T) :
  si T ≠ vide :
    x ← T.racine
    PARCOURS-INFIXE(x.gauche)
    affiche x.clé
    PARCOURS-INFIXE(x.droit)
  fin si
FIN
```

## Implémentation en Python

```Python
def ParcoursInfixe(T: tree):
    if T != None:
        x = T[0]
        ParcoursInfixe(x.left)
        print(x.value)
        ParcoursInfixe(x.right)
```