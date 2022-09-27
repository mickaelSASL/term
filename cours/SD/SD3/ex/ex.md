<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Exemples d'utilisation d'une pile

## Vérification des parenthèses

### Algorithme

L'algorithme vérifiant la correction des parenthèses dans un programme utilise une pile.

```
erreur à FAUX
P est une pile vide
i un compteur initialisé à 0
exp la chaine de caractère à analyser
TANT que erreur est FAUX:
	c à exp[i]
	si c est une parenthèse (, { ou [:
		on empile c dans P
  	sinon, si c est égal à ), } ou ]
		si P est vide
			erreur à VRAI
		sinon
			on dépile P dans s
			si c ne correspond pas à s : 
				erreur à VRAI
  i à i+1
Si erreur est vrai ou P  non vide
	on renvoie FAUX et "erreur pos." i
Sinon
	on renvoie VRAI et "chaine bien parenthésée"
```

### Trace de cet algorithme
===! "Sur CHAINE = $(3x+5x[10-x])$"

 | **C**  | **P**  | **Erreur**   |
 |:------:|:------:|:----------- :|
 | (      | (      |      FAUX    | 
 | 3      | (      |      FAUX    | 
 | \*     | (      |      FAUX    | 
 | X      | (      |      FAUX    | 
 | \+     | (      |      FAUX    | 
 | 5      | (      |      FAUX    | 
 | \*     | (      |      FAUX    | 
 | \[     | (\[    |      FAUX    | 
 | 10     | (\[    |      FAUX    | 
 | \-     | (\[    |      FAUX    | 
 | X      | (\[    |      FAUX    | 
 | \]     | (      |      FAUX    | 
 | )      |        |      FAUX    |  

=== "Sur CHAINE = $(5-(3×A+2))×3$"

 | **C**  | **P**  | **Erreur**   |
 |:------:|:------:|:----------- :|
 | (      | (      |     FAUX     |
 | 3      | (      |     FAUX     |
 | \*     | (      |     FAUX     |
 | \[     | (\[    |     FAUX     |
 | X      | (\[    |     FAUX     |
 | \+     | (\[    |     FAUX     |
 | 5      | (\[    |     FAUX     |
 | \]     | (      |     FAUX     |
 | \*     | (      |     FAUX     |
 | \[     | (\[    |     FAUX     |
 | 10     | (\[    |     FAUX     |
 | \-     | (\[    |     FAUX     |
 | X      | (\[    |     FAUX     |
 | )      | (      |     VRAI     |


## Evaluation d\'une expression

Comment un programme évalue-t-il une expression du type :
$5 -(3 \times A + 2))\  \times \ 3$ ?

### Notation RPN ou Post Fixée

L\'expression est d\'abord transformée en notation post-fixée qui
supprime l\'utilité des parenthèses :

> $3\  \times \ x + 2$ devient $3\ x\  \times \ 2\  +$
>
> $3\  \times \ (x + 2)$ devient $3\ x\ 2\  + \  \times$

### Algorithme

-   **P** est une pile vide

-   **RESULT** une chaine de caractères vide

-   **EXP** est l\'expression à analyser, valide

```
Pour chaque élément E de EXP:
	si E est +, -, × , ou / :
		on dépile les opérateurs de   				priorité supérieure ou égale
		on les copie dans RESULT
		on empile E dans P
	si E est une parenthèse ")":
		on dépile de P et on recopie 			dans RESULT jusqu'à une "("
	si E est une parenthèse "(":
		on l'empile dans P
	sinon (E est une variable ou un nombre):
		on l'ajoute à RESULT
A la fin, on dépile tous les éléments de P pour les copier dans RESULT

```


### Trace sur $\left( 5 - (3 \times A + 2) \right) \times 3$

  **E**        **P**          **RESULT**
  ------------ -------------- ---------------------------------
  (            (              
  5            (              5
  \-           -(             5
  (            (-(            5
  3            (-(            5 3
  $$\times$$   $\times$ (-(   5 3 A
  A            $\times$ (-(   5 3 A
  \+           +(-(           5 3 A $\times$
  2            +(-(           5 3 A $\times$ 2
  )            -(             5 3 A $\times$ 2 +
  )                           5 3 A $\times$ 2 + -
  $$\times$$   $$\times$$     5 3 A $\times$ 2 + -
  3            $$\times$$     5 3 A $\times$ 2 + - 3
                              5 3 A $\times$ 2 + - 3 $\times$

##  Evaluation d\'une expression

Une fois qu\'on a l\'expression post-fixée, on peut l\'évaluer
facilement avec une pile:

### Algorithme

P est une pile

```
Pour chaque élément E de la chaine RESULT obtenue par post-fixage
	Si E est un nombre :
		on l'empile dans P
	Si	non, si E est un +, -, × , /:
		on dépile 2 fois :
		a  dépiler(P)
		b  dépiler(P)
		on effectue l'opération E entre 			b et a, résultat dans R
		On empile R dans P
A la fin le résultat est au sommet de la pile P.
```


### Exemple et trace :

$$(30 - ((3\  \times 8) + \ 2)) \times 3$$

$$30\ 3\ 8\  \times \ 2\  + \  - \ 3\  \times$$

  **E**        **a**   **b**   **R**                            **P**
  ------------ ------- ------- -------------------------------- -----------
  5                                                             30
  3                                                             3, 30
  8                                                             8, 3, 30
  $$\times$$   8       3       3$\times$`<!-- -->`{=html}8=24   24, 30
  2                                                             2, 24, 30
  \+           2       24      24+2=26                          26, 30
  \-           26      30      30-26=4                          4
  3                                                             3, 4
  $$\times$$   3       4       4$\times$`<!-- -->`{=html}3      12

$$((30 - 3)/9) \times (8 + 5)$$

$$30\ 3\ –\ 9\ 8\ 5\  + \  \times \ \ $$

  **E**        **a**   **b**   **R**                             **P**
  ------------ ------- ------- --------------------------------- ---------
  30                                                             30
  3                                                              3, 30
  \-           3       30      30-3=27                           27
  9                                                              9, 27
  /            9       27      27/9=3                            3
  8                                                              8, 3
  5                                                              5, 8, 3
  \+           5       8       8+5=13                            13, 3
  $$\times$$   13      3       3$\times$`<!-- -->`{=html}13=39   39
