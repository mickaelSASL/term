# Lemmings 🏃🏻🧍🚶🤸  

## Déroulement du jeu
### La méthode

`Jeu.demarrer` lance une boucle infinie, dont une issue passe par l’appui sur la touche ++q++ (« quitter ») du clavier. Le rythme du jeu est donné par une constante de classe `Jeu.PERIODE`. Le calcul des positions des lemmings, suivi de l’affichage du jeu a lieu chaque `Jeu.PERIODE` secondes.  
A chaque « tour », les lemmings font un mouvement (avancer, tomber ou se retourner), dans l’ordre de leur entrée dans le jeu. Lorsque l’un d’entre eux atteint la sortie, il quitte le jeu (on pourra par exemple à cette occasion incrémenter un attribut `score` du jeu)
Si l’utilisateur appui sur la touche ++plus++, un nouveau lemming rentre dans le jeu.


## A faire

Par groupe de deux ou trois, vous devez implémenter en python ce jeu.  
Aucun module n'est à installer pour développer ce projet.  
Les seuls modules autorisés sont ceux indiqués dans les consignes, améliorations et ressources plus éventuellement `math` et `random`.  

Cette base pourra être améliorée. Des pistes sont proposées [ici](améliorations.md).


## A rendre

Vous devrez rendre un dossier nommé `Lemmings_NOM` ou `NOM` est votre nom de famille, contenant:

* Un fichier `lemmings.py` avec le code du jeu,  
* Le ou les fichiers textes utilisés pour générer les niveaux,  
* Un fichier au format `.pdf` de **6 pages maximum** contenant un rapport avec :
    * La répartition des tâches dans le groupe.
    * Les difficultés rencontrées et les solutions proposées.
    * L'explication d'une partie de code que chacun aura plus spécifiquement travaillé. (Travail individuel)