# **P2: Jeu de cartes : la Bataille 🃏♣️♠♥♦ **  
<center>![](main_cartes.png)</center>

A l'aide aux classes du fichier `classes.py`, créer un jeu de bataille.  
La méthode `getNbCartes`de la classe `Joueur` est à implémenter.

> Rappel des règles : [Wikipédia](https://fr.wikipedia.org/wiki/Bataille_(jeu))


## Méthode `getNbCartes`de la classe `Joueur`

```Python
def getNbCartes(self):
    return len(self.main)
```


## Programme `Bataille`

```Python
from classes import *

def bataille(J1, J2,gain=[]):
    """
    Fonction permettant de faire un tour de jeu
    
    Parameters
    ----------
    J1 : joueur
        joueur n°1.
    J2 : joueur
        joueur n°2.
    gain : list, optional
        liste de cartes à gagner en suspend en cas de bataille. 
        la valeur par défaut est [].

    Returns
    -------
    None.

    """
    # Si un des 2 joueurs ne peut plus le jeu s'arrête
    if not(J1.peut_jouer and J2.peut_jouer):
        return 0
    
    # Tirage d'une carte pour chaque joueur
    c1 = J1.jouer()
    c2 = J2.jouer()
    print(J1.getNom(), ":", c1.get_carte(), "  |  ", J2.getNom(), ":", c2.get_carte())
    gain.extend([c1, c2]) # les 2 cartes sont ajoutées dans la liste de cartes à gagner

    # Le joueur 1 gagne le tour
    if c1.get_valeur() > c2.get_valeur():
        J1.ramasser(gain)
        gain.clear()
        print(J1.getNom(), "gagne")
        return 1+bataille(J1, J2)

    # Le joueur 2 gagne le tour
    elif c1.get_valeur() < c2.get_valeur():
        J2.ramasser(gain)
        gain.clear()
        print(J2.getNom(), "gagne")
        return 1+bataille(J1, J2)
    
    else:
        print("Bataille : ", [carte.get_carte() for carte in gain])
        gain.extend([J1.jouer(), J2.jouer()])
        return bataille(J1, J2, gain)
    

def main():
    
    # Instanciation des objets
    jeu = JeuDeCartes()                
    J1 = Joueur("moi")
    J2 = Joueur("toi")

    # Distribution des cartes
    jeu.melanger()
    J1.ramasser(jeu.distribuer(26))
    J2.ramasser(jeu.distribuer(26))
    
    # Lancement du jeu
    nb_tours = bataille(J1, J2)

    # Message de fin en cas de victoire
    if J1.peut_jouer:
        print(J1.getNom(), "a gagné")
        print(J2.getNom(), "a perdu")
    else:
        print(J2.getNom(), "a gagné")
        print(J1.getNom(), "a perdu")

    print("en", nb_tours, "coups")


if __name__ == '__main__':
    main()
```