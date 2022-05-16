# -*- coding: utf-8 -*-

from binarytree import tree, Node, bst

def hauteur(T: tree):
    if T != None:
        return 1 + max(hauteur(T.left), hauteur(T.right))
    else:
        return 0
    
def taille(T: tree):
    if T != None:
        return 1 + taille(T.left) + taille(T.right)
    else:
        return 0

def ParcoursLargeur(T: tree):
    f = []
    f.append(T[0])
    
    while len(f) > 0:
        x = f.pop()
        print(x)
        if x.left != None:
            Tg = x.left
            f.insert(0, Tg[0])
        if x.right != None:
            Td = x.right
            f.insert(0, Td[0])
        

def ParcoursPrefixe(T: tree):
    if T != None:
        x = T[0]
        print(x.value)
        ParcoursPrefixe(x.left)
        ParcoursPrefixe(x.right)
        

def ParcoursInfixe(T: tree):
    if T != None:
        x = T[0]
        ParcoursInfixe(x.left)
        print(x.value)
        ParcoursInfixe(x.right)

def ParcoursSuffixe(T: tree):
    if T != None:
        x = T[0]
        ParcoursSuffixe(x.left)
        ParcoursSuffixe(x.right)
        print(x.value)

def ArbreRecherche(T: tree, k: int):
    if T == None:
        return False
    x = T[0]
    if k == x.value:
        return True
    if k < x.value:
        ArbreRecherche(x.left, k)
    else:
        ArbreRecherche(x.right, k)


def ArbreInsertion(T: tree, y: Node):
    x = T[0]
    while T != None:
        x = T[0]
        if y.value < x.value:
            T = x.left
        else:
            T = x.right
    if y.value < x.value:
        x.left = y
    else:
        x.right = y
   
def ArbreInsertion_recursif(T: tree, y: Node):
    if T == None:
        return y
    x = T[0]
    if y.value < x.value:
        return Node(value=x.value,
                    left=ArbreInsertion(x.left, y),
                    right=x.right)
    else:
        return Node(value=x.value,
                    left=x.left,
                    right=ArbreInsertion(x.right, y))

# Arbre pour tester
A = Node(23)
B = Node(14)
C = Node(3)
D = Node(22)
E = Node(1)
F = Node(0)
G = Node(86)
H = Node(57)
I = Node(0)
J = Node(5)
K = Node(1)
L = Node(8)
M = Node(0)
N = Node(3)
O = Node(14)
P = Node(1)
Q = Node(34)
R = Node(27)
S = Node(1)
T = Node(64)

A.left = B
A.right = N
B.left = C
B.right = J
C.left = D
C.right = H
D.left = E
D.right = G
E.left = F
H.left = I
J.left = K
J.right = M
K.left = L
N.left = O
N.right = S
O.left = P
O.right = R
P.left = Q
S.left = T


print(A)
ParcoursLargeur(A)