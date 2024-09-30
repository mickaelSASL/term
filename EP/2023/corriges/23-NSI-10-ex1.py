# 2023 sujet 10 - ex1


def maxliste(tab):
    maximum = tab[0]
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

# test
tab=[98, 12, 104, 23, 131, 9]
print(tab,maxliste(tab))
print('-------------------')
tab=[-27, 24, -3, 15]
print(tab,maxliste(tab))
print('-------------------')
tab=[980, 12, 104, 23, 131, 9]
print(tab,maxliste(tab))
print('-------------------')
tab=[98, 12, 104, 23, 131, 900]
print(tab,maxliste(tab))
print('-------------------')