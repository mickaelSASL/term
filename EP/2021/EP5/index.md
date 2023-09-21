# **Epreuves Pratiques**
## SUJET 5


[Corrigé](corrige.md)


**Exercice 1 (4 points)**  
On modélise la représentation binaire d'un entier non signé par un tableau d'entiers dont les éléments sont 0 ou 1. Par exemple, le tableau `[1, 0, 1, 0, 0, 1, 1]` représente l'écriture binaire de l'entier dont l'écriture décimale est
`2**6 + 2**4 + 2**1 + 2**0 = 83`.

À l'aide d'un parcours séquentiel, écrire la fonction `convertir` répondant aux spécifications suivantes :

```Python
def convertir(T):
    """
        T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
        représentant un entier écrit en binaire. Renvoie l'écriture
        décimale de l'entier positif dont la représentation binaire
        est donnée par le tableau T
    """

Exemple :
>>>	convertir([1, 0, 1, 0, 0, 1, 1])
83
>>>	convertir([1, 0, 0, 0, 0, 0, 1, 0])
130
```


**Exercice 2 (4 points)**  

La fonction tri_insertion suivante prend en argument une liste L et trie cette liste en utilisant la méthode du tri par insertion. Compléter cette fonction pour qu'elle réponde à la spécification demandée.

```Python
def tri_insertion(L):
    n = len(L)

    #   cas du tableau vide 
    if ...:
        return L

    for j in range(1,n):
        e = L[j]
        i = j

        #	A l'étape j, le sous-tableau L[0,j-1] est trié
        #	et on insère L[j] dans ce sous-tableau en déterminant
        #	le plus petit i tel que 0 <= i <= j et L[i-1] > L[j]. 
        while i > 0 and L[i-1] > ...:
            i	= ...

        #	si i != j, on décale le sous tableau L[i,j-1] d’un cran
        #	vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j,i,...):
                L[k] = L[...]
            L[i] = ...
    return L

```

Exemples :
```Python
>>>	tri_insertion([2,5,-1,7,0,28]) 
[-1, 0, 2, 5, 7, 28]
>>>	tri_insertion([10,9,8,7,6,5,4,3,2,1,0) 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```