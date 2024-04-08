# NSI pratique 2024 sujet 18- ex1

#Programmer la fonction multiplication, prenant en paramÃ¨tres deux nombres entiers n1 et n2,
# et qui renvoie le produit de ces deux nombres.
# Les seules opÃ©rations autorisÃ©es sont lâ€™addition et la soustraction.

# solution 1 : avec la valeur absolue
def multiplication(n1, n2):
    '''
       In : n1, n2 int
       Out : n1 x n2
    '''
    produit=0
    # on se ramÃ¨ne d'abord au cas oÃ¹ n1 et n2 sont tous les deux positifs ou nÃ©gatifs :
    if n1>=0:
        for _ in range(n1):
            produit=produit+n2
    else:
        n1=-n1
        for _ in range(n1):
            produit=produit-n2
    return produit
            
# Une 2e solution
def multiplication2(n1, n2):
    # on se ramÃ¨ne d'abord au cas oÃ¹ n1 et n2 sont tous les deux positifs :
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)

    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat

# Une 3e solution
def multiplication3(n1,n2):
    ''' n1 et n2 sont des entiers
    renvoie le produit de n1 par n2
    '''
    resultat=0
    if n2>=0:
        for i in range(n2):
            resultat += n1
    else:
        n2=-n2
        for i in range(n2):
            resultat -= n1
    return resultat



#tests
for n1 in range(-3,4):
    for n2 in range (-3,4):
        print((n1, n2),multiplication(n1, n2),multiplication2(n1, n2),multiplication3(n1, n2))