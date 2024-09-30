# 2022 -sujet 11 - ex2
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4))

print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5))