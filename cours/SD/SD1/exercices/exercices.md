
===! "❓ Questions"
    ``` title="✒️ Exercice"
    1.	A partir de l’exemple du type Date (partie A.3), Ecrire une méthode qui modifie la date et la met au lendemain.

    2.	Ecrire l’implémentation en python d’une méthode `moyenne()` faisant partie de l’interface du type List.

    3.	Proposer deux implémentations de la méthode `longueur()` qui renvoie la taille d’une variable de type List. 

    4.	Représenter graphiquement le type de données, appelé Pile, défini comme ceci : (nous l’étudierons davantage plus tard).

    * Données : 
    Liste dans laquelle les ajouts et suppressions n’ont lieu que sur une même extrémité appelée sommet de pile : le dernier élément entré est le premier sorti.
    * Opérations :
    `pileVide()` : retourne un booléen indiquant si la pile est vide.
    `valeurSommet()` : retourne la valeur située au sommet de la pile (sans la supprimer).
    `empiler(valeur)` : ajoute la valeur donnée en paramètre au sommet de la pile.
    `depiler()`: retourne la valeur située au sommet de la pile et la supprime.
    ```
    
=== "🧩 Corrigé Q1"
    ```python
    def demain(ma_date):    
        setJour(getJour(ma_date)+1)
    ```

=== "🧩 Corrigé Q2"
    ```python
    def moyenne(ma_liste):    
        total = 0
        for i in ma_liste:
            total = total + i
        return total / len(ma_liste)
    ```

=== "🧩 Corrigé Q3"
    ### a. avec la méthode len()

    ```python
    def longueur(ma_liste):    
        return len(ma_liste)
    ```

    ### b. sans la méthode len()

    ```python
    def longueur(ma_liste):
        ct = 0    
        while ma_liste != []:
            ma_liste.pop()
            ct += 1
        return ct
    ```

=== "🧩 Corrigé Q4"
    ![](pile crêpes.png)
    ![](pile_graph.png)
