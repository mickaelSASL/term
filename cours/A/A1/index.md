# **A1 : Algorithme sur les arbres binaires**

<center><img src="https://files.realpython.com/media/How-to-Do-a-Binary-Search-in-Python_Watermarked.e06f21f5a58b.jpg" width="75%"></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EeTZNBY7yVdEukgJszaLP0MBIq4NP87n3sToFL6_m5W1VQ?e=sIiZGF" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EYQEiqmpy_1DkA-6xyvJJfIBZWt4Hzdmw3rqHqIkHZoVOQ?e=SV6fm4" target="_blank">Fiche de révision<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>


[Implémentation en Python](Algo_arbres.py)


===! "Algo à compléter"
      ```Python
      from binarytree import tree, Node

      def hauteur(T: tree):

      
      def taille(T: tree):
      

      def ParcoursLargeur(T: tree):
      
            

      def ParcoursPrefixe(T: tree):


      def ParcoursInfixe(T: tree):


      def ParcoursSuffixe(T: tree):
      
      def ArbreRecherche(T: tree, k: int):
      


      def ArbreInsertion(T: tree, y: Node):


      def ArbreInsertion_recursif(T: tree, y: Node):


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

      ```

=== "Algo complété"
      ```python
      --8<-- "term/cours/A/A1/Algo_arbres.py"
      ```

=== "Exemple d'exécution"
      ```pycon
       >>> print(A)


                        _________23___________
                       /                      \
                 _____14____               ____3___
                /           \             /        \
           ____3__           5           14        _1
          /       \         / \         /  \      /
         22        57      1   0      _1    27   64
        /  \      /       /          /
       1    86   0       8          34
      /
     0

      >>> hauteur(A)
      6
      
      >>> taille(A)
      20
      
      >>> ParcoursLargeur(A)
      23
      14
      3
      3
      5
      14
      1
      22
      57
      1
      0
      1
      27
      64
      1
      86
      0
      8
      34
      0
      ```