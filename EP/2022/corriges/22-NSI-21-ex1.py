# 2022 - sujet 21 - ex1
# Programmer la fonction multiplication, prenant en paramètres deux nombres
#entiers n1 et n2, et qui renvoie le produit de ces deux nombres.
#Les seules opérations autorisées sont l’addition et la soustraction.
def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat

n1,n2=3,5
print(n1,n2,multiplication(n1, n2))

n1,n2=-3,5
print(n1,n2,multiplication(n1, n2))

n1,n2=-3,-5
print(n1,n2,multiplication(n1, n2))