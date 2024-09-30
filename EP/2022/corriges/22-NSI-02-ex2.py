# 2022 Sujet 2 ex 2
def pascal(n):
    C = [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

print(pascal(4))

print(pascal(5))