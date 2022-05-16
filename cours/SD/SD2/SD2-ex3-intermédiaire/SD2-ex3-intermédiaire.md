# SD2 - Exercice 3 - Version intermédiaire

```Python
# Proposition intermédiaire:
# Dans l'éditeur PYTHON
class Piece:
    # nom est une string et surface est un float
    def __init__(self,nom,surface):
        # chaque objet a pour attributs le nom de la pièce(string)
        # et la surface de celle ci(float) en m2.
        # on doit rentrer le couple nom de la pièce et la surface
        # pour chaque pièce.
        self.nom=nom
        self.surface=surface
    
    # Accesseurs: retournent les attributs d'un objet de cette classe
    def getNom(self):
        return self.surface
    
    def getSurface(self):
        ...
    
    # Mutateur: modifient les attributs, ici la surface d'une pièce
    # déjà renseignée
    def setSurface(self,s): # s est un float
        ...
    
    
class Appartement:
    # nom est une string
    def __init__(self,nom):
        #nomme l'appartement et une liste de pièces vide à remplir
        self.listeDePieces=[]
        self.nom=nom
    
    def ajouter(self,piece):
        # ajoute une piece (instance(=objet) de la classe Piece)
        
    def nbPieces(self):
        # retourne le nombre de pièces de l'appartement
        ...
        
    def getSurfaceTotale(self):
        # retourne la surface totale de l'appartement (un float)
        ...
        
    def getListePieces(self): # retourne la liste des pieces
        ...
```