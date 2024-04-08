# 2024 NSI sujet 34 - ex 1

def nbr_occurrences(chaine):
    nb_occ = {}
    for caractere in chaine:
        if caractere in nb_occ:
            nb_occ[caractere] += 1
        else:
            nb_occ[caractere] = 1
    return nb_occ

print(nbr_occurrences('bonjour'))
print(nbr_occurrences('Bébé'))
print(nbr_occurrences('Hello World !'))
