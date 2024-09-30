# 2023 sujet 29 - ex1

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None


def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.fg) + taille(a.fd)

def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))

# tests
a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)
print(hauteur(a))
print(taille(a)) 