# 2022 -sujet 10 - ex2
# La fonction fusion prend deux listes L1,L2 d’entiers triées par ordre croissant et les fusionne en une liste triée L12 qu’elle renvoie.
def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        # i1 est l'indice de parcours de L1 (de longueur n1) i2 est l'indice de parcours de L2 (de longueur n2)
        if L1[i1] < L2[i2]:
            #On se trouve dans le cas où le plus petit élément se trouve dans L1, c'est donc lui qui est ajouté à liste fusionnée L12.
            L12[i] = L1[i1]
            i1 = i1 + 1
        else:
            L12[i] = L2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        # On a atteint la fin de l'une des listes, il reste donc à ajouter les éléments restants de l'autre liste. 
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i + 1
    return L12

(L1,L2)=([-10,0,10,20,30,40],[-2,-1,0,5,10,20,25,27,50])
print(fusion(L1,L2))

print(fusion([1,6,10],[0,7,8,9]))
 