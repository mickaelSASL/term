# 2024 NSI sujet 48 - ex 2

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui represente par s
    en appliquant le procede de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(str(s))): 
        if s[i] == chiffre:
            compte += 1 
        else:
            resultat += str(compte) + str(chiffre)
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + str(chiffre) 
    resultat += lecture_chiffre
    return resultat

print(nombre_suivant('1211'))#'111221'
print(nombre_suivant('311'))#'1321'