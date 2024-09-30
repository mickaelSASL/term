#2022 - sujet 23 - ex1
def max_dico(dico):
    cle_max = ''
    val_max = 0
    for cle in dico:
        if dico[cle] > val_max:
            val_max = dico[cle]
            cle_max = cle
    return (cle_max, val_max)

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))