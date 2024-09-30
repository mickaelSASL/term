# 2023 sujet 39 - ex1

# Une solution impérative

def fibonacci1(n):
    a = 1
    b = 1
    for k in range(n-2):
        t = b
        b = a + b
        a = t
    return b

# Une autre version

def fibonacci2(n):
    assert n>0
    d = {}
    d[1] = 1
    d[2] = 1
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]

# Une solution récursive
# peut efficace car limitée à n= 44
def fibonacci3(n):
    if n == 1 :
        return 1   
    elif n == 2 :
        return 1
    else :
        return fibonacci3(n-1) + fibonacci3(n-2)


# Les Tests

n=1
print(f'fibonacci1({n})={fibonacci1(n)}')
print(f'fibonacci2({n})={fibonacci2(n)}')
print(f'fibonacci3({n})={fibonacci3(n)}')
print('-------------------------')
n=5
print(f'fibonacci1({n})={fibonacci1(n)}')
print(f'fibonacci2({n})={fibonacci2(n)}')
print(f'fibonacci3({n})={fibonacci3(n)}')
print('-------------------------')
n=10
print(f'fibonacci1({n})={fibonacci1(n)}')
print(f'fibonacci2({n})={fibonacci2(n)}')
print(f'fibonacci3({n})={fibonacci3(n)}')
print('-------------------------')
n=44
print(f'fibonacci1({n})={fibonacci1(n)}')
print(f'fibonacci2({n})={fibonacci2(n)}')
print(f'fibonacci3({n})={fibonacci3(n)}')
print('-------------------------')