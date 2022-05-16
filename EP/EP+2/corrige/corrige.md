# **Epreuves Pratiques**
## SUJET 2+ - Corrigé

**Exercice 1**
```Python

def partager(montants):
    assert len(montants) > 0, "tableau vide"    # On vérifie que le tableau ne soit pas vide

    total = 0       # Initialisation à 0
    for prix in montants.values():  # Parcours des valeurs du dictionnaire
        total += prix               
    moyenne = total/len(montants)   # Calcul de la moyenne
    moyene_arr = round(moyenne,2)   # Arrondi de la moyenne
    return total, moyene_arr        # Renvoie le total et la moyenne arrondie


# TESTS avec des différents groupes
# Groupe 1
groupe = {"Henry": 12,
          "Thierry": 15,
          "Samir": 20,
          "Sylvain": 13}

assert partager(groupe) == (60, 15.0)

# Groupe 2
groupe = {"Henry": 12,
          "Thierry": 15,
          "Samir": 20}

assert partager(groupe) == (47, 15.67)

# Groupe 3
groupe = {"Henry": 12,
          "Thierry": 15,
          "Samir": 20,
          "Sophie": 14.5}

assert partager(groupe) == (61.5, 15.38)

# Groupe vide
partager({})
```


**Exercice 2**
```Python
class Noeud:
    def __init__(self, mot, gauche=None, droite=None):
        self.gauche = gauche
        self.droite = droite
        self.mot = mot

def inserer(arbre_binaire, mot):
    '''Insère un élément dans l'arbre binaire de recherche.'''
    if arbre_binaire is None :
        arbre_binaire = Noeud(mot)
    elif mot < arbre_binaire.mot :
        arbre_binaire.gauche = inserer(arbre_binaire.gauche,mot)
    elif  mot > arbre_binaire.mot :
        arbre_binaire.droite = inserer(arbre_binaire.droite,mot)
    return arbre_binaire

def afficher(arbre_binaire):
    '''Affiche les mots par ordre alphabétique.'''
    if arbre_binaire is not None :
        afficher(arbre_binaire.gauche)
        print(arbre_binaire.mot)
        afficher(arbre_binaire.droite)

arbre = None
arbre = inserer(arbre, "kiwi")
arbre = inserer(arbre, "pomme")
arbre = inserer(arbre, "abricot")
arbre = inserer(arbre, "mangue")
arbre = inserer(arbre, "poire")
afficher(arbre)

```