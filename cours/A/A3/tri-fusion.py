def diviser(l):
    long = len(l)
    return l[:long//2], l[long//2:]

def combiner(gauche,droite):
    resultat = []
    while len(gauche) > 0 and len(droite) > 0:  
        if gauche[0] < droite[0]:
            resultat.append(gauche[0])
            gauche = gauche[1:]
        else:
            resultat.append(droite[0])
            droite = droite[1:]
    if len(gauche) == 0:
        resultat = resultat + droite
    else:
        resultat = resultat + gauche
    return resultat

def tri_fusion(l):
    if len(l)<=1:
        return l
    else:
        gauche,droite = diviser(l)
        return combiner(tri_fusion(gauche), tri_fusion(droite))
    

print(tri_fusion([2,8,3,6,9,-4,5,1]))