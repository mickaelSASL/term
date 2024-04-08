# NSI pratique 2024 sujet 19 - ex1

def liste_puissances(a,n):
    puissances = [a]
    for i in range(n-1):
        puissances.append(puissances[-1] * a)
    return puissances

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst

# Tests
(a,n)=3,5
print((a,n),liste_puissances(a,n))
(a,n)=-2,5
print((a,n),liste_puissances(a,n))
(a,n)=2,16
print((a,n),liste_puissances_borne(a,n))
(a,n)=2,17
print((a,n),liste_puissances_borne(a,n))
(a,n)=5,5
print((a,n),liste_puissances_borne(a,n))
 