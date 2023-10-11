# 🐧🐧 OS 🐧🐧

> Le module `os` est une bibliothèque standard qui permet de travailler avec le système d'exploitation.
> 
> Le module `os`` en Python est un outil très utile pour :  
- effectuer des opérations avec le système d'exploitation,  
- pour travailler avec des fichiers, des répertoires, des processus, des utilisateurs, des chemins de fichiers et de répertoires,  
- obtenir des informations sur le système d'exploitation.

La documentation est consultable <a href="https://docs.python.org/fr/3/library/os.html" target="_blank">ici</a>.


## Installation
Le module `os` est un module Python, il n'a pas besoin d'être installé. Il peut être chargé simplement avec la commande :
```Python title="Utilisation"
import os
```

## Utilisation

Le module `os` a de multiples utilisations, voici les plus courantes qui pourront vous être utiles.

### `os.getlogin()`

Le module `os` permet récuperer le nom d'utilisateur du système d'exploitation facilement via la méthode `os.getlogin()` qui renvoie le nom d'utilisateur courant.

```Python title="Exemple"
import os
user = os.getlogin()
print(user) # affiche le nom d'utilisateur
```
___

### `os.mkdir()`
Parmis ces fonction, le module `os` permet aussi de créer un répertoire selon le chemin spécifié. `os.mkdir(chemin)` crée un répertoire correspondant au chemin spécifié.

```Python title="Exemple : création d'un dossier à la racine du disque C:\"
import os
os.mkdir("c:/myFolder") # crée un dossier nommé 'myFolder' sur le disque C:\
```
___

### `os.getcwd()`
`os.getcwd()` renvoie le répertoire actuel sous forme de chaîne de caractères.

```Python title="Exemple"
import os
rep_actuel = os.getcwd()
print(rep_actuel) # renvoie le répertoire actuel
```
___

### `os.path()`
Afin de pouvoir utiliser la méthode `os.path()`, il faut préalablement importer le module `pathlib`. Le module `pathlib` est un module doté d'une interface orientée objet inclus dans python depuis la version 3.4 doté de méthodes très intuitives permettant d'interagir avec le système de fichiers d'une façon simple et conviviale.

#### 1. Tester si un répertoire existe avec la méthode `os.path.exist()`
La méthode `os.path.exist()` permet de tester si un répertoire existe ou non

```Python title="Exemple. tester l'existence d'un répertoire"
import os
from pathlib import Path
print(os.path.exists("c:/users/"))
#affiche True
#---------------------------
# On peut aussi utiliser
print(not os.path.exists("c:/users/"))
#affiche False
```

#### 2. Tester si un chemin est un répertoire ou un fichier avec les méthodes `is_dir()` et `is_file()`
Pour tester la nature d'un chemin s'il s'agit d'un répertoire ou un fichier on utilise les méthodes `is_dir()` et `is_file()`:

```Python title="Exemple"
import os
from pathlib import Path
myDirectory = "C:/Users"
p = Path(myDirectory)
print(p.is_dir()) # affiche True
print(p.is_file()) # affiche False
Exemple
import os
from pathlib import Path
myDirectory = "C:/Windows/system.ini"
p = Path(myDirectory)
print(p.is_dir()) # affiche False
print(p.is_file()) # affiche True
```

#### 3. Détrmination du chemin absolu à l'aide de la méthode `absolute()`
La méthode `absolute()` renvoie le chemin absolu du fichier qui contient le code python. Nous allons faire un petit test en créant un fichier python qui contient le code ci dessous et l'enregistrer sur le bureau :

```Python title="Exemple"
#absolute path
import os
from pathlib import Path
myDirectory = "."
p = Path(myDirectory)
print(p.absolute())
# Affiche : "C:\Users\acer\Desktop"
```
#### 4. Transformer un chemin en adresse uri avec la méthode `as_uri()`
La méthode `as_uri()` est utilisée pour transformer un chemin en uri (uniforme ressource identifier)

```Python title="Exemple"
from pathlib import Path
myDirectory = "C:/Users/Public/Videos/Sample Videos/Wildlife.wmv"
p = Path(myDirectory)
print(p.as_uri())
# Affiche : file:///C:/Users/Public/Videos/Sample%20Videos/Wildlife.wmv
```

#### 5. Obtenir le chemin du dossier parent avec la méthode parent
La méthode `parent()` permet de renvoyer le dossier parent d'un dossier existant :

```Python title="Exemple: dossier parent"
from pathlib import Path
myDirectory = "C:/Users/Public/"
p = Path(myDirectory)
print(p.parent) # Affiche 'C:\Users'
# parent renvoie aussi le dossier parent d'un fichier
myDirectory = "C:/Users/Public/Videos/Sample Videos/Wildlife.wmv"
p = Path(myDirectory)
print(p.parent) # Affiche 'C:\Users\Public\Videos\Sample Videos'
```
#### 6. Récuperation du contenu d'un dossier avec la méthode scandir() appliquée à la méthode Path()
En appliquant la méthode `scandir()` à la méthode `Path()`, on peut obtenir le contenu d'un dossier :

```Python title="Exemple: récupération du contenu du répertoire 'C:/Users'"
from pathlib import Path
import os
myDirectory="c:/users"
p = Path(myDirectory)
for x in os.scandir(p):
    print(x)
 
"""
output:
<DirEntry 'All Users'>
<DirEntry 'Default'>
<DirEntry 'Default User'>
<DirEntry 'dell'>
<DirEntry 'desktop.ini'>
<DirEntry 'Public'>
"""
```


#### 7. Afficher tous les fichiers d'une extension spécifique via la méthode glob()
La méthode `os.glob()` est l'une des méthodes de l'objet `Path` permettant d'afficher la liste des fichiers d'une extension donnée :

```Python title="Exemple: affichage des bibliothèques .dll du répertoire ' C:/Windows '"
from pathlib import Path
p = Path('C:/Windows/')
for f in list(p.glob('**/*.dll')):
	print(f)
 
"""
output:
Affiche tous les fichiers dont d'extension .dll du répertoire 'C:/Windows/'
"""
```
___



## Récapitulatif des méthodes associées au module `os`
Voici un récapitulatif des méthodes les plus couramment utilisées associées au module `os` en Python:

`os.name`: renvoie le nom du système d'exploitation sous-jacent.  
`os.environ`: renvoie un dictionnaire contenant les variables d'environnement du système.  
`os.getcwd()`: renvoie le répertoire de travail actuel.  
`os.chdir(path)`: change le répertoire de travail actuel en path.  
`os.listdir(path)`: renvoie une liste des fichiers et répertoires dans le répertoire spécifié par path.  
`os.mkdir(path)`: crée un nouveau répertoire avec le nom path.  
`os.rmdir(path)`: supprime le répertoire vide spécifié par path.  
`os.remove(path)`: supprime le fichier spécifié par path.  
`os.path.exists(path)`: renvoie `True` si path existe, sinon `False`.  
`os.path.isdir(path)`: renvoie `True` si path est un répertoire, sinon `False`.  
`os.path.isfile(path)`: renvoie `True` si path est un fichier, sinon `False`.  
`os.path.join(path1, path2, ...)`: combine plusieurs chemins en un seul chemin complet.  
`os.path.basename(path)`: renvoie le nom de base du chemin spécifié.  
`os.path.dirname(path)`: renvoie le répertoire parent du chemin spécifié.  
`os.path.abspath(path)`: renvoie le chemin absolu du chemin spécifié.  
`os.path.split(path)`: divise un chemin en deux parties: le répertoire parent et le nom de fichier.  
`os.path.splitext(path)`: divise un chemin en deux parties: le nom de fichier et l'extension de fichier.  
`os.chmod(path, mode)`: modifie les permissions du fichier ou du répertoire spécifié.  
`os.rename(src, dst)`: renomme le fichier ou le répertoire spécifié.  
`os.system(command)`: exécute une commande dans un sous-shell.  
`os.popen(command)`: ouvre un processus pour exécuter une commande.  
`os.getpid()`: renvoie l'identifiant de processus du processus courant.  
`os.kill(pid, signal)`: envoie le signal spécifié au processus spécifié.  
`os.getlogin()`: renvoie le nom d'utilisateur de l'utilisateur courant.  
`os.getuid()`: renvoie l'identifiant de l'utilisateur courant.  
`os.getgid()`: renvoie l'identifiant du groupe d'utilisateurs courant.  
`os.setuid(uid)`: change l'identifiant de l'utilisateur courant.  
`os.setgid(gid)`: change l'identifiant du groupe d'utilisateurs courant.  

!!! warning
    Noter bien que ce ne sont pas toutes les méthodes associées au module `os`, mais seulement les plus couramment utilisées. Il existe de nombreuses autres méthodes disponibles pour travailler avec des fichiers, des répertoires, des processus, des utilisateurs et des chemins de fichiers et de répertoires.
    Pour plus de détails sur le module `Path` voir la <a href="https://docs.python.org/fr/3/library/os.path.html" target="_blank">documentation officielle</a>.