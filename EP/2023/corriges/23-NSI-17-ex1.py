# 2023 sujet 17 - ex1

def moyenne(liste_notes):
    somme_notes = 0
    somme_coeffs = 0
    for devoir in liste_notes:
        note = devoir[0]
        coeff = devoir[1]
        somme_notes += note * coeff
        somme_coeffs += coeff
    return somme_notes / somme_coeffs

#tests

print(moyenne([(15,2),(9,1),(12,3)]))