# 2023 sujet 13 - ex2

def rendu_monnaie(somme_due, somme_versee):
    ''' In : somme_due et somme_versee  deux int
       Out : un tableau de type list contenant les pièces qui
composent le rendu.
      '''
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre =   somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre>0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i-1
    return rendu

#tests
(somme_due, somme_versee)=700,700
print(f'avec {(somme_due, somme_versee)}=',rendu_monnaie(somme_due, somme_versee))
(somme_due, somme_versee)=102,500
print(f'avec {(somme_due, somme_versee)}=',rendu_monnaie(somme_due, somme_versee))