# **Epreuves Pratiques**
## SUJET 6 - Corrigé

**Exercice 1**

```Python
def rendu(somme_a_rendre):
    nbr=[0,0,0]
    m = [5,2,1]
    for i in range(len(m)):
        while somme_a_rendre>=m[i]:
            somme_a_rendre=somme_a_rendre-m[i]
            nbr[i]=nbr[i]+1
    return nbr
```

**Exercice 2**

```Python
class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None 


F = File()
F.est_vide()
F.enfile(2)
F.affiche()
F.est_vide()
F.enfile(5)
F.enfile(7)
F.affiche()
F.defile()
F.defile()
F.affiche()

```
