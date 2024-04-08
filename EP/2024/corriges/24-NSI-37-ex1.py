# 2024 NSI sujet 37 - ex 1

def moyenne(tab):
    if tab == []:
        print('Le tableau donné est vide')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)
    
print(moyenne([5,3,8])) #5.333333333333333
print(moyenne([1,2,3,4,5,6,7,8,9,10]))#5.5
print(moyenne([])) #None