# 2022 -sujet 13 - ex1
def rendu(somme_a_rendre):
    pieces = [5, 2, 1]
    retour = [0, 0, 0]
    reste_a_rendre = somme_a_rendre
    for i in range(3):
        retour[i] = reste_a_rendre // pieces[i]
        reste_a_rendre = reste_a_rendre % pieces[i]
    return retour

somme_a_rendre=13
print(somme_a_rendre,rendu(somme_a_rendre))
somme_a_rendre=64
print(somme_a_rendre,rendu(somme_a_rendre))
somme_a_rendre=89
print(somme_a_rendre,rendu(somme_a_rendre))
somme_a_rendre=0
print(somme_a_rendre,rendu(somme_a_rendre))