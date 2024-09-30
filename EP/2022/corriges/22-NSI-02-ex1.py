# 2022 Sujet 2 ex 1
def moyenne(tab):
    somme_notes = 0
    somme_coeffs = 0
    for devoir in tab:
        note = devoir[0]
        coeff = devoir[1]
        somme_notes += note * coeff
        somme_coeffs += coeff
    return somme_notes / somme_coeffs

print(moyenne([(15,2),(9,1),(12,3)]))