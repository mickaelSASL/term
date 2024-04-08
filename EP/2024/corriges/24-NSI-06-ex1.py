print("\nNSI Partie Pratique - SUJET nº04\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")

def verifie(tab:list)->bool:
    for i in range(len(tab)-1):
        if tab[i]>tab[i+1]:
            return False
    return True
#tests
print(f'''verifie([0, 5, 8, 8, 9]) --> {verifie([0, 5, 8, 8, 9])}
verifie([8, 12, 4]) --> {verifie([8, 12, 4])}
verifie([-1,4]) --> {verifie([-1,4])}
verifie([]) --> {verifie([])}
verifie([5]) --> {verifie([5])}
''')

print("• Exo 2 --> ") 

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat
def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre
    ↪ de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]

    liste_finale = [ nom for nom in election if election[nom] == nmax]
    return liste_finale

#tests
election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])
print("depouille([ 'A', 'B', 'A' ]) -->",depouille([ 'A', 'B', 'A' ]))
print("depouille([]) -->",depouille([]))
print("election -->",election)
print("vainqueurs(election) -->",vainqueurs(election))
print("vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) -->",vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}))