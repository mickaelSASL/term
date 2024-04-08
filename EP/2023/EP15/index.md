<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 15


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

Écrire une fonction `rechercheMinMax` qui prend en paramètre un tableau de nombres non triés `tab`, et qui renvoie la plus petite et la plus grande valeur du tableau sous la forme d’un dictionnaire à deux clés ‘min’ et ‘max’. Les tableaux seront représentés sous forme de liste Python.



Exemples :
```Python
>>>	tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
>>>	resultat = rechercheMinMax(tableau)
>>>	resultat
{'min': -2, 'max': 9}


>>>	tableau = []
>>>	resultat = rechercheMinMax(tableau)
>>>	resultat
{'min': None, 'max': None}
```



**Exercice 2 (4 points)**

On dispose d’un programme permettant de créer un objet de type `PaquetDeCarte`, selon les éléments indiqués dans le code ci-dessous.

Compléter ce code aux endroits indiqués par `#A compléter`, puis ajouter des assertions dans l’initialiseur de `Carte`, ainsi que dans la méthode `getCarteAt()`.



```Python 
class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur-1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
	#A compléter

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        #A compléter

```

Exemple :
```Python
>>>	unPaquet = PaquetDeCarte()
>>>	unPaquet.remplir()
>>>	uneCarte = unPaquet.getCarteAt(20)
>>>	print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
6 de coeur
```