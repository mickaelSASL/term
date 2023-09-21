# **Epreuves Pratiques**
## SUJET 1 - Corrigé

**Exercice 1**

```Python
def recherche(tab, n):
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice
```

**Exercice 2**

```Python
from math import sqrt   # import de la fonction racine carrée

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus     
    courte distance du point depart."""
    assert type(tab)==list, "tab doit être une liste"
    assert type(depart)==tuple, "depart doit être un tuple"
    
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist :
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
```