# NSI pratique 2024 sujet - ex1

#methode naive
def recherche_motif(motif, texte):
    list=[]
    for i in range(len(texte)-len(motif)+1):
        j = 0
        while j < len(motif) and motif[j] == texte[i+j]:
            j += 1
        if j == len(motif):
            list.append(i)
    return list

print(recherche_motif("ab", ""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))