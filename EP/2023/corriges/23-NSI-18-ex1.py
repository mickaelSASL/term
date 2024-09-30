# 2023 sujet 18 - ex1

def max_et_indice(tab):
    '''
    renvoie la valeur du plus grand élément de cette liste ainsi
    que l’indice de sa première apparition dans cette liste.
    '''
    assert tab != [], 'le tableau est vide'

    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

# Tests
tab=[1, 5, 6, 9, 1, 2, 3, 7, 9, 8]
print(tab,max_et_indice(tab))
print('------------------------')
tab=[-2]
print(tab,max_et_indice(tab))
print('------------------------')
tab=[-1, -1, 3, 3, 3]
print(tab,max_et_indice(tab))
print('------------------------')
tab=[1, 1, 1, 1]
print(tab,max_et_indice(tab))
print('------------------------')