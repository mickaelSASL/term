# 24-NSI-42 Ex1
def moyenne(L):
    sum = 0
    for x in L:
        sum+=x
    return sum/len(L)
print(moyenne([1]))
# 1.0
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
# 4.0
print(moyenne([1, 2]))
# 1.5