# **AMSER4 - Sécurisation des communications**

<center><img src="https://files.realpython.com/media/HTTPS-Fundamentals-with-Python_Watermarked.8da2b3c561b9.jpg" width="75%"></center>

<!-- <center><p style="font-style: italic;color=red;">Se connecter à votre compte office365 pour visualiser les vidéos</p></center> -->

## [Introduction](Intro.html)



<iframe width="560" height="315" src="https://www.youtube.com/embed/7W7WPMX7arI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/Ef6RXUX9zP9OrbaAvIgkoqsBs4Loq_rzaM8Y3kN0ix4Pzw?e=KiWbep" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>


[Chat-Serveur](chat_serveur.py)

[Chat-Client](chat_client.py)


Sujet pratique - Exo2.py
```Python
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
resultat = ''
    for ... in message :
        if lettre in ALPHABET :
            indice = ( ... )%26
            resultat = resultat + ALPHABET[indice] 
        else:
            resultat = ...
    return resultat

```


<!-- 
## Fichiers Filius
<img src="exemple.png">
<a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EYCMNcnZa_hKrHwsWtyLCRYBlJckmoKgjRx2ZQLpYxpU3Q?e=2MYLS2" target="_blank">Exemple du cours.fls<img src="\images\filius.png" width="32px"></a>

<img src="Exo3.png">
<a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EV4zFiIUprRKoKylAt0lUWkB5ddhkPBFzbnRIRyOytWzvQ?e=b0VmGO" target="_blank">Exo3.fls<img src="\images\filius.png" width="32px"></a>
[Exo3 - Corrigé](exo3_corrige.md) -->