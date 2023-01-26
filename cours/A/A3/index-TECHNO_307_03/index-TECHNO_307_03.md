---
hide:
  - navigation
  - toc
---

# **A3 : Méthode Diviser pour Régner**

<center><img src="https://files.realpython.com/media/The-Python-Sort-Function-Guide_Watermarked.394963ad7eff.jpg" width="75%"></center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EXWcfiFq-DBPgSVf9BIS8DEBG1ukQzyZuK4MIpuPs82RHQ?e=UxfDHO" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>

[Exercices](exo.md)

## Tri-Fusion

<tab>
    <tr>
        <td>
            ![](tri-fusion.jpg)
        </td>
        <td>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/OEmlVnH3aUg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </td>
    </tr>
</tab>

## B. Tri-Fusion
### 5. Implémentation en Python

===! "Diviser"
    ```Python
    def diviser(l):
        long = len(l)
        return l[:long//2], l[l//2:]
    ```

===! "Combiner"
    ```Python
    def combiner(gauche,droite):
        resultat = []
        while len(gauche) > 0 and len(droite) > 0:  
            if gauche[0] < droite[0]:
                resultat.append(gauche[0])
                gauche = gauche[1:]
            else:
                resultat.append(droite[0])
                droite = droite[1:]
        if len(gauche) == 0:
            resultat = resultat + droite
        else:
            resultat = resultat + gauche
        return resultat

    ```

===! "Tri-Fusion"
    ```Python
    def tri_fusion(l):

    ```


## C. Rotation d'une image

<tab><tr><td>![](fichiers/R2D2.jpg)</td><td>![](fichiers/vador.jpg)</td></tr></tab>

```python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def rotate(image):
    n = len(image)
    if n > 1:
        temp = np.copy(image[n//2:, :n//2])
        image[n//2:, :n//2] = rotate(image[n//2:, n//2:])
        image[n//2:, n//2:] = rotate(image[:n//2, n//2:])
        image[:n//2, n//2:] = rotate(image[:n//2, :n//2])
        image[:n//2, :n//2] = rotate(temp)
    return image


image = np.array(Image.open('R2D2.jpg'))
image = rotate(image)
plt.imshow(image)
```

En itératif
```Python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def rotate(image):
    n = len(image)
    result = np.copy(image)
    for i in range(n//2):
        for j in range(n//2):
            # partie à compléter pour déplacer
            # les pixels des quatre quadrants
            
    return result


image = np.array(Image.open('vador.jpg'))
image = rotate(image)
plt.imshow(image)
```
___


![](rotation repères.png)