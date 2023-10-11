# **Epreuves Pratiques**
## SUJET 9 - Corrigé

**Exercice 1**

```Python
def recherche(tab,n):
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        milieu = (debut + fin)//2
        if tab[milieu] == n:
            return milieu
        elif n>tab[milieu]:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1
```

**Exercice 2**

```Python
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre)+decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat+lettre
    return resultat
```