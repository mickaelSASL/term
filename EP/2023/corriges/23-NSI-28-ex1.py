# 2023 sujet 28 - ex1 -fd

#Ecrire une fonction qui prend en paramètre un tableau d'entiers non vide et qui renvoie la
#moyenne de ces entiers. La fonction est spécifiée ci-après et doit passer les assertions
#fournies.

def moyenne(tableau):
    '''
    moyenne(tableau) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    '''
    somme=0
    for element in tableau:
        somme=somme+element
    return somme/len(tableau)
    
    
     
 
assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5