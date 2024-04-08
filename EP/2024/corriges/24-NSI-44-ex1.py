# 24-NSI-44 Ex1
def enumere(tab):
    dico = {}
    for x in tab:
        dico[x] = []
        for i in range(len(tab)):
            if tab[i] == x:
                dico[x].append(i)
    return dico
print(enumere([]))
print(enumere([1,2,3]))
print(enumere([1, 1, 2, 3, 2, 1]))

    