# 2024 NSI sujet 33 - ex 1

def renverse(mot):
    sol = ''
    for lettre in mot:
        sol = lettre + sol
    return sol

print(renverse(""))
print(renverse("abc"))
print(renverse("informatique"))