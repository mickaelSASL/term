<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 19


[Corrigé](corrige.md)


**Exercice 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche dichotomique du nombre entier `n` dans le tableau non vide `tab`.

Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le tableau, `-1` sinon.


Exemples:
```Python
>>>	recherche([2, 3, 4, 5, 6], 5)
3
>>>	recherche([2, 3, 4, 6, 7], 5)
-1
```


**Exercice 2 (4 points)**

Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet.

Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A, le Y en B et le Z en C. Les autres caractères (‘!’, ’?’…) ne sont pas codés.

La fonction `position_alphabet` ci-dessous prend en paramètre un caractère `lettre` et renvoie la position de `lettre` dans la chaîne de caractères `ALPHABET` s’il s’y trouve et `-1` sinon.

La fonction `cesar` prend en paramètre une chaîne de caractères message et un nombre entier `decalage` et renvoie le nouveau message codé avec le codage de César utilisant le décalage `decalage`.



```Python 
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
resultat = ''
    for ... in message :
        if lettre in ALPHABET :
            indice = ( ... )%26
            resultat = resultat + ALPHABET[indice] 
        else:
            resultat = ...
    return resultat
```

Compléter la fonction cesar.

Exemples :
```Python
>>>	cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'

>>>	cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
```