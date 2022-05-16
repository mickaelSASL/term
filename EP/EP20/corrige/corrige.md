# **Epreuves Pratiques**
## SUJET 20 - Corrigé

**Exercice 1**

```Python
def mini(releve,date):
    m = releve[0]
    ind = 0
    for i in range(1,len(releve)):
        if releve[i]<m:
            m=releve[i]
            ind=i
    return (m,date[ind])
    
```

**Exercice 2**

```Python
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere+result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine==inverse
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
```