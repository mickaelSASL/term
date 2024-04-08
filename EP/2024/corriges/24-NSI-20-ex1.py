#NSI pratique 2024 sujet - ex1
import random

def lancer(n):
    return [random.randint(1,6) for _ in range(n)]

def paire_6(list):
    counter=0
    for num in list:
        if num==6:
            counter+=1
    print(f'value of the counter: {counter}')
    return counter>=2

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))
lancer3 = lancer(3)
print(paire_6(lancer3))
lancer4 = lancer(0)
print(paire_6(lancer4))
