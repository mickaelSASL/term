# 2024 NSI sujet 48 - ex 1

def voisins_entrants(adj,x):
    listeFin = []
    for i in range(len(adj)):
        if x in adj[i]:
            listeFin.append(i)
    return listeFin

print(voisins_entrants([[1, 2], [2], [0], [0]], 0)) #[2, 3]
print(voisins_entrants([[1, 2], [2], [0], [0]], 1)) #[0]