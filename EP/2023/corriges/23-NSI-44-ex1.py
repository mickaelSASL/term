# 2023 sujet 44 - ex1

def renverse(mot):
    sol = ''
    for lettre in mot:
        sol = lettre + sol
    return sol
 
 
# Les Tests

print(renverse("informatique"))
