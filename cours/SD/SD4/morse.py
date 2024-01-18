from binarytree import build

def get_valeur(lettre):
      if lettre in MORSE_CODE_DICT.keys():
            return MORSE_CODE_DICT[lettre]


def get_lettre(val):
    for key, value in MORSE_CODE_DICT.items():
         if val == value:
             return key

def decode(code):
      monarbre = arbre
      for symbole in code:
            if symbole == '.':
                  monarbre = monarbre.left
            elif symbole == '-':
                  monarbre = monarbre.right
      return get_lettre(monarbre.values[0])

MORSE_CODE_DICT = { 'A':10, 'B':15,
                    'C':19, 'D':16, 'E':7,
                    'F':5, 'G':24, 'H':1,
                    'I':4, 'J':13, 'K':20,
                    'L':8, 'M':26, 'N':18,
                    'O':27, 'P':11, 'Q':25,
                    'R':9, 'S':2, 'T':22,
                    'U':6, 'V':3, 'W':12,
                    'X':16, 'Y':21, 'Z':23, '.':14}

arbre_lettres = ['.', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', None, 'L', None, 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', None, None]
arbre_valeurs = []

for c in arbre_lettres :
      arbre_valeurs.append(MORSE_CODE_DICT[c]) if c in MORSE_CODE_DICT.keys() else arbre_valeurs.append(None)

arbre = build(arbre_valeurs) 

def message_decode(message):
      liste = message.split()
      message_decode = ""

      for l in liste:
            message_decode = message_decode + decode(l)
      return message_decode


message_code = '-.-. . -- . ... ... .- --. . ...- --- ..- ... -- --- -. - .-. . --.- ..- . -.-. .- -- .- .-. -.-. .... .'
print(message_decode(message_code))