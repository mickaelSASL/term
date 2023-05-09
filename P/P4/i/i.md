# **P4: Résolution de labyrinthe par les graphes**  
<img src="./labyrinthe/menu_donnees_base.jpg" alt="donnees">

## Projet  : Créer, représenter et résoudre des labyrinthes
Le but du TP est de créer, représenter et résoudre des labyrinthes. Les labyrinthes peuvent être vus comme des graphes.

## Propriétes des labyrinthes
Nous nous intéresserons seulement à des labyrinthes rectangulaires composés de n lignes et m colonnes sur une grille régulière composée de n×m cellules. Chaque cellules comportant 4 côtés dont chacun peut être ouvert ou fermé (présence d'un mur).

<img src="./labyrinthe/labyrinthe_1.png" alt="labyrinthe">
<figcaption>grille vide avec murs extérieurs</figcaption>


* Deux cellules sont consécutives si elles partagent un côté.
* Un chemin dans un labyrinthe est une suite finie de n cellules où chacune est consécutive avec sa suivante.
* Un labyrinthe est dit parfait s'il existe un et un seul chemin connectant 2 cellules.

<img src="./labyrinthe/labyrinthe_2.png" alt="labyrinthe">
<img src="./labyrinthe/labyrinthe_3.png" alt="labyrinthe">
<img src="./labyrinthe/labyrinthe_4.png" alt="labyrinthe">

<figcaption>Chemin  ..................... plusieurs chemins .................................... parfait </figcaption>


</blockquote>


<div class="exercice">
	<h4>Entrainement 1 :</h4>
		<p>Montrer que pour un labyrinthe rectangulaire de n lignes et m colonnes le nombre maximal de murs internes fermés est : 2 n m - n - m</p>
</div>




<p>
	La création d'un labyrinthe suit les étapes suivantes: 
</p>
<ul>
	<li>Générer un graphe G représentant une grille de taille m*n</li>
	<li>Construire un <b>arbre couvrant</b> A de ce graphe</li>
	<li>Dessiner le labyrinthe en traçant un mur entre les sommets directement liés dans G et non dans A</li>
</ul>



<h4>Générer une grille de taille m * n</h4>
<p>
	Un labyrinthe, composé de longueur × largeur cases numérotées par des couples (i, j), est représenté par un graphe (non orienté) dont les sommets sont étiquetés par des couples (i, j). Lorsqu’une case (i0, j0) communique avec une autre case voisine (i1, j1), alors il existe une arête entre les sommets (i0, j0) et (i1, j1) du graphe. Deux cases (ou sommets) sont particuliers, ce sont l’entrée (0,0) et la sortie du labyrinthe.<br>
	Soit le labyrinthe suivant :
</p>


<h5>Présentation de la structure de données représentant la géométrie d'un labyrinthe</h5>
		<p>
			Le labyrinthe de taille 4x4 suivant :
		</p>
		<div class="centrer">
			<img src="./labyrinthe/labyrinthe_5.png" width="250">
		</div>