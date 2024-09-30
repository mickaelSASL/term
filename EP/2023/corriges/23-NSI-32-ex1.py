# 2023 sujet 32 - ex1

def min_et_max(tab):
    d = {}
    d['min'] = tab[0]
    d['max'] = tab[0]
    for val in tab:
        if val < d['min']:
            d['min'] = val
        if val > d['max']:
            d['max'] = val
    return d
 
 
# Les Tests
tab=[1,2,9,9,0,6,99,6,-99,1,1]
print(tab,min_et_max(tab))