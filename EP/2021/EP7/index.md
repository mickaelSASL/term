<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 7


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

On s’intéresse à la suite d’entiers définie par

$$U1 = 1, U2 = 1.$$ et, pour tout entier naturel `n`, par $$Un+2 = Un+1 + Un.$$.

Elle s’appelle la suite de Fibonnaci.

Écrire la fonction fibonacci qui prend un entier `n > 0` et qui renvoie l’élément d’indice `n` de cette suite.

On utilisera une programmation dynamique (pas de récursivité).

Exemples :

```Python
>>>	fibonacci(1)
1

>>>	fibonacci(2)
1
>>>	fibonacci(25)
75025

>>>	fibonacci(45)
1134903170
```

**Exercice 2 (4 points)**

Les variables liste_eleves et liste_notes ayant été préalablement définies et étant de même longueur, la fonction meilleures_notes renvoie la note maximale qui a été attribuée, le nombre d’élèves ayant obtenu cette note et la liste des noms de ces élèves.

Compléter le code Python de la fonction  meilleures_notes ci-dessous.

```Python
liste_eleves = ['a','b','c','d','e','f','g','h','i','j'] liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = ...
    liste_maxi =	...

    for compteur in range(...):
        if liste_notes[compteur] == ...:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[...])

        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur] nb_eleves_note_maxi = ... 
            liste_maxi = [...]

    return (note_maxi,nb_eleves_note_maxi,liste_maxi)
```

Une fois complété, le code ci-dessus donne
```Python
>>>	meilleures_notes() (80, 3, ['c', 'f', 'h'])
```