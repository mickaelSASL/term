---
hide:
  - navigation
  - toc
---

[Retour](../../)


# **Parcours d'un arbre binaire en ordre *suffixe***

## Principe
> L'arbre est parcouru récursivement dans l'ordre :  
> 
> * Sous-Arbre Gauche  
> * Sous-Arbre Droit  
> * Racine  

## Algorithme

```
VARIABLES
T : arbre
x : noeud

DEBUT
PARCOURS-SUFFIXE(T) :
  si T ≠ vide :
    x ← T.racine
    PARCOURS-SUFFIXE(x.gauche)
    PARCOURS-SUFFIXE(x.droit)
    affiche x.clé
  fin si
FIN
```

## Implémentation en Python

```Python
def ParcoursSuffixe(T: tree):
    if T != None:
        x = T[0]
        ParcoursSuffixe(x.left)
        ParcoursSuffixe(x.right)
        print(x.value)
```