# 2023 sujet 15 - ex1 fd

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

#Écrire la fonction mini qui prend en paramètres un tableau releve des relevés
# et un tableau date des dates
#et qui renvoie la plus petite valeur relevée au cours de la
#période et l’année correspondante. 
#On suppose que la température minimale est atteinte une seule fois.

def mini(temperatures,annees):
    '''In : temperatures,annees des listes
       Out : la plus petite valeur relevée au cours de la période
       et l’année correspondante. 
       '''
    min=temperatures[0]
    annee_min=annees[0]
    for i in range(1,len(temperatures)):
        if temperatures[i]<min:
            min=temperatures[i]
            annee_min=annees[i]
    return (min,annee_min)

#tests
print(mini(t_moy, annees))
