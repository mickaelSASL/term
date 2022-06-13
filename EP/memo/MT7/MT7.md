---
hide:
  - navigation

---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
[Retour](../../)


# **Recherche d'une clé dans un Abre Binaire**

## Principe

> On parcours l'arbre en comparant la valeur recherchée avec les différents noeuds jusqu'à trouver la valeur ou atteindre une feuille (dans ce cas la valeur n'est pas présente dans l'arbre).

## Algorithme

```
VARIABLES
T : arbre
x : noeud
k : entier

DEBUT
ARBRE-RECHERCHE(T,k) :
  si T == vide :
    renvoyer faux
  fin si
  x ← T.racine
  si k == x.clé :
    renvoyer vrai
  fin si
  si k < x.clé :
    ARBRE-RECHERCHE(x.gauche,k)
  sinon :
    ARBRE-RECHERCHE(x.droit,k)
  fin si
FIN
```

## Implémentation en Python

```Python
def ArbreRecherche(T: tree, k: int):
    if T == None:
        return False
    x = T[0]
    if k == x.value:
        return True
    if k < x.value:
        ArbreRecherche(x.left, k)
    else:
        ArbreRecherche(x.right, k)
```

## Complexité

* Pire des cas (arbre complet) :  $$ O(log.2(n)) $$

* Meilleur des cas (arbre filiforme) : $$ O(n) $$