# 2022 sujet 34 - ex2
def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) #

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0]) #

def negatif(image):
    '''renvoie le negatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
# on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(nbCol(image)): #
            L[i][j] = 255-image[i][j] #
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inferieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(nbCol(image)): 
            if image[i][j] < seuil :
                # On applique l'algorithme donné en commentaire :
                #le pixel est mis à 0 s'il est inférieur au seuil et à 1 sinon.
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img,120))
 