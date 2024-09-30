# 2022 -sujet 9 - ex1
# Écrire une fonction calcul prenant en paramètres un entier n strictement positif et qui renvoie la liste des valeurs un ,
#en partant de k et jusqu’à atteindre 1.
def calcul(k):
  resultat=[k]
  while k!=1:
    if k%2==0: 
      k=k//2
    else:
      k=3*k+1
    resultat.append(k)
  return resultat

print(calcul(7))