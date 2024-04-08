# NSI Partie Pratique 2024 - SUJET 01

# EXERCICE 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}

def taille(arbre, lettre):
    fils_gauche = arbre[lettre][0]
    fils_droit  = arbre[lettre][1]

    if fils_gauche != '' and fils_droit != '':
        return 1 + taille(arbre, fils_gauche) + taille(arbre, fils_droit)

    if fils_gauche != '' and fils_droit == '':
        return 1 + taille(arbre, fils_gauche)

    if fils_gauche == '' and fils_droit != '':
        return 1 + taille(arbre, fils_droit)

    else:
        return 1

# test 
print(f"taille(a,'F') --> {taille(a,'F')} \ntaille(a,'B') --> {taille(a,'B')} \ntaille(a,'I') --> {taille(a,'I')}") #devrait rendre 9, 5, 2

# Une autre solution

def taille1(arbre:dict,lettre:str) -> int:
    """Renvoie la taille de l'arbre, soit le nombre total de noeuds restant à partir de ce noeud"""
    if arbre[lettre] == ['','']: #si le nœud est vide 
        return 1 
    else: # sinon 3 differentes situations --> 
        if arbre[lettre][1] == '': #le noeud de la droite est vide -> on retourne tout ce qui se retrouve à la gauche
            return 1 + taille1(arbre,arbre[lettre][0]) 
        elif arbre[lettre][0] == '':  #le noeud de la gauche est vide -> on retourne tout ce qui se retrouve à la droite
            return 1 + taille1(arbre,arbre[lettre][1]) 
        else : # les deux noeuds ne sont pas vides -> on retourne la somme recursive des deux nœuds 
            return 1 + taille1(arbre,arbre[lettre][0]) + taille1(arbre,arbre[lettre][1]) 
#test
print(f"taille1(a,'F') --> {taille1(a,'F')} \ntaille1(a,'B') --> {taille1(a,'B')} \ntaille1(a,'I') --> {taille1(a,'I')}\n\n• Exo 2 -->") #devrait rendre 9, 5, 2

