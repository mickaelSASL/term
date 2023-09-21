<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# **Epreuves Pratiques**
## SUJET 29

[Corrigé](corrige.md)

**Exercice 1 (4 points)**

Soit un nombre entier supérieur ou égal à 1 :

* s'il est pair, on le divise par 2 ;
* s’il est impair, on le multiplie par 3 et on ajoute 1.

Puis on recommence ces étapes avec le nombre entier obtenu, jusqu’à ce que l’on obtienne la valeur 1.

On définit ainsi la suite ( \\(u_{n} \\) ) par

* \\(u_{0} = k\\) , où `k` est un entier choisi initialement ;
* \\(u_{n+1} = u_{n} / 2\\) si \\(u_{n} \\) est pair ;
* \\(u_{n+1} = 3×u_{n} + 1\\) si \\(u_{n} \\) est impair.

On admet que, quel que soit l’entier `k` choisi au départ, la suite finit toujours sur la valeur 1.

Écrire une fonction `calcul` prenant en paramètres un entier `n` strictement positif et qui renvoie la liste des valeurs \\(u_{n} \\), en partant de `k` et jusqu’à atteindre 1.

Exemple :
```Python
>>> calcul(7)
[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```



**Exercice 2 (4 points)**

On affecte à chaque lettre de l’alphabet un code selon les tableaux ci-dessous :

<table>
    <TR>
        <TD>A</TD><TD>B</TD><TD>C</TD><TD>D</TD><TD>E</TD><TD>F</TD><TD>G</TD><TD>H</TD><TD>I</TD><TD>J</TD><TD>K</TD><TD>L</TD><TD>M</TD><TD>N</TD><TD>O</TD>
    </TR>
    <TR>
        <TD>1</TD><TD>2</TD><TD>3</TD><TD>4</TD><TD>5</TD><TD>6</TD><TD>7</TD><TD>8</TD><TD>9</TD><TD>10</TD><TD>11</TD><TD>12</TD><TD>13</TD><TD>14</TD><TD>15</TD>
    </TR>
</table>

<table>
    <TR>
        <TD>P</TD><TD>Q</TD><TD>R</TD><TD>S</TD><TD>T</TD><TD>U</TD><TD>V</TD><TD>W</TD><TD>X</TD><TD>Y</TD><TD>Z</TD>
    </TR>
    <TR>
        <TD>16</TD><TD>17</TD><TD>18</TD><TD>19</TD><TD>20</TD><TD>21</TD><TD>22</TD><TD>23</TD><TD>24</TD><TD>25</TD><TD>26</TD>
    </TR>
</table>

Pour un mot donné, on détermine d’une part son code alphabétique concaténé, obtenu par la juxtaposition des codes de chacun de ses caractères, et d’autre part, son code additionné, qui est la somme des codes de chacun de ses caractères. Par ailleurs, on dit que ce mot est « parfait » si le code additionné divise le code concaténé.

Exemples :

* Pour le mot `"PAUL"`, le code concaténé est la chaîne `1612112`, soit l’entier `1 612 112`.
Son code additionné est l’entier `50` car `16 + 1 + 21 + 12 = 50`.
`50` ne divise pas l’entier `1 612 112` ; par conséquent, le mot `"PAUL"` n’est pas parfait.

* Pour le mot `"ALAIN"`, le code concaténé est la chaîne `1121914`,  soit l’entier `1 121 914`.
Le code additionné est l’entier `37` car `1 + 12 + 1 + 9 + 14 = 37`.
`37` divise l’entier `1 121 914` ; par conséquent, le mot `"ALAIN"` est parfait.


Compléter la fonction `est_parfait` ci-dessous qui prend comme argument une chaîne de caractères `mot` (en lettres majuscules) et qui renvoie le code alphabétique concaténé, le code additionné de `mot`, ainsi qu’un booléen qui indique si `mot` est parfait ou pas.


```Python
dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,  "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,  "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,  "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}
```

```Python
def est_parfait(mot) :
    #mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""

    code_a = ???
    for c in mot :
        code_c = code_c + ???
        code_a = ???

    code_c = int(code_c)
    if ??? :
        mot_est_parfait = True

    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]
```


Exemples :
```Python
>>>	est_parfait("PAUL") 
[50, 1612112, False]

>>>	est_parfait("ALAIN") 
[37, 1121914, True]
```