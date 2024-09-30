# 2023 sujet 33 - ex2

def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]
 

# Les Tests
tab=[41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
print(tab)