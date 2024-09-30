# 2022 Sujet 5 ex 1
def rechercheMinMax(tab):
    if tab == []:
        return {'min': None, 'max': None}
    d = {}
    d['min'] = tab[0]
    d['max'] = tab[0]
    for val in tab:
        if val < d['min']:
            d['min'] = val
        if val > d['max']:
            d['max'] = val
    return d

# tests
tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
print(rechercheMinMax(tableau))

tableau = []
print(rechercheMinMax(tableau))