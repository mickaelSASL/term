# 24-NSI-43 Ex1
def a_doublon(tab):
    if len(tab)>=2:
        for i in range(1,len(tab)): #teste si le tableau est triee
            if tab[i-1]>tab[i]:
                return False
        for i in range(len(tab)):
            for j in range(1,len(tab)):
                if tab[i] == tab[j] and i!=j:
                    return True
    return False
print(a_doublon([])
)
print(a_doublon([1])
)
print(a_doublon([1, 2, 4, 6, 6]))
print(a_doublon([2, 5, 7, 7, 7, 9])
)
print(a_doublon([0, 2, 3]))