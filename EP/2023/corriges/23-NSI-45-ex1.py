# 2023 sujet 45 - ex1

def rangement_valeurs(notes_eval):
    lst = [0]*11
    for note in notes_eval:
        lst[note] += 1
    return lst

def notes_triees(effectifs_notes):
    triees = []
    for i in range(11):
        if effectifs_notes[i] != 0:
            for _ in range(effectifs_notes[i]):
                triees.append(i)
    return triees
 
 
# Les Tests

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

effectifs_notes = rangement_valeurs(notes_eval)
print(effectifs_notes)
print(notes_triees(effectifs_notes))
