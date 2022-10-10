# SD2 - Programmation Orientée Objet

## Exercice 1 - CORRIGE

**Utilisation d’objets**

===! "Question 1"

    ```Python
    #1. Créer la carte Valet de COEUR que l'on nommera c1.
    c1=Carte('Valet', 'COEUR')
    ```
=== "Question 2"

    ```Python
    #2. Afficher le nom, la valeur et la couleur de c1.
    print('c1 = ',c1.getNom(), c1.getValeur() , c1.getCouleur() )
    ```
=== "Question 3"

    ```Python
    #3. Créer la carte As de PIQUE que l'on nommera c2.
    c2=Carte('As', 'PIQUE')
    ```
=== "Question 4"

    ```Python
    #4. Afficher le nom, la valeur et la couleur de c2.
    print('c2 = ',c2.getNom(), c2.getValeur() , c2.getCouleur() )
    ```
=== "Question 5"

    ```Python
    #5. Modifier le nom de la carte c2 en Roi et afficher les attributs de c2
    c2.setNom('Roi')
    print('c2 = ',c2.getNom(), c2.getValeur() , c2.getCouleur() )
    ```
=== "Question 6"

    ```Python
    #6. Créer la carte 8 de TREFLE que l'on nommera c3.
    c3=Carte('8', 'TREFLE')
    ```
=== "Question 7"

    ```Python
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


===! "Question 1"

    ```Python
    # 1. créer une pièce « chambre1 » , de surface 20 m2 et une pièce « chambre2 » », de surface 15 m2
    chambre1 = Piece("chambre1", 20)
    chambre2 = Piece("chambre2", 15)
    ```

=== "Question 2"

    ```Python
    # 2. créer une pièce « séjour » », de surface 25 m2 et une pièce « sdb » », de surface 10 m2
    sejour = Piece("séjour", 25)
    sdb = Piece("sdb", 10)
    ```

=== "Question 3"

    ```Python
    # 3. créer une pièce « cuisine » », de surface 12 m2
    cuisine = Piece("cuisine", 12)
    ```

=== "Question 4"

    ```Python
    # 4. créer un appartement « appart205 » qui contiendra toutes les pièces créées
    appart205 = Appartement("Appart205")
    appart205.ajouter(chambre1)
    appart205.ajouter(chambre2)
    appart205.ajouter(sejour)
    appart205.ajouter(sdb)
    appart205.ajouter(cuisine)
    ```

=== "Question 5"

    ```Python
    # 5. afficher la surface totale de l’appartement créé.
    print(appart205.SurfaceTotale())
    ```

=== "Question 6"

    ```Python
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
___

## Exercice 4 - CORRIGE

===! "Question 1"

    ```Python
    toto = Toto(1, 2, 3)
    titi = Toto(2, 1, 6)

    ```

=== "Question 2"

    a) `meth1()`
    b) 
    ```Python
    def meth3(self, c):
        self.att3 = self.att3 * c

    ```

=== "Question 3"

    ```Python
    titi.meth1()

    ```

=== "Question 4"
    ```Python
    toto.meth3(2)

    ```
=== "Question 5"

    ```Python
    >>> print(toto == titi)
    False
    ```

    |               |    toto    |    titi    |                           |
    |:-------------:|:----------:|------------|---------------------------|
    |  Question 1   |  (1, 2, 3) |  (2, 1, 6) | *instanciation*           | 
    |  Question 3   |  (1, 2, 3) |  (1, 2, 6) | *inversion dans titi*     |
    |  Question 4   |  (1, 2, 6) |  (1, 2, 6) | *multiplication dan toto* |

    Les valeurs de `i`, `j`, `k` sont les mêmes pour `toto` et `titi` mais le test est effectué sur les objets et non les valeurs de leurs attributs.
___

## Exercice 5 - CORRIGE

===! "Question 1"

    ```Python
    def __init(self, x, y, z)__:
        self.x = x
        self.y = y
        self.z = z
    ```

=== "Question 2"

    ```Python
    def avance(self):
        self.x = x + 1
    
    def droite(self):
        self.y = y + 1

    def saute(self):
        self.z = z + 1
    ```

=== "Question 3"

    ```Python
    def coord(self):
        return (x, y, z)
    
    ```

=== "Question 4"

    ```Python
    class Personnage:
    
        def __init(self, x, y, z)__:
            self.x = x
            self.y = y
            self.z = z

        def avance(self):
            self.x = x + 1
        
        def droite(self):
            self.y = y + 1

        def saute(self):
            self.z = z + 1

        def coord(self):
            return (x, y, z) 
    ```

    ```Python
    Laura = Personnage(0, 0, 0)
    Laura.avance()
    Laura.saute()
    Laura.droite()
    print(Laura.coord())
    ```

    Retour de la console : `>>> (1, 1, 1)`
___

## Exercice 6 - CORRIGE

```
Il permet d'effectuer un tirage aléatoire de 100 valeurs et d'en afficher la moyenne.
```

___

## Exercice 7 - CORRIGE

===! "Questions 1 & 2"
    ```Python
    class Carre:
        def __init(self, cote):
            self.cote = cote

        def perimetre():
            return 4 * self.cote

        def aire():
            return self.cote**2
    ```

=== "Question 3"
    ```Python
    c1 = Carre(3)
    c2 = Carre(2)
    print(c1.perimetre)
    print(c1.aire)
    print(c2.perimetre)
    print(c2.aire)
    ```

    Retour de la console : 
    ```
    12
    9
    8
    4

    ```