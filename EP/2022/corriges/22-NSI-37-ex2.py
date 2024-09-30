# 2022 sujet 37 - ex2
urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = '' # même nom que la fonction ! et cette variable est inutile
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat #
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

# ATTENTION il y a une faute dans l'exemple proposé sur le sujet
election = depouille(urne)
print(urne,election)
print(vainqueur(election))