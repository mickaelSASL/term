# **Epreuves Pratiques**
## SUJET 28 - Corrigé

**Exercice 1**

```Python
def taille(arbre,lettre):
    if arbre[lettre][0]!="" and arbre[lettre][1]!="":
        return 1+taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1])
    elif arbre[lettre][0]=="" and arbre[lettre][1]!="":
        return 1+taille(arbre,arbre[lettre][1])
    elif arbre[lettre][0]!="" and arbre[lettre][1]=="":
        return 1+taille(arbre,arbre[lettre][0])
    else :
        return 1


a= {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}

```

**Exercice 2**

```Python
def tri_iteratif(tab):
    for k in range( len(tab)-1 , 0, -1):
        imax = k
        for i in range(0 , k ):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab
```