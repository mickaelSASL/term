# 24-NSI-47 Ex1
def max_dico(dico):
    max = 0
    for cle in dico:
        if dico[cle]>max:
            max = dico[cle]
            tup = (cle,max)
    return tup
print(max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }))
print(max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }))