# 2023 sujet 14 - ex1

def recherche(elt, tab):
    '''
    renvoie l’indice de la première occurrence de
    elt dans tab si elt est dans tab et -1 sinon. 
    '''
    assert tab != [], "le tableau est vide"
    for i in range(len(tab)):
        if tab[i] == elt:
            return i        
    return -1         

# tests
(elt, tab)=(1, [2, 3, 4])
print((elt, tab),recherche(elt, tab))
print('---------------------')

(elt, tab)=(1, [2, 3, 4])
print((elt, tab),recherche(elt, tab))
print('---------------------')

(elt, tab)=(50, [1, 50, 1])
print((elt, tab),recherche(elt, tab))
print('---------------------')

(elt, tab)=(15, [8, 9, 10, 15])
print((elt, tab),recherche(elt, tab))
print('---------------------')