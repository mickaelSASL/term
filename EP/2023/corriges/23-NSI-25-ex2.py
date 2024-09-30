# 2023 sujet 25 - ex2



class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
    un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

# tests
a = Arbre(5)
insere(a, 2)
insere(a, 7)
insere(a, 3)
print(parcours(a, []))
#[2, 3, 5, 7]
insere(a, 1)
insere(a, 4)
insere(a, 6)
insere(a, 8)
print(parcours(a, []))
#[1, 2, 3, 4, 5, 6, 7, 8]
