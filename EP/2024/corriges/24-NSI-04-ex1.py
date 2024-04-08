print("\nNSI Partie Pratique - SUJET nº04\nBooleans/conditions et ...\n------------------------------------------\n\n• Exo 1 -->")

def recherche(tab:list,n:int)->int:
    indice = None
    for i in range(len(tab)):
        if tab[i]==n:
            indice = i
    return indice

def recherche1(tab:list,n:int)->int:
    return [['None']+[i for i in range(len(tab)) if tab[i]==n]][-1][-1]

#tests
print(f"""
recherche([5,3],1) --> {recherche([5,3],1)}
recherche([2,4],2) --> {recherche([2,4],2)}
recherche([2,3,5,2,4],2) --> {recherche([2,3,5,2,4],2)}
""")

print(f"""recherche1([5,3],1) --> {recherche1([5,3],1)}
recherche1([2,4],2) --> {recherche1([2,4],2)}
recherche1([2,3,5,2,4],2) --> {recherche1([2,3,5,2,4],2)}
""")
print("• Exo 2 -->") 

def distance_carre(point1,point2):
    """Calcule et renvoie la distance au carre entre deux points."""
    return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2

def point_le_plus_proche(depart,tab):
    """ Renvoie les coordonnées du premier point du tableau tab se trouvant à la plus courte distance du point départ."""
    min_point = tab[0]
    min_dist = distance_carre(min_point, depart) 
    for i in range(1,len(tab)):
        if distance_carre(tab[i],depart) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(tab[i],depart)
    return min_point

#tests
print(f"""distance_carre((1,0), (5,3)) --> {distance_carre((1,0), (5,3))}
distance_carre((1,0),(0,1)) --> {distance_carre((1,0),(0,1))}
point_le_plus_proche((0,0),[(7,9),(2,5),(5,2)]) --> {point_le_plus_proche((0,0),[(7,9),(2,5),(5,2)])}
point_le_plus_proche((5,2),[(7,9),(2,5),(5,2)]) --> {point_le_plus_proche((5,2),[(7,9),(2,5),(5,2)])}
""")


