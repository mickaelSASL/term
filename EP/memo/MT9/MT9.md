---
hide:
  - navigation
  - toc
---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
[Retour](../../)


# **Méthode Diviser pour régner :TRI FUSION**

## Principe

> **DIVISER --> REGNER --> FUSIONNER**
![](medias/fusion.png)

## Algorithme
```
VARIABLE
tab1, tab2, resultat, t1, t2, t1_trie, t2_trie, res: tableaux d'entiers
pos1, pos2, n : entiers


DEBUT

FUSION (tab1, tab2):
  resultat = tableau vide
  pos1 ← 0
  pos2 ← 0
  TANT QUE pos1 < longueur de tab1 ET pos2 < longueur de tab2:
    SI tab1[pos1] < tab2[pos2]:
      ajouter à resultat tab1[pos1]
      pos1 = pos1 + 1
    SINON:
      ajouter à resultat tab2[pos2]
      pos2 = pos2 + 1
    FIN SI
  FIN TANT QUE
  SI pos1 < longueur de tab1: #Dans le cas où les tableaux sont de longueur différente
    Ajouter à la fin du tab1
  SINON:
    Ajouter à la fin du tab2
    RENVOYER resultat
  FIN SI
FIN FUSION

TRI-FUSION(tab):
  n ← longueur de tab
  SI n <= 1:
    RENVOYER tab
  SINON:
    # diviser 
    t1 ← première moitié de tab 
    t2 ← seconde moitié de tab
    # régner 
    t1_trie ← tri_fusion(t1) 
    t2_trie ← tri_fusion(t2) 
    # combiner 
    res ← fusion(t1_trie, t2_trie) 
    RENVOYER res
  FIN SI
FIN TRI-FUSION

FIN
```

## Implémentation en Python

```Python
def fusion(tab1, tab2): 
    resultat = [] 
    pos1, pos2 = 0, 0 
    while pos1 < len(tab1) and pos2 < len(tab2): 
        if tab1[pos1] < tab2[pos2]:     
            resultat.append(tab1[pos1]) 
            pos1 = pos1 + 1 
        else: 
            resultat.append(tab2[pos2]) 
            pos2 = pos2 + 1 
    if pos1 < len(tab1):  # Dans le cas où les 2 tableaux sont de longueur différente
        resultat = resultat + tab1[pos1:] 
    else: 
        resultat = resultat + tab2[pos2:]     
    return resultat

def tri_fusion(tab): 
    n = len(tab) 
    if n <= 1: 
        # cas de base 
        return tab 
    else: 
        # diviser 
        t1 = tab[:n // 2] 
        t2 = tab[n // 2:] 
        # régner 
        t1_trie = tri_fusion(t1) 
        t2_trie = tri_fusion(t2) 
        # combiner 
        res = fusion(t1_trie, t2_trie) 
        return res
```

## Complexité

<table width="100%" border="1" cellspacing="1" cellpadding="5">
  <tr>
    <td>
    logarithmique
    </td>
    <td>
    $$ O(n.log_2(n))$$ ou $$ O(log(n))$$
    </td>
  </tr>
</table>