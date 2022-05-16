---
hide:
  - navigation
  - toc
---

[Retour](../../)


# **Parcours d'un arbre binaire en ordre *préfixe***

## Principe
> L'arbre est parcouru récursivement dans l'ordre :  
> 
> * Racine  
> * Sous-Arbre Gauche  
> * Sous-Arbre Droit  

## Algorithme

```
VARIABLES
T : arbre
x : noeud

DEBUT
PARCOURS-PREFIXE(T) :
  si T ≠ vide :
    x ← T.racine
    affiche x.clé
    PARCOURS-PREFIXE(x.gauche)
    PARCOURS-PREFIXE(x.droit)
  fin si
FIN

```

## Implémentation en Python

```Python
def ParcoursPrefixe(T: tree):
    if T != None:
        x = T[0]
        print(x.value)
        ParcoursPrefixe(x.left)
        ParcoursPrefixe(x.right)
```