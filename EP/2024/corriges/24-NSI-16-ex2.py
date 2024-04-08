# NSI pratique 2024 sujet 16 - ex2

def tri_bulles(T):
    '''
    Renvoie le tableau T triÃ© par ordre croissant
    '''
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
 

# Les Tests
T=[]
print(T,tri_bulles(T))
print('-------------------------')
T=[7]
print(T,tri_bulles(T))
print('-------------------------')
T=[9, 3, 7, 2, 3, 1, 6]
print(T,tri_bulles(T))
print('-------------------------')
T=[9, 7, 4, 3]
print(T,tri_bulles(T))
print('-------------------------')