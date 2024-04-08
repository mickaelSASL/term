# NSI pratique 2024 sujet 15 - ex2

def binaire(a):
    bin_a = str(a%2) # pour gErer le cas a=0
    a = a // 2
    while a >0 :
        bin_a = str(a%2) + bin_a
         # attention a  l'ordre de concatenation
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