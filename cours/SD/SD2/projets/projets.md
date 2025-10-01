# **Mini-Projet**

Ce premier mini-projet a pour but de consolider les connaissances autour de la programmation objet.
Il consiste à modéliser plusieurs classes qui vont être liées entre elles.

!!! note "Mini-projet"
    Chaque fonction doit être documentée.
    Le mini-projet se fait par 2.



## I. Réflexion
Vous devez choisir une thématique parmi celles proposées ci-dessous, puis définir les classes nécessaires.
**Chaque classe doit avoir au maximum 3 attributs principaux.**

Thématiques possibles :

### 1. L’école
- Classes possibles : `Eleve`, `Classe`, `Enseignant`.
- Exemple de méthodes : ajouter une note, calculer la moyenne d’un élève, moyenne générale d’une classe, changer la matière d’un enseignant.

### 2. Tournoi sportif
- Classes possibles : `Equipe`, `Match`, `Tournoi`.
- Exemple de méthodes : enregistrer le résultat d’un match, afficher les scores, calculer le classement.

### 3. Playlist musicale
- Classes possibles : `Chanson`, `Playlist`.
- Exemple de méthodes : ajouter/supprimer une chanson, calculer la durée totale de la playlist, trouver la chanson la plus longue.

### 4. Bibliothèque scolaire
- Classes possibles : `Livre`, `Utilisateur`, `Bibliotheque`.
- Exemple de méthodes : ajouter un livre, emprunter/rendre un livre, afficher les livres disponibles.

### 5. Pizzeria
- Classes possibles : `Pizza`, `Commande`, `Client`.
- Exemple de méthodes : ajouter une pizza à une commande, calculer le prix total, afficher la commande.


!!! note "Conseil"
Vous pouvez proposer d’autres contextes, mais validez-les d’abord avec l’enseignant.

## II. Schématisation
Dessinez un diagramme (suivant le modèle) permattant de visualiser :

les attributs de chaque classe,
leurs méthodes principales,
les associations entre classes (par exemple : une Classe contient plusieurs Eleve).

!!! warning "Important !"
    Le diagramme UML est une étape de réflexion indispensable.
    Il permet d’avoir une vision claire des interactions entre vos classes et de limiter les erreurs lors du codage.

Exemple (simplifié) pour Eleve :

``` mermaid
    classDiagram
        class Eleve{
            nom : str
            prenom : str
            notes : list[float]
            ajouter_note()
            moyenne()
            meilleure_note()
        }
```


## III. Répartition des tâches
Les classes ne sont pas longues à écrire.
Répartissez-les entre vous. Le regroupement pourra se faire lorsque les classes sont finies et testées.

## IV. Tests
Testez au fur et à mesure vos classes et méthodes.
Commencez par le constructeur et une méthode simple, puis ajoutez progressivement de nouvelles méthodes.

## V. Exemple (École)
Un élève peut être défini par les informations ci-dessous :

- Un attribut `nom` (string)
- Un attribut `prenom` (string)
- Un attribut `notes` (liste de nombres, initialisée vide)
- Une méthode `ajouter_note(self, x)` qui ajoute une note (entre 0 et 20) à la liste
- Une méthode `moyenne(self)` qui renvoie la moyenne des notes
- Une méthode `note_la_plus_basse(self)` qui renvoie la plus petite note
- Une méthode `note_la_plus_haute(self)` qui renvoie la meilleure note
- Une méthode `affichage(self)` qui affiche le nom, prénom et la moyenne


!!! danger "Définissez, documentez et testez vos classes."