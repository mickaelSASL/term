1a

l'ordre de grandeur de la complexité est $O(n.log_2(n))$ (logarithmique)


1b
L’algorithme de tri par insertion a une complexité en temps dans le pire des cas en $O(n^2)$.  
L’algorithme du tri par insertion est moins efficace que l’algorithme de tri fusion.


2
Voici l’affichage obtenu :
```python
[7, 4, 2,  1, 8,  5,  6, 3]
[7, 4, 2, 1]
[7,4]
[2, 1]
[8, 5, 6, 3]
[8, 5] 
[6, 3]

```
résultat renvoyé par la fonction : `[1,  2, 3, 4, 5, 6, 7, 8] `

3 

```Python
def moitie_droite(L): 
    n  = len(L) 
    deb = n//2 
    tab = [] 
    for i in range(deb,n):
        tab.append(L[i])
    return tab
```

Solution plus courte:
```Python
def moitie_droite(L): 
    return L[len(L)//2 : ]
```
4 

```Python
def fusion(L1, L2): 
    L=[] 
    n1 = len(L1) 
    n2 = len(L2) 
    i1 = 0 
    i2 = 0 
    while i1<n1 or i2<n2: 
        if i1>=n1:
            L.append(L2[i2]) 
            i2 = i2+1
        elif i2>=n2:
            L.append(L1[i1]) 
            i1=i1+1
        else :
            e1 = L1[i1] 
            e2 = L2[i2] 
            if e1 > e2:
                L.append(e2) 
                i2 = i2 + 1
            else :
                L.append(e1) 
                i1 = i1 + 1
    return L
```