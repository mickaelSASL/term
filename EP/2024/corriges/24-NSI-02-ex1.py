# NSI Partie Pratique 2024 - SUJET 02

# EXERCICE 1

def correspond(mot:str,mot_a_trous:str)-> bool:
    """Renvoie vrai si les deux mots sont correspondants"""
    if len(mot)!= len(mot_a_trous):
        return False
    else:
        for i in range(len(mot)):
            if mot[i]!= mot_a_trous[i] and mot_a_trous[i]!= '*':
                return False
        return True
    
print(f"correspond('INFORMATIQUE','INFO*MA*IQUE) --> {correspond('INFORMATIQUE','INFO*MA*IQUE')}\ncorrespond('AUTOMATIQUE','INFO*MA*IQUE') --> {correspond('AUTOMATIQUE','INFO*MA*IQUE')}\ncorrespond('STOP','S*') --> {correspond('STOP','S*')}\ncorrespond('AUTO','*UT*') --> {correspond('AUTO','*UT*')}")




print()