# 2023 sujet 11 - ex1


def convertir(tab):
    puissance = 0
    total = 0
    for i in range(len(tab)-1, -1, -1):
        total += tab[i]*(2**puissance)
        puissance += 1
    return total

# Tests
print(convertir([1, 0, 1, 0, 0, 1, 1]))

print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))
