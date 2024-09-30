# 2023 sujet 40 - ex1

def nombre_de_mots(phrase):
    nb_mots = 0
    for caractere in phrase:
        if caractere == ' ' or caractere == '.':
            nb_mots += 1
    return nb_mots
 
 
# Les Tests
phrase = 'Le point d exclamation est separe !'
print(phrase,nombre_de_mots(phrase))
print('-------------')
phrase = ''
print(phrase,nombre_de_mots(phrase))
print('-------------')
phrase = 'Il y a un seul espace entre les mots !'
print(phrase,nombre_de_mots(phrase))
print('-------------')
phrase = 'Combien de mots y a t il dans cette phrase ?'
print(phrase,nombre_de_mots(phrase))
print('-------------')
phrase = 'Fin.'
print(phrase,nombre_de_mots(phrase))
print('-------------')