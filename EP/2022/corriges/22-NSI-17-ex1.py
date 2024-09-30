# 2022 - sujet 17 - ex1def nombre_de_mots(phrase):
def nombre_de_mots(phrase):
    nb_mots = 0
    for caractere in phrase:
        if caractere == ' ' or caractere == '.':
            nb_mots += 1
    return nb_mots

print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Il y a un seul espace entre les mots !'))