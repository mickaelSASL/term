![](./Morse-code-tree.svg)  
Une branche à gauche correspond à un point (.) et une branche correspond à un tiret (-).

**1. Implémentez cet arbre en python.**

Aide : 
```Python
MORSE_CODE_DICT = { 'A':10, 'B':15,
                    'C':19, 'D':16, 'E':7,
                    'F':5, 'G':24, 'H':1,
                    'I':4, 'J':13, 'K':20,
                    'L':8, 'M':26, 'N':17,
                    'O':27, 'P':11, 'Q':25,
                    'R':9, 'S':2, 'T':22,
                    'U':6, 'V':3, 'W':12,
                    'X':16, 'Y':21, 'Z':23, '*':14}

# le caractère * représente la racine de l'arbre
```
**2. Ecrire une fonction pour le décodage d'un caractère en code morse vers l'alphabet.**

Exemple d'exécution :

```Python
>>> decode("... --- ...")
Message décodé : S O S
```