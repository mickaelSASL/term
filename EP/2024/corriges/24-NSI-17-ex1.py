# NSI pratique 2024 sujet 17 - ex1

def nb_repetitions(elt, tab):
    nb = 0
    for element in tab:
        if element == elt:
            nb += 1
    return nb
 

# Les Tests
(elt, tab)=5,[1,3,5,9,5,5]
print((elt, tab),nb_repetitions(elt, tab))