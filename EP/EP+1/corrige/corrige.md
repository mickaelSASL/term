# **Epreuves Pratiques**
## SUJET 1+ - Corrigé

**Exercice 1**
```Python

def amplitude(valeurs):
    assert len(valeurs) > 0, "tableau vide"  # On s'assure que le tableau ne soit pas vide

    mini = valeurs[0]                 # Minimum et maximum initialisé à la première valeur de la liste
    maxi = valeurs[0]                 ## Ne pas initialiser à 0 !!

    for element in valeurs :          # Parcours par élément car pas besoin de l'indice
        
        if element < mini :           # Comparaison pour identifier le minimum
            mini = element
        if element > maxi :           # Comparaison pour identifier le maximum
            maxi = element
    
    return maxi - mini                # La fonction renvoie l'amplitude (différence entre maxi et mini)

tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

# Test pour vérifier l'exactitude du résultat renvoyé
assert amplitude(tableau) == 11

# Test avec un tableau vide
assert amplitude([])

```

**Exercice 2**

```Python
class Temps:
    """Initialise Temps (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s

    def ajouter_minutes(self, mins):
        """incrémente les minutes de la valeur mins passée en paramètre"""
        self.minutes = self.minutes + mins
        while self.minutes > 59 :
            self.heures += 1
            self.minutes = self.minutes - 60


    def ajouter_secondes(self, secs):
        """incrémente les secondes de la valeur secondes passée en paramètre"""
        self.secondes = self.secondes + secs
        while self.secondes > 59 :
            self.ajouter_minutes(1)
            self.secondes = self.secondes - 60


    def __str__(self):
        """renvoie une chaine de caractères sous la forme hh : mm : ss"""
        return str(self.heures) + " : " + str(self.minutes) + " : " + str(self.secondes)

    def en_secondes(self):
        """Convertie un temps en heures/minutes/secondes en secondes"""
        return self.heures*3600 + self.minutes*60 + self.secondes

    def est_plus_petit (self, tps) :
        """Compare deux temps entre eux. Renvoie True si l'objet est plus petit que l'objet tps passé en paramètre"""
        return self.en_secondes() < tps.en_secondes()

    def __lt__ (self, tps) :
        """Compare deux temps entre eux. Renvoie True si l'objet est plus petit que l'objet tps passé en paramètre"""
        return self.en_secondes() < tps.en_secondes()


#Test du code
t1 = Temps(1,59,45)
t2 = Temps(2,15,13)
t1.ajouter_secondes(20)
#assert str(t1)== "2 : 0 : 5"
assert t1.est_plus_petit(t2) == True
assert t1 < t2

```