# 2023 sujet 19 - ex2

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c  <= 'Z':
            # La relation d'ordre utilise le code ASCII
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

# tests
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))

print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))