print("\nNSI Partie Pratique - SUJET nº04\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")
def gb_vers_entier(tab:list)->int:
    decimal = 0
    for i in range(len(tab)):
        if tab[i] == True: decimal += 2**(len(tab)-1-i)
    return decimal    
def gb_vers_entier1(tab:list)->int:
    return sum([2**(len(tab)-1-i) for i in range(len(tab)) if tab[i] == True])      

#tests
print(f'''gb_vers_entier([]) --> {gb_vers_entier([])}
gb_vers_entier([True]) --> {gb_vers_entier([True])}
gb_vers_entier([True, False, True,False, False, True, True]) --> {gb_vers_entier([True, False, True,False, False, True, True])}
gb_vers_entier([True, False, False, False,False, False, True, False]) --> {gb_vers_entier([True, False, False, False,False, False, True, False])}
''')
print(f'''
gb_vers_entier1([]) --> {gb_vers_entier1([])}
gb_vers_entier1([True]) --> {gb_vers_entier1([True])}
gb_vers_entier1([True, False, True,False, False, True, True]) --> {gb_vers_entier1([True, False, True,False, False, True, True])}
gb_vers_entier1([True, False, False, False,False, False, True, False]) --> {gb_vers_entier1([True, False, False, False,False, False, True, False])}
''')

print("• Exo 2 -->") 
def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer
        # où placer la valeur à ranger
        j = i
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion

        

#tests
tab = [98,12,104,23,131,9]
print(tab, " -->tri -->", end=" ")
tri_insertion(tab)
print(tab)
