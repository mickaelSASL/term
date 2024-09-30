# 2023 sujet 24 - ex1

def nbr_occurrences(chaine):
    nb_occ = {}
    for caractere in chaine:
        if caractere in nb_occ:
            nb_occ[caractere] += 1
        else:
            nb_occ[caractere] = 1
    return nb_occ

# tests
chaine='Hello world !'
print(chaine,nbr_occurrences(chaine))