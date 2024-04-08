# Sujet 28 #

# Exercice 1

def fibo(n):
    if n == (1 or 0):
        return 1
    else:
        x = [1, 1]
        for i in range(2, n):
            x.append(x[i-1] + x[i-2])
    return x[n-1]

print(fibo(25))

# Exercice 2

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(notes)) :
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(eleves_du_mois(eleves_nsi, notes_nsi))
print(eleves_du_mois([],[]))
