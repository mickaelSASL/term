# 2022 - sujet 19 - ex2
def chercher(T, n, i, j):
    if i < 0 or j >= len(T) :
        print('Erreur')
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if T[m] < n :
        return chercher(T, n, m + 1, j)
    elif T[m] > n :
        return chercher(T, n, i, m - 1 )
    else :
        return m

(T, n, i, j)=([1,5,6,6,9,12],7,0,10)
print((T, n, i, j),chercher(T, n, i, j))

(T, n, i, j)=([1,5,6,6,9,12],7,0,5)
print((T, n, i, j),chercher(T, n, i, j))

(T, n, i, j)=([1,5,6,6,9,12],9,0,5)
print((T, n, i, j),chercher(T, n, i, j))

(T, n, i, j)=([1,5,6,6,9,12],6,0,5)
print((T, n, i, j),chercher(T, n, i, j))