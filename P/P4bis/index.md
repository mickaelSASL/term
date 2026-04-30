---
hide:
    - toc
---    

# **P4: Résolution de labyrinthe par les graphes**  
<img src="https://files.realpython.com/media/Build-a-Pac-Man-Maze-Solver-in-Python_Watermarked.c2e79a85fc99.jpg" alt="donnees" width="75%">

*<center>Le but du projet est résoudre des labyrinthes générés aléatoirement. Les labyrinthes peuvent être vus comme des graphes.</center>*

___

## Propriétes des labyrinthes
Nous nous intéresserons seulement à des labyrinthes rectangulaires composés de n lignes et m colonnes sur une grille régulière composée de n×m cellules. Chaque cellules comportant 4 côtés dont chacun peut être ouvert ou fermé (présence d'un mur).

<center>
  <img src="./labyrinthe/labyrinthe_1.png" alt="labyrinthe">
  <figcaption>grille vide avec murs extérieurs</figcaption>
</center>

> * Deux cellules sont consécutives si elles partagent un côté.
> * Un chemin dans un labyrinthe est une suite finie de n cellules où chacune est consécutive avec sa suivante.
> * Un labyrinthe est dit parfait s'il existe un et un seul chemin connectant 2 cellules.
> 
> |Exemple 1|Exemple 2|Exemple3|
> |:-:|:-:|:-:|
> |<img src="./labyrinthe/labyrinthe_2.png" alt="labyrinthe">|<img src="./labyrinthe/labyrinthe_3.png" alt="labyrinthe">|<img src="./labyrinthe/labyrinthe_4.png"alt="labyrinthe"> |
> |<figcaption>Chemin</figcaption>|<figcaption>plusieurs chemins</figcaption>|<figcaption>parfait</figcaption>|


!!! question  
    Montrer que pour un labyrinthe rectangulaire de n lignes et m colonnes le nombre maximal de murs internes fermés est : $2nm - n - m$


## Création d'un labyrinthe

La création d'un labyrinthe suit les étapes suivantes: 

1. Générer un graphe G représentant une grille de taille m*n  
1. Construire un **arbre couvrant** A de ce graphe  
1. Dessiner le labyrinthe en traçant un mur entre les sommets directement liés dans G et non dans A  

___  
### 1. Générer une grille de taille m * n

Un labyrinthe, composé de longueur × largeur cases numérotées par des couples (i, j), est représenté par un graphe (non orienté) dont les sommets sont étiquetés par des couples (i, j). Lorsqu’une case (i0, j0) communique avec une autre case voisine (i1, j1), alors il existe une arête entre les sommets (i0, j0) et (i1, j1) du graphe. Deux cases (ou sommets) sont particuliers, ce sont l’entrée (0,0) et la sortie du labyrinthe.  
Soit le labyrinthe suivant :

#### Présentation de la structure de données représentant la géométrie d'un labyrinthe
Le labyrinthe de taille 4x4 suivant :  
<center><img src="./labyrinthe/labyrinthe_5.png" width="180"></center>  
est représenté par la matrice Python suivante :

```Python
grille = 
[[[False, True, True, True], [False, False, False, True], [ False, False, True, False], [ False, False, True, False]],
[[ True, True, True, False], [ False, True, False, True], [ True, True, True, True], [ True, False, False, True]],
[[ True, True, False, False], [ False, False, True, True], [ True, True, False, False], [ False, False, True, True]],
[[ False, True, False, False], [ True, False, False, True], [ False, True, False, False], [ True, True, False, True]]]
```

Il s'agit d'une matrice de dimension 4x4 et l'élément `grille[i][j]`, `i` et `j` étant deux entiers compris entre 0 et 3, décrit la géométrie de la case à l'intersection de la ligne `i` et de la colonne `j`.

Exemple :  
`une_case = grille[2][1] = [False, False, True, True]` correspond à la case du labyrinthe à l'intersection de la ligne `2` et de la colonne `1`.
<center><img src="./labyrinthe/labyrinthe_6.png" width="250"></center>

Description des éléments de la liste représentant `une_case = [False, False, True, True]`:  

* Indice 1 : valeur `False` : booléen qui indique ici la **présence** d'un mur **en haut** de la case est présent.
* Indice 2 : valeur `False` : booléen qui indique ici la **présence** d'un mur **à droite** de la case est présent.
* Indice 3 : valeur `True` : booléen qui indique ici l'**absence** de mur **en bas** de la case est présent.
* Indice 4 : valeur `True` : booléen qui indique ici l'**absence** de mur **à gauche** de la case est présent.
___  
### 2. Construire un **arbre couvrant** A de ce graphe

#### Qu'est ce qu'un arbre couvrant ?
Un **arbre** est un graphe à la fois connexe et sans cycle. Un **arbre couvrant** d'un graphe est un arbre inclus dans ce graphe et qui connecte tous les sommets du graphe.
<center><img src="./labyrinthe/labyrinthe_7.png" width="200"></center>

En plaçant un sommet sur chaque cellule de notre labyrinthe, et en reliant deux sommets par une arête si leurs cellules sont séparées par une porte, il devient possible de dessiner un arbre à partir de n'importe quel labyrinthe.  

Sur notre graphe, un arête est donc un passage dans notre labyrinthe.

<center><img src="./labyrinthe/labyrinthe_8.png" width="200"></center>


!!! question  
    Représenter l'arbre du graphe ci-dessus avec en étiquette les coordonnées de chaque noeud.


#### constuire l'arbre binaire
De nombreux algorithmes existent pour répartir toutes ces portes de manière à ce que toutes les cellules soient accessibles et qu'il n'existe qu'un unique chemin entre l'entrée et la sortie, dont le parcours en profondeur et l'algorithme de Kruskal. Chaque algorithme est différent et produit des labyrinthes visuellement différents.

<center><img src="./labyrinthe/labyrinthe_9.gif" width="200"></center>
<p>L'algorithme du parcours en profondeur (ou "recursive backtracker" en anglais) commence sur une cellule aléatoire dans le labyrinthe.
Il suffit ensuite de se diriger dans une direction aléatoire et de casse le mur face à soi, tout en marquant la cellule précédente comme visitée.
Lorsque plus aucune direction n'est disponible, l'algorithme "remonte" à la position précédente : c'est le backtracking.</p>


___  
## Cahier des charges :

Le modèle de représentation afin de modéliser des labyrinthes rectangulaires est une classe `Labyrinthe` qui contiendra les *méthodes* et les *attributs* suivants :
 
* un **constructeur** : `__init__(self, largeur, hauteur)`  
* des **attributs** :  `self.largeur`, le nombre de colonnes de la grille et `self.hauteur`, le nombre de lignes définis dans le constructeur
* un **attribut** :  `self.grille` représentant les cellules du labyrinthe.  

!!! question  
	Écrire la méthode `solution` de la classe `Labyrinthe` (un parcours en profondeur) renvoyant un chemin permettant de se rendre d’une cellule de départ à une cellule d’arrivée. Vous testerez votre code dans le fichier <a href="./labyrinthe.py" target="_blank">labyrinthe.py</a>.


___ 

## Le code du programme :

```Python
class Cellule:
	def __init__(self):
		self.mur_bas = True # True signifie que le mur est fermé
		self.mur_droit = True # False signifie que le mur est ouvert


class Labyrinthe:
	def __init__(self, largeur, hauteur):
		self.hauteur = hauteur
		self.largeur = largeur
		self.grille = [[Cellule() for j in range(largeur)] for i in range(hauteur)]
		self.generation()
	
	def solution(self, depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne):
		"""
		Renvoie la liste de directions à suivre pour se rendre de la cellule
		(depart_ligne, depart_colonne) à la cellule (arrivee_ligne, arrivee_colonne).
		Exemple de retour : ['n', 'e', 'e', 's', 'o']
		"""

	        
    
    def generation(self):
        nombre_cellules = self.largeur*self.hauteur
        zones_cellules = list(range(nombre_cellules))
        # Les cellules sont numérotées en ligne, avec les numéros 0 à 
        # largeur-1 sur la première ligne, largeur à 2*largeur-1 sur la
        # deuxième ... jusqu'à hauteur*largeur-1 en bas à droite
        murs_modifiables = list(range(2*nombre_cellules-self.largeur-self.hauteur))
        # Tous les murs bas et droits sont modifiables sont ceux en bas ou à 
        # droite du labyrinthe. Ils sont numérotés en commençant par les murs
        # verticaux dans le même ordre que les cellules. Les murs numéro 0 à
        # self.largeur*self.hauteur-self.hauteur-1 sont les murs verticaux, et 
        # ceux allant de self.largeur*self.hauteur-self.hauteur à 
        # 2*self.largeur*self.hauteur-self.largeur-self.hauteur-1 les horizontaux.
        indice_premier_non_modifiable = len(murs_modifiables)
        # Lorsqu'un mur est choisi, on le met à la fin du tableau pour ne
        # pas le rechoisir. Ce serait plus simple de le supprimer de la liste
        # mais plus couteux car la suppression est en O(n).
        modifications = 0
        while modifications < nombre_cellules - 1:
            indice_mur = rd.randrange(indice_premier_non_modifiable)
            mur_candidat = murs_modifiables[indice_mur]
            if self.modifier_mur(mur_candidat, zones_cellules):
                modifications += 1
            indice_premier_non_modifiable -= 1
            murs_modifiables[indice_mur], murs_modifiables[indice_premier_non_modifiable] = \
                murs_modifiables[indice_premier_non_modifiable], murs_modifiables[indice_mur]
 
    def fusionner_zones(zones_cellules, indice_cellule1, indice_cellule2):
       zone1 = zones_cellules[indice_cellule1]
       zone2 = zones_cellules[indice_cellule2]
       for i in range(len(zones_cellules)):
           if zones_cellules[i] == zone2:
               zones_cellules[i] = zone1       
 
    def modifier_mur(self, mur_candidat, zones_cellules):
        # Le mur sépare cellule1 et cellule2
        mur_vertical = (mur_candidat < self.largeur*self.hauteur-self.hauteur)
        if mur_vertical:
            ligne_cellule1 = mur_candidat//(self.largeur-1)
            colonne_cellule1 = mur_candidat%(self.largeur-1)
            indice_cellule1 = ligne_cellule1*self.largeur + colonne_cellule1
            indice_cellule2 = indice_cellule1 + 1
        else:
            ligne_cellule1 = (mur_candidat-(self.largeur*self.hauteur-self.hauteur))//self.largeur
            colonne_cellule1 = (mur_candidat-(self.largeur*self.hauteur-self.hauteur))%self.largeur
            indice_cellule1 = mur_candidat-(self.largeur*self.hauteur-self.hauteur)
            indice_cellule2 = indice_cellule1 + self.largeur
        if zones_cellules[indice_cellule1] != zones_cellules[indice_cellule2]:  
            Labyrinthe.fusionner_zones(zones_cellules, indice_cellule1, indice_cellule2)
            if mur_vertical:
                self.grille[ligne_cellule1][colonne_cellule1].mur_droit = False
            else:
                self.grille[ligne_cellule1][colonne_cellule1].mur_bas = False
            return True
        else:   # les deux cellules sont déjà dans la même zone, on ne supprime pas le mur
            return False


class GfxHMI(tk.Tk):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maze = Labyrinthe(largeur, hauteur)  
        tk.Tk.__init__(self)    
        self.canevas = tk.Canvas(self, height=self.hauteur*COTE_CASE+1, width=self.largeur*COTE_CASE+1,
                                  borderwidth=0, highlightthickness=0, bg='ivory')
        self.dessine_labyrinthe()
        self.porte = self.canevas.create_rectangle(2, 2, COTE_CASE-1, COTE_CASE-1, fill='brown')
        self.porte_ligne, self.porte_colonne = 0, 0
        self.tresor_ligne, self.tresor_colonne = hauteur-1, largeur-1
        self.tresor = self.canevas.create_oval((largeur-1)*COTE_CASE+2, (hauteur-1)*COTE_CASE+2, largeur*COTE_CASE-2, hauteur*COTE_CASE-2, fill='yellow')
        self.canevas.bind("<Button-1>", self.placement)
        self.canevas.pack(padx=5, pady=5, side=tk.TOP)
        tk.Button(self, text='Entrée', command=self.souris_entree).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text='Trésor', command=self.souris_tresor).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text='Solution', command=self.solution).pack(side=tk.RIGHT, padx=5, pady=5)
        self.placer_entree = True
        self.placer_tresor = False
        self.trace_du_chemin = None  # conserve la variable tracé pour pouvoir effacer le chemin
       
    def dessine_cellule(self, i, j, cellule):
        if cellule.mur_droit:
            self.canevas.create_line((j+1)*COTE_CASE, i*COTE_CASE+1, (j+1)*COTE_CASE, (i+1)*COTE_CASE+1)
        if cellule.mur_bas:
            self.canevas.create_line(j*COTE_CASE+1, (i+1)*COTE_CASE, (j+1)*COTE_CASE+1, (i+1)*COTE_CASE)
                
    def dessine_labyrinthe(self):
        self.canevas.create_line(0, self.hauteur*COTE_CASE, 0, 0, self.largeur*COTE_CASE, 0, fill='black')
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.dessine_cellule(i, j, self.maze.grille[i][j])
    
    def placement(self, event):
        colonne = event.x//COTE_CASE
        ligne = event.y//COTE_CASE
        if self.placer_entree:
            objet = self.porte
            self.porte_ligne = ligne
            self.porte_colonne = colonne
        else:
            objet = self.tresor
            self.tresor_ligne = ligne
            self.tresor_colonne = colonne
        self.canevas.coords(objet, colonne*COTE_CASE+2, ligne*COTE_CASE+2, (colonne+1)*COTE_CASE-2, (ligne+1)*COTE_CASE-2)
        
    def souris_entree(self):
        self.placer_entree = True
        self.placer_tresor = False
    
    def souris_tresor(self):
        self.placer_entree = False
        self.placer_tresor = True

    def tracer_chemin(self, depart_ligne, depart_colonne, chemin):
        x = depart_colonne*COTE_CASE + COTE_CASE//2
        y = depart_ligne*COTE_CASE + COTE_CASE//2
        coordonnees_chemin = [x, y]
        for direction in chemin:
            if direction == 'n':
                y -= COTE_CASE
            elif direction == 's':
                y += COTE_CASE
            elif direction == 'e':
                x += COTE_CASE
            else:
                x -= COTE_CASE   
            coordonnees_chemin.extend([x, y])
        self.canevas.delete(self.trace_du_chemin)
        self.trace_du_chemin = self.canevas.create_line(*coordonnees_chemin, fill='blue', width=2)
               
    
    def solution(self):
        chemin_solution = self.maze.solution(self.porte_ligne, self.porte_colonne, self.tresor_ligne, self.tresor_colonne)
        self.tracer_chemin(self.porte_ligne, self.porte_colonne, chemin_solution)
        


	class Affichage(tk.Tk):
		def __init__(self, labyrinthe):
			largeur = self.largeur = len(labyrinthe.grille[0])
			hauteur = self.hauteur = len(labyrinthe.grille)
			self.maze = labyrinthe
			tk.Tk.__init__(self)    
			self.canevas = tk.Canvas(self, height=self.hauteur*COTE_CASE+1, width=self.largeur*COTE_CASE+1,
									borderwidth=0, highlightthickness=0, bg='ivory')
			self.dessine_labyrinthe()
			self.porte = self.canevas.create_rectangle(2, 2, COTE_CASE-1, COTE_CASE-1, fill='brown')
			self.porte_ligne, self.porte_colonne = 0, 0
			self.tresor_ligne, self.tresor_colonne = hauteur-1, largeur-1
			self.tresor = self.canevas.create_oval((largeur-1)*COTE_CASE+2, (hauteur-1)*COTE_CASE+2, largeur*COTE_CASE-2, hauteur*COTE_CASE-2, fill='yellow')
			self.canevas.pack(padx=5, pady=5, side=tk.TOP)

		
		def dessine_cellule(self, i, j, cellule):
			if cellule.mur_droit:
				self.canevas.create_line((j+1)*COTE_CASE, i*COTE_CASE+1, (j+1)*COTE_CASE, (i+1)*COTE_CASE+1)
			if cellule.mur_bas:
				self.canevas.create_line(j*COTE_CASE+1, (i+1)*COTE_CASE, (j+1)*COTE_CASE+1, (i+1)*COTE_CASE)
					
		def dessine_labyrinthe(self):
			self.canevas.create_line(0, self.hauteur*COTE_CASE, 0, 0, self.largeur*COTE_CASE, 0, fill='black')
			for i in range(self.hauteur):
				for j in range(self.largeur):
					self.dessine_cellule(i, j, self.maze.grille[i][j])
    
        


	if __name__=='__main__':
		GfxHMI(20, 10).mainloop()        
 
```


___ 

## Exemples d'exécution :

<iframe src="https://trinket.io/embed/python/e25159be66?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<iframe src="https://trinket.io/embed/python/e27dfa9f4d?outputOnly=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>