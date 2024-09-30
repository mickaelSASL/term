# 2022 -sujet 10 - ex1
# Écrire une fonction occurence_lettres avec prenant comme paramètre une variable phrase de type str.
#Cette fonction doit renvoyer un dictionnaire de type constitué des occurrences des caractères présents dans la phrase.
def occurrence_lettres(phrase):
    occ = {}
    for caractere in phrase:
        if caractere in occ:
            occ[caractere] += 1
        else:
            occ[caractere] = 1
    return occ

phrase='hello'
print(phrase,occurrence_lettres(phrase))

phrase='Hello world !'
print(phrase,occurrence_lettres(phrase))