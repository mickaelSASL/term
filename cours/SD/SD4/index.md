# **SD4 : structure de données : Les Arbres**
<center><img src="https://files.realpython.com/media/How-to-Do-a-Binary-Search-in-Python_Watermarked.e06f21f5a58b.jpg" width="75%"></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EbUhHZaApMBJj3Sl0jkGAbABj-puonTICnyLa5cvXYWHkQ?e=oC8dCX" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EQoDih_vV-pGjVzKw4Pc1rUBKO7G0UqYbVycqOAr2VRs3g?e=MJtbUc" target="_blank">Exemple à compléter<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="exemple_corrigé.png" target="_blank">Exemple à compléter - corrigé![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a>


<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EZKNWz1nxShJtrL2I3aa0kUBYOgZ-RVrPJiynVBIo70u0w?e=ku5u3F" target="_blank">Exercices<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/ERN4aAhiQg9Ek7THbZDtbZgBrqwvyRFbs8gRbL7xq2YbkA?e=iLydrI" target="_blank">Exercices - Corrigé<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EbU0Uy6F_7pDsuZsdMnWju0B1XugXVLLOlBYX6NtpTrgwg?e=7H0yYp" target="_blank">Fiche de révision<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

## Implémentation POO
* Classe Arbres : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/ETBAVP-1mklEgq78DSTFoK0BTZAjNykRPIrBad45BGdxUg?e=RbJCVr" target="_blank">`Arbres.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>

* Module binarytree ([Site Web](https://pypi.org/project/binarytree/))
> **Installation**  
`pip install binarytree`
>
> **Utilisation**  
La classe de nœuds `Node` représente la structure d’un nœud particulier dans l’arborescence binaire. Les attributs de cette classe sont des valeurs, gauche, droite .
```Python
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (integer)
        self.left = left    # Left child
        self.right = right  # Right child
```
> **Exemples**  
Voir les exemples sur la documentation du site
Bloc Notes Jupyter, Codes Python
<a href="https://nbviewer.org/urls/mickaelsasl.github.io/T/cours/SD/SD4/Arbres.ipynb" target="_blank"><img src="/images/nbviewer_badge.svg"></a>
<a href="https://mybinder.org/v2/gh/mickaelSASL/mickaelSASL.github.io/HEAD?filepath=T/cours/SD/SD4/Arbres.ipynb" target="_blank"><img src="https://mybinder.org/badge_logo.svg"></a>


## Exercices

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EQHfbnCIYklDq4sBvC16-94B09I4IwPV9owX5bzXrnSSmg?e=YOJmDA" target="_blank">Exercice type BAC<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a></br>
<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EaEAODGpRdpLm4eDU59MtjsB06gbgVy25pELqBN2SCfWBQ?e=dNKTea" target="_blank">Exercice type BAC - Corrigé<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>


[TP - Morse](morse)