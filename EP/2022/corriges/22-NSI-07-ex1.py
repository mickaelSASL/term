# 2022 -sujet 7 - ex1
# Écrire une fonction conv_bin qui prend en paramètre un entier positif n
# et renvoie un couple (b,bit) où :
#b est une liste d'entiers correspondant à la représentation binaire de n;
#  bit correspond aux nombre de bits qui constituent b.
def conv_bin(n):
    liste_bit=[n%2] # initialisation permettant de traiter le cas où n=0
    n=n//2
    while n!=0:
        liste_bit.append(n%2)
        n=n//2
    liste_bit.reverse()
    return (liste_bit,len(liste_bit))

# tests : on peut utiliser la fonction bin pour les tests
n=9
print(n,conv_bin(n),bin(n))
n=0
print(n,conv_bin(n),bin(n))
n=16
print(n,conv_bin(n),bin(n))
n=164
print(n,conv_bin(n),bin(n))