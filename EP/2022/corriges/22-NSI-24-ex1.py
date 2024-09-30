#2022 - sujet 24 - ex1
def maxliste(tab):
    maximum = tab[0]
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

print(maxliste([98, 12, 104, 23, 131, 9]))
print(maxliste([-27, 24, -3, 15]))
print(maxliste([-27, 24, -3, 150]))
print(maxliste([500, 24, -3, 15]))