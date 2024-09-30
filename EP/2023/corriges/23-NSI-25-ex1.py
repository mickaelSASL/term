# 2023 sujet 25 - ex1

def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]].append(i)
        else:
            d[L[i]] = [i]
    return d

# Tests
print(enumere([1, 1, 2, 3, 2, 1]))