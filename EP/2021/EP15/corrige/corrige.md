# **Epreuves Pratiques**
## SUJET 15 - Corrigé

**Exercice 1**

```Python
def RechercheMinMax(tab):
    mini=float("inf")
    maxi=-float("inf")
    if len(tab)==0:
        return {'min':None,'max':None}
    for v in tab:
        if v>maxi:
            maxi=v
        if v<mini:
            mini=v
    return {'min':mini,'max':maxi}
```

**Exercice 2**

```Python
class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        assert c>0 and c<5, "erreur couleur"
        assert v>0 and v<14, "erreur valeur"
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
        for c in range(1,5):
            for v in range(1,14):
                self.contenu.append(Carte(c,v))
        

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        assert pos<52,'erreur position'
        carte = self.contenu[pos]
        return carte

unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
```