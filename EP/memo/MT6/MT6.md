---
hide:
  - navigation

---

[Retour](../../)


# **Parcours d'un arbre binaire en largeur d'abord**

## Principe
> L'arbre est parcouru en commençant à la racine puis tous les noeuds voisins à la profondeur actuelle avant de passer aux noeuds au prochain niveau de profondeur.

## Algorithme

```
VARIABLES
T : arbre
Tg : arbre
Td : arbre
x : noeud
f : file (initialement vide)

DEBUT
PARCOURS-LARGEUR(T) :
  enfiler(T.racine, f) //on place la racine dans la file
  tant que f non vide :
    x ← defiler(f)
    affiche x.clé
    si x.gauche ≠ vide :
      Tg ← x.gauche
      enfiler(Tg.racine, f)
    fin si
    si x.droit ≠ vide :
      Td ← x.droite
      enfiler(Td.racine, f)
    fin si
  fin tant que
FIN

```
## Implémentation en Python

```Python
def ParcoursLargeur(T: tree):
    f = []
    f.append(T[0])
    
    while len(f) > 0:
        x = f.pop()
        print(x.value)
        if x.left != None:
            Tg = x.left
            f.insert(0, Tg[0])
        if x.right != None:
            Td = x.right
            f.insert(0, Td[0])
```