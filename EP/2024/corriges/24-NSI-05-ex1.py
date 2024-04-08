print("\nNSI Partie Pratique - SUJET nº05\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")

def max_et_indice(tab:list)->tuple:
    max,indice = tab[0],0
    for i in range(len(tab)):
        if tab[i] > max: max,indice = tab[i],i
    return max,indice
#tests
print(f"max_et_indice([1,5,6,9,1,2,3,7,9,8]) --> {max_et_indice([1,5,6,9,1,2,3,7,9,8])}\nmax_et_indice([-2]) --> {max_et_indice([-2])}\nmax_et_indice([-1,-1,3,3,3]) --> {max_et_indice([-1,-1,3,3,3])}\nmax_et_indice([1,1,1,1]) --> {max_et_indice([1,1,1,1])}\n")


print("• Exo 2 -->") 

def est_un_ordre(tab:list)->bool:
    '''Renvoie True si tab est de longueur n et contient tous les entiers de 1 à n, False sinon '''
    n = len(tab)
    #les entiers vus lors du parcours
    vus = []
    for x in tab:
        if x < 1 or x > n or x in vus: 
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    #print('ATTENTION nb apres la premiere condition',nb)
    i = 0
    while i < n-1: 
        if ordre[i+1]-ordre[i] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

#tests
print(f'''est_un_ordre([1, 6, 2, 8, 3, 7]) --> {est_un_ordre([1, 6, 2, 8, 3, 7])}\nest_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]) --> {est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])}\n\nnombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]) --> {nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])}\nnombre_points_rupture([1, 2, 3, 4, 5]) --> {nombre_points_rupture([1, 2, 3, 4, 5])}\nnombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]) --> {nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])}\nnombre_points_rupture([2, 1, 3, 4]) --> {nombre_points_rupture([2, 1, 3, 4])} ''')
