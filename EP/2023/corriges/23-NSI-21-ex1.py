# 2023 sujet 21 - ex1

def delta(tab):
    diff = [tab[0]]
    for i in range(1, len(tab)):
        diff.append(tab[i] - tab[i-1])
    return diff

# Tests
print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
