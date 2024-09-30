#2022 - sujet 29 - ex1def fibonnaci(n):
def fibonnaci(n):
    d = {}
    d[1] = 1
    d[2] = 1
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]


n=1
print(n,fibonnaci(n))

n=2
print(n,fibonnaci(n))

n=25
print(n,fibonnaci(n))

n=45
print(n,fibonnaci(n))