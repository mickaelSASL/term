# SD2 - Programmation Orientée Objet

## Exercice 1

### Utilisation d’objets
> Voici la classe `Carte` dont on vous donne les en-têtes de méthodes :

```Python
class Carte:
    def __init__(self, nom, couleur):
        # Affectation de l'attribut nom et de l'attribut couleur
        couleur = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
        noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 
                'Roi', 'As']
        valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
        
    def setNom(self, nom):
        # Mutateur de l'attribut nom (de la liste noms)
        
    def getNom(self):
        # renvoie le nom de la carte (de la liste noms): Accesseur
        
    def getCouleur(self):
        # renvoie la couleur de la carte (de la liste couleur): Accesseur
        
    def getValeur(self):
        # renvoie la valeur de la carte (du dictionnaire valeurs) : Accesseur
        
    def egalite(self, carte):
        ''' Renvoie True si les cartes self et carte ont même valeur, False sinon
        carte: Objet de type Carte '''
        
    def estSuperieureA(self, carte):
        ''' Renvoie True si la valeur de self est supérieure à celle de carte,
        False sinon
        carte: Objet de type Carte
        '''
        
    def estInferieureA(self, carte):
        ''' Renvoie True si la valeur de self est inférieure à celle de carte,
        False sinon
        carte: Objet de type Carte
        '''
```

**Ecrire (sur feuille) un programme principal qui va :**  

1. Créer la carte Valet de CŒUR que l’on nommera c1.  
2. Afficher le nom, la valeur et la couleur de c1.  
3. Créer la carte As de PIQUE que l’on nommera c2.  
4. Afficher le nom, la valeur et la couleur de c2.  
5. Modifier le nom de la carte c2 en Roi et afficher le nom, la valeur et la couleur de c2.  
6. Créer la carte 8 de TREFLE que l’on nommera c3.  
7. Comparer les cartes c1 et c2 puis c1 et c3.

___
## Exercice 2

### Utilisation d’objets
> On suppose écrites les classes `Piece` et `Appartement`, dont on vous donne les en-têtes de méthodes :

```Python
class Piece:
    # nom est une string et surface est un float
    def __init__(self,nom,surface):
        self.nom=nom
        self.surface=surface
        
    # Accesseurs: retournent les attributs d'un objet de cette classe    
    def getSurface(self):
        return self.surface
    
    def getNom(self):
        return self.nom

    # Mutateur
    def setSurface(self,s): # s est un float,
    ...


class Appartement:
    # nom est une string
    def __init__(self,nom):
        # L'objet est une liste de pièces (objets issus de la classe Piece)
        self.listeDePieces=[]
        self.nom=nom
        
    # Accesseurs:
    def getNom(self):        
        return self.nom

    # pour ajouter une pièce de classe Piece  
    def ajouter(self,piece):
        ...

    # pour avoir le nombre de pièces de l'appartement   
    def nbPieces(self): #
        ...

    # retourne la surface totale de l'appartement (un float)    
    def SurfaceTotale(self):
        ...

    # retourne la liste des pièces avec les surfaces    
    def getListePieces(self): # sous forme d'une liste de tuples
        ...

```

**Ecrire, sur feuille, un programme principal utilisant ces deux classes qui va :**

1. Créer une pièce "chambre1", de surface 20 m² et une pièce "chambre2", de surface 15 m².
2. Créer une pièce "séjour", de surface 25 m² et une pièce "sdb", de surface 10 m².
3. Créer une pièce "cuisine", de surface 12 m².
4. Créer un appartement "appart205" qui contiendra toutes les pièces créées.
5. Afficher la surface totale del'appartement créé.
6. Afficher la liste des pièces et surfaces de l'appartement créé.








___
## Exercice 3

### Rédaction de méthodes
> On utilise les classes `Piece` et `Appartement` de l'exercice 2, les en-têtes de méthodes restent identiques mais vous allez devoir les compléter : (... : parties à compléter)

**Consignes :**  

*En cas de difficulté, rendez-vous à la [version intermédiaire](./SD2-ex3-intermédiaire.md)*  

Le test suivant sera exécuté
```Python
# Programme de test
a=Appartement('appt25')
p1=Piece("chambre", 11.1)
p2=Piece("sdbToilettes", 7)
p3=Piece("cuisine", 7)
p4=Piece("salon", 21.3)
print(p4.getNom(),p4.getSurface())
p1.setSurface(12.6)
a.ajouter(p1)
a.ajouter(p2)
a.ajouter(p3)
a.ajouter(p4)
print(a.getNom(),a.getListePieces())
print('nb pièces =', a.nbPieces(),', Surface totale =',a.SurfaceTotale())
```
Il devra retourner :
```Python
# Dans la console Python

salon 21.3
appt25 [('chambre', 12.5), ('sdbToilettes', 7), ('cuisine', 7), ('salon', 21.3)]
nb pièces = 4 , Surface totale = 47.9
```

1. Finaliser la classe `Piece` : écrire les méthodes accesseurs et mutateurs de la classe `Piece`  

2. Finaliser la classe `Appartement`:  
     a. Ecrire la méthode qui permet d'ajouter une pièce (`ajouter(self, piece)`) dans la liste des pièces présentes dans l'appartement.  
     b. Ecrire la méthode qui permet de retourner le nombre de pièces (`nbPieces(self)`) présentes dans l'appartement.  
     c. Ecrire la méthode `getSurfaceTotale(self)`, qui renvoie la surface totale de l'appartement.  
     d. Ecrire la méthode `getlistePieces(self)`, qui renvoie la liste des pièces de l'appartement.  
3. Créer un tableau qui classe les méthodes de ces deux classes suivant leur type :  

|               | Constructeurs | Accesseurs | Mutateurs | Autres |
|:-------------:|:-------------:|------------|-----------|:------:|
|    `Piece`    |               |            |           |        |
| `Appartement` |               |            |           |        |



___
## Exercice 4

On donne ci-dessous le code en Python d’une classe nommée Toto. Chaque objet de cette classe a 3 attributs de type entier et dispose de 3 méthodes. Le code d’une de ces méthodes n’est pas complètement écrit.

```Python
class Toto:
    def __init__(self, i, j, k): 
        self.att1 = i
        self.att2 = j         
        self.att3 = k 
    
    def meth1(self):         
        tmp = self.att1         
        self.att1 = self.att2         
        self.att2 = tmp 
    
    def meth2(self): 
        return self.att3 

     def meth3(self, c):         
        # code à compléter 

```
1. Écrire la ligne de code qui crée un objet de nom toto de la classe `Toto`, dont les attributs `att1`, `att2` et `att3` contiennent respectivement 1, 2 et 3. De même créer un objet de nom `titi` de la même classe et contenant 2, 1 et 6 dans ses attributs `att1`, `att2` et `att3`.  
 
2.  
a.	Quel est le nom de la méthode de la classe `Toto` qui échange les attributs `att1` et `att2` ?  
b.	Compléter le code de la méthode `meth3` afin qu’elle prenne en argument l’entier c et qu’elle multiplie l’argument `att3` par `c`.  
 
3.	Écrire la ligne de code permettant, à l’aide des méthodes de la classe `Toto` d’échanger les attributs `att1` et `att2` de `titi`.  
 
4.	Écrire la ligne de code permettant, à l’aide d’une méthode de la classe `Toto` de multiplier par 2 l’attribut `att3` de `toto`.  
 
5.	Toutes les lignes de codes précédentes ayant été exécutées, que va afficher l’instruction print(`toto` == `titi`) ? Expliquer. 

___
## Exercice 5

On considère une classe `Personnage` représentant un personnage de Jeu.  
    Le plateau de jeu est représenté par un repère orthonormé à trois axes.  
    La position du joueur dans le plateau est repérée par ses attributs `x`, `y`, `z`.  
  
1)	Ecrire un constructeur initialisant les mesures.  
2)	Ecrire les méthodes `avance`, `droite` et `saute` permettant respectivement de faire avancer, aller à droite et sauter le personnage, c’est-à-dire d’augmenter de 1 respectivement `x`, `y` et `z`.  
3)	Implémenter une autre méthode `coord` renvoyant les coordonnées sous forme d’un triplet.  
4)	Essayer avec : `Laura = Personnage(0, 0, 0)`  

___
## Exercice 6

Voici un programme en Python :  
  
```Python
import random

class Piece :  
    def alea(self) :  
        return random.randint(0, 1)  

    def moyenne(self, n):  
        tirage = []              
        for i in range (n) :                  
            tirage.append(self.alea())              
        return sum(tirage) / n  

p = Piece()  
print(p.moyenne(100))  
```  

Expliquer en détail ce qu’il permet d’afficher. 

___
## Exercice 7

On considère une classe `Carre` admettant la mesure des côtés d’un carré en attribut.  
  
1)	Ecrire un constructeur initialisant les mesures.  

2)	Ecrire les méthodes :  
- `perimetre` : permettant de retourner le périmètre du carré.  
- `aire` : permettant de retourner son aire.  

3)	Créer des exemples. 
