# 2023 sujet 31 - ex2

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a
 

# Les Tests

for a in range(10):
    print(a,binaire(a))