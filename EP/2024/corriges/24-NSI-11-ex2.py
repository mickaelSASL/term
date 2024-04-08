# Epreuve pratique 2024 - NSI - Sujet 11 - Exercice 2


# Exercice 2

class Noeud:
    def __init__(self, etiquette):
        '''MÃ©thode constructeur pour la classe Noeud.
        CrÃ©e une feuille d'Ã©tiquette donnÃ©e.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''InsÃ¨re la clÃ© dans l'arbre binaire de recherche
            en prÃ©servant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

# test Exercice 2
print('---------------')
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.etiquette)

print(arbre.droit.etiquette)

print(arbre.gauche.gauche.etiquette)

print(arbre.gauche.droit.etiquette)
