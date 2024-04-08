# 2024 NSI sujet 38 - ex 1

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

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])) #(9, [3, 8])
print(indices_maxi([7])) #(7, [0])