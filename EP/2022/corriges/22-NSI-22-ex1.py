#2022 - sujet 22 - ex1
def renverse(mot):
    sol = ''
    for lettre in mot:
        sol = lettre + sol
    return sol

print(renverse("informatique"))