# **Epreuves Pratiques**
## SUJET 7 - Corrigé

**Exercice 1**

```Python
def fibonacci(n):
    u = [None, 1, 1]
    i = 2
    while len(u) <= n:
        i = i + 1
        u.append(u[i-2] + u[i-1])
    return u[n]

```

**Exercice 2**

```Python
liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi =  []
    
    for compteur in range(len(liste_notes)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]
            
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)
```