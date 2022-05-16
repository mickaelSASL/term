# ** LP2: Exercices - Corrigé**

## A. Boucle

```python
    def boucle(i, k):
        if i == k:
            return str(i)
        else:
            return(str(i)+ ' ' + boucle(i+1,k))
```
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20boucle%28i,%20k%29%3A%0A%20%20%20%20if%20i%20%3D%3D%20k%3A%0A%20%20%20%20%20%20%20%20return%20str%28i%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%28str%28i%29%2B%20'%20'%20%2B%20boucle%28i%2B1,k%29%29%0A%20%20%20%20%20%20%20%20%0Aprint%28boucle%280,%203%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


## B. Le nombre de chiffres

**Version avec chaine de caractères :**

```python
    def nombre_de_chiffres(n):
        if len(str(n)) == 0:
            return 0
        else:
            return(1 + nombre_de_chiffres(str(n)[1:]))
```

**Version avec entiers :**

```python
    def nombre_de_chiffres(n):
        if n < 10:
            return 1
        else:
            return (1 + nombre_de_chiffres(n/10))
```

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20nombre_de_chiffres%28n%29%3A%0A%20%20%20%20if%20n%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20%281%20%2B%20nombre_de_chiffres%28n/10%29%29%0A%20%20%20%20%20%20%20%20%0Aprint%28nombre_de_chiffres%28123456%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## C. Fonction Factorielle

```python
def factoriel(x):
    """
    Fonction renvoyant la factorielle de x
    """
        
    if x == 1:					# Cas de base
        return 1
    else:
        return x * factoriel(x-1)
```

## B. Sommes

_Somme de 2 nombres_

```python
def somme(a, b):
    if b==0:
        return 1
    else:
        return somme(1, a-1) + somme(1, b-1)
```

_Somme de 2 relatifs_

```python
def somme_relatif(a, b):
    if b==0:
        return a
    else:
        if a>0 and b>0:
            return somme_relatif(1, a-1) + somme_relatif(1, b-1)
        if a>0 and b<0:
            return somme_relatif(1, a-1) + somme_relatif(-1, b+1)  
        if a<0 and b>0:
            return somme_relatif(-1, a+1) + somme_relatif(1, b-1)
        if a<0 and b<0:
            return somme_relatif(-1, a+1) + somme_relatif(-1, b+1)
```

## C. Palindromes
```python
def palind(x):
    """
    Fonction testant si un mot x est un palindrome
    Renvoie False si pas palindrome
    Renvoie True si palindrome
    """
    if len(x)>1:
        if x[0]==x[-1]:
            erreur = True
        else:
            erreur = False
        return erreur and palind(x[1:-1])
    else: 
        return False
    
print(palind("moto"))
print(palind("abba"))
print(palind("kayak"))
print(palind("salut"))

Sortie du programme:

False
True
True
False

```
## D. Suite de Fibonacci
```python
def fibonacci(n, suite=[]):
    """
    Fonction récursive affichant les n premiers nombres de la suite de Fibonacci
    suite=[] : paramètre optionnel, si omis prend la valeur par défaut : []
    """
    if n == 0:                  # Cas de base
         return [0, 1]          # Début de la suite
    else:
        suite = fibonacci(n-1)                         # Appel récursif de la fonction
        suite.append(suite[-1] + suite[-2])           # calcul du nouveau nombre, ajout à la liste
        return suite                                  # Renvoi de la liste contenant la suite

           
print(fibonacci(5))

Sortie du programme :
[0, 1, 1, 2, 3, 5, 8]

# On obtient une suite de n+2 nombres.
# Pour avoir une suite de n nombres, Que faut-il modifier ?

```
## F. EXERCICES EN PLUS  

### 1. Fractales

*Arbre de Pythagore*  

<table>
    <tr>
        <td width="50%" style="vertical-align: middle;">
            Angle de 30°
        </td>
        <td>
            <img src="https://www.mathweb.fr/euclide/wp-content/uploads/2019/03/Arbre-de-Pythagore.png" width="30%">
        </td>
    </tr>
    <tr>
        <td style="vertical-align: middle;">
            Angle de 50°
        </td>
        <td>
            <img src="https://www.mathweb.fr/euclide/wp-content/uploads/2019/03/Arbre-de-Pythagore-2.png" width="30%">
        </td>
    </tr>
    <tr>
        <td style="vertical-align: middle;">
            Angle de 110°
        </td>
        <td>
            <img src="https://www.mathweb.fr/euclide/wp-content/uploads/2019/03/Arbre-de-Pythagore-3.png" width="30%">
        </td>
    </tr>
</table>

```python
from turtle import *

angle = 30
color('#3f1905')

def arbre(n,longueur):
    if n==0:
        color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle) # tourne vers la gauche de angle degrés
        arbre(n-1,longueur*2/3)
        right(2*angle) # tourne vers la droite de angle degrés
        arbre(n-1,longueur*2/3)
        left(angle) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule

hideturtle() # cache la tortue
up() # lève le stylo
right(90) # tourne de 90 degrés vers la droite 
forward(300) # avance de 300 pixels
left(180) # fait un demi-tour
down() # pose le stylo
arbre(11,700) # exécute la macro
showturtle() # affiche la tortue
mainloop()
```

*Spirale*  
![](spirale.png)
```python
from turtle import *

def spirale(n):
    if n <= 0: 
        return   
    for j in range(4):
        forward(3*n)
        left(90)
    right(10)
    spirale(n-1)

speed(20)
pensize(2)
pencolor("black")

spirale(73)
mainloop()
```

### 2. Conjecture de Syracuse

```python
    def syracuse(u):
        print(u)
        if u != 1:
            if u%2==0:
                return syracuse(u/2)
            else:
                return syracuse(3*u+1)
        else:
            print("fin")
```
