# -*- coding: utf-8 -*-

def recherche_naif(m, t):
    nb_trouve = 0
    long_txt = len(m)
    long_cle = len(t)
    
    for position in range(0, long_txt - long_cle + 1):
        if t == m[position : position + long_cle]:
            nb_trouve = nb_trouve + 1
            
    return nb_trouve

def pretraitement(cle):
    dico = {}
    long_cle = len(cle)
    
    for position in range(0, long_cle-1): # On ne traite pas le dernier caractère
        dico[cle[position]] = long_cle - position - 1
    print(dico)
    return dico

def boyer_moore(m, t):
    """
    Recherche textuelle selon l'algorithme de Boyer-Moore,
    version simplifiée de Horspool
    
    PARAMETRES
    m : Chaine de caractère, motif recherché (clé)
    t : Chaine de caractère, texte exploré
    
    RETURN
    Liste des positions de départ des occurences trouvées
    """
    
    decalages = pretraitement(m) # Dictionnaire de décalage de la clé
    
    positions = []      # positions de départ des occurences trouvées
    long_txt = len(t)   # longueur du texte exploré
    long_cle = len(m)   # longueur de la clé
    position = 0        # position de début de la clé dans le texte

    # Tant que la recherche n'est pas à la fin du texte :
    #
    # ABCDEFGH
    #      CLE
    #      ↑
    #
    # Ici la clé est en dernière position : position = long_txt-long_cle -1
    
    while (position <= long_txt-long_cle):     
        # Pour chaque caractère de la clé (de la fin au début)
        for i in range(long_cle-1, -1, -1):
            
            trouve = True   # trouve indique qu'une occurence est trouvée
            
            # Si le caractère de la clé (le dernier) est différent
            # du caractère du texte à la position (position + i)
            # ABCDEFGH
            #    CLE
            #      ↑
            #   position + 2
 
            if t[position+i] != m[i]:
                # Alors on vérifie si ce caractères est présent dans le dictionnaire
                if t[position +  i] in decalages.keys():
                    # pour ajouter le décalage correspondant
                    position += decalages[t[position + i]]
                else:
                    # Sinon on ajoute le décalage maximal : long_cle
                    position += long_cle
                
                # Si un caractère est différent, l'occurence n'existe pas
                trouve = False
                break   # On arrête la boucle POUR
            
            
        # Lorsque tous les caractères de la clé sont testés,
        # Si trouve est toujours Vrai, 
        # Alors on a trouvé une occurence de la clé
        
        if trouve:
            positions.append(position)
            
            # actualisation de la position pour la suite de la recherche
            position += 1


            
    return positions


assert boyer_moore("abra", "abracadabra") == [0, 7]
assert boyer_moore("clecle", "cleclecleclecle") == [0, 3, 6, 9]

