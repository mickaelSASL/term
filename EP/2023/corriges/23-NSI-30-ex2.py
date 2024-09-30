# 2023 sujet 30 - ex2 - fd 

#On considère la fonction binaire ci-dessous qui prend en paramètre un entier positif a
#en écriture décimale. Cette fonction renvoie l’écriture binaire de a sous la forme d'une
#chaîne de caractères.
#L’algorithme utilise la méthode des divisions euclidiennes successives comme l’illustre
#l’exemple ci-après.

def binaire(a):
    bin_a = str(a%2) # pour gérer le cas a=0
    a = a // 2
    while a >0 :
        bin_a = str(a%2) + bin_a
         # attention à l'ordre de concaténation
        a = a//2
    return bin_a

# Les Tests
a=0
print('Avec a=',a,' On a :', binaire(a))

a=10
print('Avec a=',a,' On a :', binaire(a))

a=83
print('Avec a=',a,' On a :', binaire(a))

a=127
print('Avec a=',a,' On a :', binaire(a))