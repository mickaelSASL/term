# 2023 sujet 5 - ex1 FD


from random import randint

def lancer(n):
    '''In : n int
      Out : liste de n entiers obtenus aléatoirement entre 1 et 6 (1 et 6 inclus)
      '''
    return [randint(1,6) for _ in range (6)]

def paire_6(tab):
    '''In : tab, un tableau de type list de n entiers entre 1 et
            6 obtenus aléatoirement
      Out : un booléen égal à True si le nombre de 6
            est supérieur ou égal à 2, False sinon.
    '''
    compteur_de_6 =0
    for element in tab:
        if element==6:
            compteur_de_6+=1
    return compteur_de_6>=2
    

# Les Tests
lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
print('----------------------------') 
lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))
print('----------------------------')  
lancer3  = lancer(3)
print(lancer3)
print(paire_6(lancer3))
print('----------------------------') 
lancer4  = lancer(0)
print(lancer4)
print(paire_6(lancer4))
print('----------------------------') 