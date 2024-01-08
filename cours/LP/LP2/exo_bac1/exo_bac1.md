# Exercice type BAC 1
## Sujet NSIJ2G11 - Centres étrangers 2, 2022

[Corrigé](correction_exo_bac1.pdf)

*Cet exercice porte sur les langages et la programmation (récursivité).* 

1. Voici une fonction codée en Python :
```Python
def f(n): 
 if n == 0: 
 print("Partez!") 
 else: 
 print(n) 
 f(n-1) 
```
    1. Qu’affiche la commande `f(5)` ?  
    1. Pourquoi dit-on de cette fonction qu'elle est récursive ?  

1. On rappelle qu’en python l’opérateur `+` a le comportement suivant sur les chaînes de caractères :
```Python
>>> S = 'a'+'bc' 
>>> S 
'abc'
```
Et le comportement suivant sur les listes :
```Python
>>> L = ['a'] + ['b', 'c'] 
>>> L 
['a', 'b', 'c'] 
```
On a besoin pour les questions suivantes de pouvoir ajouter une chaîne de caractères `s` en préfixe à chaque chaîne de caractères de la liste `liste`. On appellera cette fonction `ajouter`.  Par exemple, `ajouter("a",["b","c"])` doit retourner `["ab","ac"]`.
    1. Recopiez le code suivant et complétez `.......` sur votre copie :
```Python
def ajouter(s, liste): 
 res = [] 
 for m in liste: 
 res ................. 
 return res  
```  
    1. Que renvoie la commande `ajouter("b", ["a","b","c"])` ?  
    1. Que renvoie la commande `ajouter("a", [""])` ?  


1. On s'intéresse ici à la fonction suivante écrite en Python où `s` est une chaîne de caractères et `n` un entier naturel.  
```Python
def produit(s, n): 
 if n == 0: 
 return [""] 
 else: 
 res = [] 
 for i in range(len(s)): 
 res = res + ajouter(s[i], produit(s, n-1)) 
 return res
```
    1. Que renvoie la commande `produit("ab", 0)` ?  
    Le résultat est-il une liste vide ?  
    1. Que renvoie la commande `produit("ab", 1)` ?  
    1. Que renvoie la commande `produit("ab", 2)` ?