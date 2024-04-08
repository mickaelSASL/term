# 2024 NSI sujet 41 - ex 1

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def taille(arbre):
    if arbre is None:
        return 0
    return 1 + taille(arbre.gauche) + taille(arbre.droit)

def hauteur(arbre):
    if arbre is None:
        return -1
    return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))

print(hauteur(a))#2
print(taille(a)) #4
print(hauteur(None)) #-1
print(taille(None)) #0
print(hauteur(Noeud(1, None, None))) #0
print(taille(Noeud(1, None, None))) #1
    