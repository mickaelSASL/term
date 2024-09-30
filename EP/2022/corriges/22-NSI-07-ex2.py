# 2022 -sujet 7 - ex2
# La fonction tri_bulles prend en paramètre une liste T d’entiers non triés
# et renvoie la liste triée par ordre croissant.
def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        # On parcourt la liste à l'envers à l'aide de l'indice i
        # (le dernier élément de T a pour indice len(T)-1)
        for j in range(i):
            if T[j] > T[j+1]: # Dans ce cas on échange les éléments
                # en utilisant ici un variable tampon : temp
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


# tests :
T=[5,10,0,-50,15,3,780]
print(tri_bulles(T))

T=[500,100,0,-50,15,3,-780]
print(tri_bulles(T))