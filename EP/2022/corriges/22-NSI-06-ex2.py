# 2022 - sujet 6 - ex2

def recherche(gene, seq_adn):
    n = len(seq_adn) # la longueur de la chaine (n)
    g = len(gene) #   la longueur du motif (g)
    i = 0 # C'est l'indice i de parcours de la chaîne, initialisé à 0
    trouve = False
    while i < n-g+1 and trouve == False :
        # La recherche continue tant que i est inférieure strictement à n - g +1
        # ou inférieure ou égale à n-g
        # et que la motif n'a pas été trouvé
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1 # On a une correspondance, j est l'indice de parcours du motif,
            # on continue à chercher en avançant dans le motif j--> j+1.
        if j == g:
            trouve = True
        i+=1 #


    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))
print(recherche("AGTC", "GTACAAATCTTGCC"))
# on teste quand la séquence est à la fin ou au début
print(recherche("AGTC", "GTACAAATCTTGCCAGTC"))
print(recherche("AGTC", "AGTCGTACAAATCTTGCC"))

 