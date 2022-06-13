---
hide:
  - navigation

---

[Retour](../../)


# **Insertion d'une clé dans un Abre Binaire**
## Principe

> Se déplacer dans l'arbre en comparant la valeur à insérer avec les clés jusqu'à atteindre une feuille.


## Algorithme **itératif**  

```
VARIABLES
T : arbre
x : noeud
y : noeud

DEBUT
ARBRE-INSERTION(T,y) :
  x ← T.racine
  TANT QUE T ≠ vide :
    x ← T.racine
    SI y.clé < x.clé :
      T ← x.gauche
    SINON :
      T ← x.droit
    FIN SI
  FIN TANT QUE
  SI y.clé < x.clé :
    insérer y à gauche de x
  SINON :
    insérer y à droite de x
  FIN SI
FIN
```

## Implémentation en Python

```Python
def ArbreInsertion(T: tree, y: Node):
    x = T[0]
    while T != None:
        x = T[0]
        if y.value < x.value:
            T = x.left
        else:
            T = x.right
    if y.value < x.value:
        x.left = y
    else:
        x.right = y
```

## Algorithme **récursif**  

```
VARIABLES
T : arbre
x : noeud
y : noeud

DEBUT
ARBRE-INSERTION_RECURSIF(T,y) :
  SI T ≠ vide
    renvoyer y
  FIN SI

  x ← T.racine
  SI y.clé < x.clé :
    insérer y à gauche de x
  SINON :
    insérer y à gauche de x
  FIN SI
  renvoyer x
FIN
```

## Implémentation en Python

```Python
def ArbreInsertion_recursif(T: tree, y: Node):
    if T == None:
        return y
    
    if y.value < T.value:
        T.left = ArbreInsertion_recursif(T.left, y)
    else:
        T.right = ArbreInsertion_recursif(T.right, y)
    return T
```
