# NSI Partie Pratique 2024 - SUJET 02

# EXERCICE 2

def est_cyclique(plan):
    '''
        Prend en paramètre un dictionnaire `plan` correspondant à
        un plan d'envoi de messages (ici entre les personnes A, B, C,
        D, E, F).
        Renvoie True si le plan d'envoi de messages est cyclique et
        False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1 
    return nb_destinataires == 6

print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})) #False
print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})) #True
print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})) #True
print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})) #False




