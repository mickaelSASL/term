# Exemples d'utilisation d'une pile

## Vérification des parenthèses

### Algorithme
[Info](#){.btn .btn-info}

L'algorithme vérifiant la correction des parenthèses dans un programme utilise une pile.

| **1**  | **erreur FAUX**                                    |
| **2**  | **P est une pile vide**                            |
| **3**  | **i un compteur initialisé à 0**                   |
| **4**  | **exp la chaine de caractère à analyser**          |
| **5**  | **TANT que erreur est FAUX:**                      |
| **6**  | **c exp\[i\]**                                     |
| **7**  | **si c est une parenthèse (, { ou \[:**            |
| **8**  | **on empile c dans P**                             |
| **9**  | **sinon, si c est égal à ), } ou \]**              |
| **10** | **si P est vide**                                  |
| **11** | **erreur VRAI**                                    |
| **12** | **sinon**                                          |
| **13** | **on dépile P dans s**                             |
| **14** | **si c ne correspond pas à s :**                   |
| **15** | **erreur VRAI**                                    |
| **16** | **i i+1**                                          |
| **17** | **Si erreur est vrai ou P non vide**               |
| **18** | **on renvoie FAUX et \"erreur pos.\" i**           |
| **19** | **Sinon**                                          |
| **20** | **on renvoie VRAI et \"chaine bien parenthésée\"** |


### Trace de cet algorithme

Sur CHAINE = \"(3\*x+5\*\[10-x\])\"

  **C**   **P**   **Erreur**
  ------- ------- ------------
  (       (       FAUX
  3       (       FAUX
  \*      (       FAUX
  X       (       FAUX
  \+      (       FAUX
  5       (       FAUX
  \*      (       FAUX
  \[      (\[     FAUX
  10      (\[     FAUX
  \-      (\[     FAUX
  X       (\[     FAUX
  \]      (       FAUX
  )               FAUX

Sur CHAINE = \"(3\*\[x+5\]\*\[10-x)+17\*(x-1)\"

  **C**   **P**   **Erreur**
  ------- ------- ------------
  (       (       FAUX
  3       (       FAUX
  \*      (       FAUX
  \[      (\[     FAUX
  X       (\[     FAUX
  \+      (\[     FAUX
  5       (\[     FAUX
  \]      (       FAUX
  \*      (       FAUX
  \[      (\[     FAUX
  10      (\[     FAUX
  \-      (\[     FAUX
  X       (\[     FAUX
  )       (       VRAI

## Evaluation d\'une expression

Comment un programme évalue-t-il une expression du type :
$\left( \mathbf{5 -}\left( \mathbf{3} \times \mathbf{A + 2} \right) \right)\mathbf{\times}\mathbf{3}$
?

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

+--------+------------------------------------------------------------+
| **1**  | **Pour chaque élément E de EXP:**                          |
|        |                                                            |
| **2**  | **si E est +, -,** $\mathbf{\times}\ $**, ou / :**         |
|        |                                                            |
| **3**  | **on dépile les opérateurs de [priorité supérieure ou      |
|        | égale]{.ul}**                                              |
| **4**  |                                                            |
|        | **on les copie dans RESULT**                               |
| **5**  |                                                            |
|        | **on empile E dans P**                                     |
| **6**  |                                                            |
|        | **si E est une parenthèse \")\":**                         |
| **7**  |                                                            |
|        | **on dépile de P et on recopie dans RESULT jusqu\'à une    |
| **8**  | \"(\"**                                                    |
|        |                                                            |
| **9**  | **si E est une parenthèse \"(\":**                         |
|        |                                                            |
| **10** | **on l\'empile dans P**                                    |
|        |                                                            |
| **11** | **sinon (E est une variable ou un nombre):**               |
|        |                                                            |
| **12** | **on l\'ajoute à RESULT**                                  |
|        |                                                            |
| **13** | **A la fin, on dépile tous les éléments de P pour les      |
|        | copier dans RESULT**                                       |
| **14** |                                                            |
|        |                                                            |
| **15** |                                                            |
+--------+------------------------------------------------------------+

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

+--------+------------------------------------------------------------+
| **1**  | **Pour chaque élément E de la chaine RESULT obtenue par    |
|        | post-fixage**                                              |
| **2**  |                                                            |
|        | **Si E est un nombre :**                                   |
| **3**  |                                                            |
|        | **on l\'empile dans P**                                    |
| **4**  |                                                            |
|        | **Si non, si E est un +, -,** $\mathbf{\times}\ $**, /:**  |
| **5**  |                                                            |
|        | **on dépile 2 fois :**                                     |
| **6**  |                                                            |
|        | **a dépiler(P)**                                           |
| **7**  |                                                            |
|        | **b dépiler(P)**                                           |
| **8**  |                                                            |
|        | **on effectue l\'opération E entre b et a, résultat dans   |
| **9**  | R**                                                        |
|        |                                                            |
| **10** | **On empile R dans P**                                     |
|        |                                                            |
| **11** | **A la fin le résultat est au sommet de la pile P.**       |
|        |                                                            |
| **12** |                                                            |
|        |                                                            |
| **13** |                                                            |
+--------+------------------------------------------------------------+

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
