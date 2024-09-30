# 2022 sujet 34 - ex2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Il y a une faute de frappe dans la variable alphabet de l'énoncé
# (une virgule en trop dans la valeur 'o,')

def occurrence_max(ch):
    occurrence = [0]*26
    for caractere in ch:
        if caractere in alphabet:
            index_caractere = alphabet.index(caractere)
            occurrence[index_caractere] += 1
    indice_max_occurence = 0
    max_occurence = occurrence[0]
    for i in range(0,len(occurrence)):
        if occurrence[i]>max_occurence:
            max_occurence = occurrence[i]
            indice_max_occurence = i 
    return alphabet[indice_max_occurence]

ch='je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
print(occurrence_max(ch))