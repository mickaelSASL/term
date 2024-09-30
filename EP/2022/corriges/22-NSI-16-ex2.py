# 2022 - sujet 16 - ex2
def positif(T):
    T2 = list(T) # on peut aussi utiliser la fonction copy afin de ne pas modifier T
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = [] # <- NB : cette ligne est inutile
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2


print(positif([-1,0,5,-3,4,-6,10,9,-8 ]))