# 2022 - sujet 6 - ex1
# Écrire une fonction maxi qui prend en paramètre une liste tab de nombres entiers
#et qui renvoie un couple donnant le plus grand élément de cette liste
# ainsi que l’indice de la première apparition de ce maximum dans la liste.
def maxi(tab):
    if tab==[]: return None,None
    indice_maxi,maxi = 0, tab[0]
    for indice in range(1,len(tab)):
        if tab[indice]>maxi:
            indice_maxi,maxi = indice,tab[indice]
    return (maxi,indice_maxi)

print(maxi([1,5,6,9,1,2,3,7,9,8]))
