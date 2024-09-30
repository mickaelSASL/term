#2022 - sujet 28 - ex2
def dec_to_bin(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

#on peut utiliser la fonction bin pour les tests

a=0
print(a,dec_to_bin(a),bin(a))

a=83
print(a,dec_to_bin(a),bin(a))

a=127
print(a,dec_to_bin(a),bin(a))