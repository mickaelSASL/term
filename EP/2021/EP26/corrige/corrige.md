# **Epreuves Pratiques**
## SUJET 26 - Corrigé

**Exercice 1**

```Python
def occurrence_max(chaine):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
    occurence=[0]*26
    for c in chaine:
        if c in alphabet:
            i = alphabet.index(c)
            occurence[i]=occurence[i]+1
    m=0
    k=0
    for i in range(len(occurence)):
        if occurence[i]>m:
            m=occurence[i]
            k=i
    return alphabet[k]
```

**Exercice 2**

```Python
def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            L[i][j] = 255-image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inférieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


```