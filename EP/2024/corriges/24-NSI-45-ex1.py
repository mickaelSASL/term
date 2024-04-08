# 24-NSI-45 Ex1
def compte_occurrences(x,tab):
    occ = 0
    for element in tab:
        if element == x:
            occ+=1
    return occ
print(compte_occurrences(5, [])
)
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print(compte_occurrences('a', ['a','b','c','a','d','e','a'])
)