# NSI pratique 2024 sujet 13 - ex2

def insere(a, tab):
    """
    Insere l'element a (int) dans le tableau tab (list)
    trie par ordre croissant a  sa place et renvoie le
    nouveau tableau.
    """
    l = list(tab) #l contient les mÃªmes Ã©lÃ©ments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l

# tests
print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))