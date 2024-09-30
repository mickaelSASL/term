# 2022 - sujet 16 - ex1
def maxi(tab):
    val_max = tab[0]
    pos_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            pos_max = i
    return (val_max, pos_max)


print(maxi([1,5,6,9,1,2,3,7,9,8]))