# Epreuve pratique 2024 - NSI - Sujet 11


def nombre_de_mots(phrase):
    if phrase =='':
        return 0
    else:
        compteur = 1
        for char in phrase:
            if char == ' ':
                compteur+=1
            if char == '!' or char == '?' :
                compteur = compteur - 1
                break
            if char == '.':
                break
    return compteur


print(nombre_de_mots('Cet exercice est simple.'))

print(nombre_de_mots('Le point d exclamation est séparé !'))

print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))

print(nombre_de_mots('Fin.'))
                
            