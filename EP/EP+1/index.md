---
hide:
  - navigation

---

# **Epreuves Pratiques**
## SUJET +1

<!-- [Corrigé](corrige.md) -->

## Exercice 1

**Écrire** une fonction ``amplitude()`` qui prend en paramètre un tableau non vide d'entiers non triés *valeurs*, et qui renvoie la valeur de l'amplitude, à savoir la différence entre la plus grande et la plus petite valeur. 

Les tableaux seront représentés sous forme de liste Python.

```python
tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

assert amplitude(tableau) == 11
```

**Compléter** la fonction en vérifiant les préconditions. 

## Exercice 2

On dispose d’un programme permettant de créer un objet de type **Temps**, qui permet de manipuler un temps entré en heures, minutes et secondes.

Les secondes et les minutes sont des entiers positifs, inférieurs à 60. Dans les méthodes ``ajouter_secondes()`` et ``ajouter_minutes()``, si les secondes (ou les minutes) dépassent 59, on doit les convertir en minutes (ou respectivement en heure).

La méthode ``__str__()`` est une méthode native qui est appelée quand on tente de convertir un objet en chaine de caractères. La méthode de cette classe renvoie une chaine de caractères sous la forme "hh : mm : ss". Par exemple, pour un objet initialisé avec les valeurs 3h,20min et 2s, la méthode renverrait "3 : 20: 2"

La méthode ``en_secondes()`` permet de convertir le temps en secondes. La méthode ``est_plus_petit()`` compare deux objets temps et renvoie True si l'objet temps passé en paramètre est le plus grand des deux.

Compléter ce code aux endroits indiqués par ..., puis ajouter des assertions dans l’initialiseur de **Temps**.
On devra créer deux instances de la classe Temps, avec pour valeurs 1h,59min et 45s et l'autre avec 2h,15min et 13s. 

```python
class Temps:
    """Initialise Temps (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s
        
    def ajouter_minutes(self, mins):
        """incrémente les minutes de la valeur mins passée en paramètre"""
        self.minutes = self.minutes + mins
        while ... :
            self.heures += 1
            self.minutes = self.minutes - 60
            
            
    def ajouter_secondes(self, secs):
        """incrémente les secondes de la valeur secondes passée en paramètre"""
        self.secondes = self.secondes + secs
        while ... :
            ...
            self.secondes = self.secondes - 60
    
       
    def __str__(self):
        """renvoie une chaine de caractères sous la forme hh : mm : ss"""
        return ...+" : "+...+" : "+...
    
    def en_secondes(self):
        """Convertit un temps en heures/minutes/secondes en secondes"""
        return ...
    
    def est_plus_petit (self, tps) :
        """Compare deux temps entre eux. Renvoie True si l'objet est plus petit que l'objet tps passé en paramètre"""
        return ...
```

    



```Python
#Test du code
...
...
t1.ajouter_secondes(20)

assert str(t1)== "2 : 0 : 5"
assert t1.est_plus_petit(t2) == True
```
