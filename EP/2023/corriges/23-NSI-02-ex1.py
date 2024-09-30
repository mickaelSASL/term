# 2023 sujet 2 - ex1

def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)

# Les Tests
tab=[1, 5, 6, 9, 1, 2, 3, 7, 9, 8]
print(tab,indices_maxi(tab))

tab=[7]
print(tab,indices_maxi(tab))

 