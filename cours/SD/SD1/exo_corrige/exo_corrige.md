# ** SD1 : Exercices - Corrigé**

## 1. Date au lendemain

```python
def demain(ma_date):    
    setJour(getJour(ma_date)+1)
```

## 2. moyenne d'une liste

```python
def moyenne(ma_liste):    
    total = 0
    for i in ma_liste:
        total = total + i
    return total / len(ma_liste)
```

## 3. Longueur d'une liste

### a. avec la méthode len()

```python
def longueur(ma_liste):    
    return len(ma_liste)
```

### b. sans la méthode len()

```python
def longueur(ma_liste):
    ct = 0    
    while ma_liste != []:
        ma_liste.pop()
        ct += 1
    return ct
```

## 4. Représenter un type de données

![](pile crêpes.png)
![](pile_graph.png)