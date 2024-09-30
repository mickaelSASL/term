# 2022 - sujet 19 - ex1
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

n1,n2=-4,-8
print(n1,n2,multiplication(n1, n2))

n1,n2=-2,6
print(n1,n2,multiplication(n1, n2))

n1,n2=-2,0
print(n1,n2,multiplication(n1, n2))