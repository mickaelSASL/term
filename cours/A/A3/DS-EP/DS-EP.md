On dispose :

- d'un camion pouvant transporter un poids `P`.  
- d'un ensemble de n colis ayant chacun un poids $p_i$ et une valeur $v_i$.  

Avec :  

* $1 =< i =< n$  
* $p_1 + p_2 + p_3 + ... + p_n > P$

On souhaite mettre dans le camion le plus de colis possible tout en maximisant la valeur totale transportée dans le camion.

Le remplissage du camion suit 3 règles à chaque colis contrôlé:

* Il n'y a pas de colis (ensemble vide) : la valeur est nécessairement nulle.
* Le colis contrôlé est plus lourd que le poids autorisé : il n'est pas chargé.
* Le poids du colis contrôlé l'autorise à être chargé : il faut choisir la valeur la plus grande parmi :  
    * une autre combinaison avec les colis restants (sans le colis contrôlé)
    * la valeur du colis contrôlé + la valeur d'une combinaison des colis restants (en déduisant le poids du colis contrôlé)



Compléter la fonction `camion` avec une approche récursive "Diviser pour régner".

Vous vérifierez votre réponse avec l'exemple donné.
```python
# colis : (poids, valeur)

def camion(E, P, i):
    if i == 0:
        return ...
    if E[i-1][0]>...:
        return camion(E, P, ...)
    else:
        return max(camion(...), E[i-1][1] + ...)
    

print(camion(E, P, len(E)))
```

```python
E=((12,14), (1,2), (4,10), (1,1), (2,2))
P=15

>>> camion(E, P, len(E))
18
```
