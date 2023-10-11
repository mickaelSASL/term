# Lemmings 🏃🏻🧍🚶🤸  

## Gestion des tableaux
On peut stocker les tableaux de jeux dans un fichier texte *.txt*.

## Amélioration de l’affichage

### Affichage dans une fenêtre séparée
Pour avoir un affichage correct il sera surement nécessaire de lancer le programme à partir de la ligne de commande :

* > Dans l'invite de commande Windows (`cmd.exe`) :
        ```Shell title=""
        python3 JeuDeLaVie.py
        ```

OU plus simple

* > Dans Spyder : `Run \ Configuration per file...` :
        Modifiez comme ceci :
        ![](img/config_spyder.png)  
        Spyder exécutera désormais le fichier dans une invite de commande windows où les éléements s'afficheront grâce la fonction `print()`.



### Avec des caractères plus complets
L'affichage pourra être améliorer en modifier les caractères utilisés pour construire la carte █ pour les murs par exemple.
 

### Avec des couleurs
Ajout de la couleur à l'aide de plusieurs méthodes :

```python title="Méthode d'utilisation des couleurs"
class bcolors: 
    VIOLET = '\033[95m' 
    BLEU = '\033[94m' 
    CYAN = '\033[96m' 
    VERT = '\033[92m' 
    JAUNE = '\033[93m' 
    ROUGE = '\033[91m' 
    ENDC = '\033[0m' 
    BOLD = '\033[1m' 
    UNDERLINE = '\033[4m' 
    
print(f"Voici un {bcolors.ROUGE}texte{bcolors.ENDC} {bcolors.BOLD}avec{bcolors.ENDC} des {bcolors.BLEU}couleurs{bcolors.ENDC}")
```

> *Remarque : fonctionne avec certains terminaux seulement (pas avec l’IDLE de Python, ni avec Pyzo, mais avec VSCode)*
Ou bien utiliser une bibliothèque, comme [termcolor](https://pypi.org/project/termcolor/).

 

### Avec des cases de plusieurs caractères
…

### Implémenter une classe pour gérer l’interface utilisateur
…

### Affichage graphique
…