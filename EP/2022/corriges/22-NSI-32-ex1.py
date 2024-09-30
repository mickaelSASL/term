# 2022 sujet 32 - ex1

# Écrire une fonction recherche qui prend en paramètres elt un nombre
#et tab un tableau de nombres, et qui renvoie l’indice de la dernière
# occurrence de elt dans tab si elt est dans tab et le -1 sinon.

def recherche(elt, tab):
    n=len(tab)
    for i in range(n):
        if tab[n-i-1] == elt:
  # on parcourt la liste à l'envers pour avoir la première occurrence
            return n-i-1
    return -1

# autre solution
def recherche2(elt,tab):
    for i in range(len(tab)-1,-1,-1):
        if elt==tab[i]:
            return i
    return -1



(elt, tab)=(1,[2,3,4])
print((elt, tab),recherche(elt, tab),recherche2(elt, tab))

(elt, tab)=(1,[10,12,1,56])
print((elt, tab),recherche(elt, tab),recherche2(elt, tab))

(elt, tab)=(1,[1,50,1])
print((elt, tab),recherche(elt, tab),recherche2(elt, tab))

(elt, tab)=(1,[8,1,10,1,7,1,8])
print((elt, tab),recherche(elt, tab),recherche2(elt, tab))