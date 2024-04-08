# **Epreuves Pratiques**
## SUJET 9 - Corrigé

**Exercice 1**

```Python
def tri_selection(t):
    N = len(t)
    i = 0
    while i < N-1 :
        j = i + 1
        min = i
        while j < N:
            if t[j]<t[min]:
                min=j
            j = j + 1
        if min != i :
            k = t[i]
            t[i] = t[min]
            t[min] = k
        i = i +1
    return t
```

**Exercice 2**

```Python
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre était ",nb_mystere)
```