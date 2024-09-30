# 2022 -sujet 15 - ex2
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

# pour les tests on peut utiliseeer la fonctions bin
a=0
print(a,binaire(a),bin(a))

a=77
print(a,binaire(a),bin(a))

a=10
print(a,binaire(a),bin(a))