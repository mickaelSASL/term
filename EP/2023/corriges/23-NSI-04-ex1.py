# 2023 sujet 4 - ex1


def a_doublon(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

# Les Tests

print(a_doublon([]))
print(a_doublon([1]))

print(a_doublon([1, 2, 4, 6, 6]))

print(a_doublon([2, 5, 7, 7, 7, 9]))

print(a_doublon([0, 2, 3]))

