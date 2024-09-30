# 2022 -sujet 8 - ex1
# Écrire une fonction recherche qui prend en paramètres elt un nombre entier et tab un tableau de nombres entiers,
# et qui renvoie l’indice de la première occurrence de elt dans tab si elt est dans tab et -1 sinon.
def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i        
    return -1     

(elt, tab)=(2, [-10,2,-20,4,50,20,3,-3])
print(recherche(elt, tab))
(elt, tab)=(-3, [-10,2,-20,4,50,20,3,-3])
print(recherche(elt, tab))
(elt, tab)=(-10, [-10,2,-20,4,50,20,3,-3])
print(recherche(elt, tab))
(elt, tab)=(200, [-10,2,-20,4,50,20,3,-3])
print(recherche(elt, tab))