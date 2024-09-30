# 2022 sujet 37 - ex1
def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

# Les Tests

tab=[0, 5, 8, 8, 9]
print(tab,verifie(tab))

tab=[8,12,4]
print(tab,verifie(tab))

tab=[-1,4]
print(tab,verifie(tab))

tab=[5]
print(tab,verifie(tab))