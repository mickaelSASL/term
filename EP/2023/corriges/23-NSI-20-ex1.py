# 2023 sujet 20 - ex1

def ajoute_dictionnaires(d1, d2):
    for cle in d2:
        if cle in d1:
            d1[cle] += d2[cle]
        else:
            d1[cle] = d2[cle]
    return d1

# tests
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))
