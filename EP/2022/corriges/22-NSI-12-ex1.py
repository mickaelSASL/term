# 2022 -sujet 12 - ex1
#Programmer la fonction moyenne prenant en paramètre un tableau d'entiers tab (type list)
#qui renvoie la moyenne de ses éléments si le tableau est non vide et affiche 'erreur' si le tableau est vide.
def moyenne(tab):
    if tab == []:
        print('erreur')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)

# on utilise la fonction um(tab)/len(tab) pour les tests
tab=[-10,10]
print(moyenne(tab),sum(tab)/len(tab))

tab=[]
print(moyenne(tab))

tab=[-100,50,20,30,60,148,1]
print(moyenne(tab),sum(tab)/len(tab))