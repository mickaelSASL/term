# 2023 sujet 31 - ex2

valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)
 

# Les Tests
 
a_rendre, rang=67,0
print((a_rendre, rang),rendu_glouton(a_rendre, rang))
print('-----------------------------')
a_rendre, rang=291,0
print((a_rendre, rang),rendu_glouton(a_rendre, rang))
print('-----------------------------')
a_rendre, rang=291,1
# si on ne dispose pas de billets de 100
print((a_rendre, rang),rendu_glouton(a_rendre, rang))
print('-----------------------------')