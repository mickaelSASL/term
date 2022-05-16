# SD2 - Programmation Orientée Objet

## Exercice 1 - CORRIGE

** Utilisation d’objets**

```Python
#1. Créer la carte Valet de COEUR que l'on nommera c1.
c1=Carte('Valet', 'COEUR')

#2. Afficher le nom, la valeur et la couleur de c1.
print('c1 = ',c1.getNom(), c1.getValeur() , c1.getCouleur() )

#3. CrÃ©er la carte As de PIQUE que l'on nommera c2.
c2=Carte('As', 'PIQUE')

#4. Afficher le nom, la valeur et la couleur de c2.
print('c2 = ',c2.getNom(), c2.getValeur() , c2.getCouleur() )

#5. Modifier le nom de la carte c2 en Roi et afficher les attributs de c2
c2.setNom('Roi')
print('c2 = ',c2.getNom(), c2.getValeur() , c2.getCouleur() )

#6. CrÃ©er la carte 8 de TREFLE que l'on nommera c3.
c3=Carte('8', 'TREFLE')

#7. Comparer les cartes c1 et c2 puis c1 et c3.
if c1.egalite(c2):
    print(c1.getNom(), " est égale à ",c2.getNom())
elif c1.estSuperieureA(c2):
   print(c1.getNom(), " est supérieure à ",c2.getNom())
else:
    print(c1.getNom(), " est inférieure à ",c2.getNom())
    
if c1.egalite(c3):
    print(c1.getNom(), " est égale à ",c3.getNom())
elif c1.estSuperieureA(c3):
   print(c1.getNom(), " est supérieure à ",c3.getNom())
else:
    print(c1.getNom(), " est inférieure à ",c3.getNom())

```

___

## Exercice 2 - CORRIGE

**Utilisation d’objets**

```Python
# 1. créer une pièce « chambre1 » , de surface 20 m2 et une pièce « chambre2 » », de surface 15 m2
chambre1 = Piece("chambre1", 20)
chambre2 = Piece("chambre2", 15)

# 2. créer une pièce « séjour » », de surface 25 m2 et une pièce « sdb » », de surface 10 m2
sejour = Piece("séjour", 25)
sdb = Piece("sdb", 10)

# 3. créer une pièce « cuisine » », de surface 12 m2
cuisine = Piece("cuisine", 12)

# 4. créer un appartement « appart205 » qui contiendra toutes les pièces créées
appart205 = Appartement("Appart205")
appart205.ajouter(chambre1)
appart205.ajouter(chambre2)
appart205.ajouter(sejour)
appart205.ajouter(sdb)
appart205.ajouter(cuisine)

# 5. afficher la surface totale de l’appartement créé.
print(appart205.SurfaceTotale())

# 6. afficher la liste des pièces et surfaces de l’appartement créé.
print(appart205.getListePieces())

```
___

## Exercice 3 - CORRIGE

**Rédaction de méthodes**

```Python
class Piece:
    def __init__(self,nom,surface):  # Constructeur
        self.nom=nom
        self.surface=surface
        
    def getSurface(self):            # accesseur
        return self.surface
    
    def getNom(self):                # accesseur
        return self.nom
    
    def setSurface(self,s):          # mutateur
        self.surface=s
    
class Appartement:
    def __init__(self,nom):          # Constructeur
        self.listeDePieces=[]
        self.nom=nom
    
    def getNom(self):                # accesseur
        return self.nom
    
    def ajouter(self,piece):         # mutateur
        self.listeDePieces.append(piece)
    
    def nbPieces(self):              # autre nbPieces N’EST PAS un attribut de la classe Appartement
        return len(self.listeDePieces)
    
    def getSurfaceTotale(self):      # accesseur
        total=0
        for piece in self.listeDePieces:
            surf=piece.getSurface()
            total=total+surf
        return total

    def getListePieces(self):        # accesseur
        L=[]
        for piece in self.listeDePieces:
            surf=piece.getSurface()
            nom=piece.getNom()
            L.append((nom,surf))
        return L
```