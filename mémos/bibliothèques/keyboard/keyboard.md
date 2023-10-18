---
hide:
    - toc
---    

# ⌨️ Keyboard ⌨️ 

> `keyboard` est un module à installer permettant de gérer les claviers.
> 
> Il gère totalement le clavier :  
> - détecter tous les évènements,  
> - enregistrez des raccourcis clavier,  
> - simulez l'appui des touches touches,  
> - …  
 

## Installation
La documentation du module `keyboard` est disponible <a href="https://pypi.org/project/keyboard/" target="_blank">ici</a>.

Depuis une fenêtre de commande ou un terminal, ou encore certains IDE comme pyzo :

```Python
pip install keyboard
``` 

## Utilisation
L’utilisation la plus courante est de créer un gestionnaire d’écoute d’événement (*hook event handler* ou *event listener handler*) : à chaque événement sur une touche (pressée, relâchée, …) une routine (appelée `callback`) est exécutée.

Plusieurs types d’événements peuvent être écoutés, à l'aide des fonctions suivantes :

* appui sur une touche : `on_press_key`
* relâchement d’une touche : `on_release_key`
* appui ou relâchement d’une touche : `hook_key`
Pour tous ces évènements, il est nécessaire d'indiquer la touche écoutée.

Pour une écoute de n'importe quelle touche, on utilisera :
* appui sur une touche quelconque : `on_press`
* relâchement d’une touche quelconque : `on_release`
* appui ou relâchement d’une touche quelconque : `hook`

!!! info
    Dans tous les cas, il faut préciser le nom de la fonction à exécuter lorsque l’événement se produira.


!!! warning
    À la fin du programme, il est important de libérer tous les gestionnaires d'écoute d'événements : `unhook_all`

!!! info 
    <a href="https://github.com/boppreh/keyboard#api" target="_blank">API complète</a>

 

## Exemples
### Utilisation dans un programme
Dans un programme, on peut utiliser le module `keyboard` « autour » d’un boucle « infinie ».

```Python title="Exemple dans un programme"
import keyboard
import time
run = True

def action_clavier(event):
    global run
    if event.name == 'q':
        run = False
    # les actions à réaliser suite à un appui sur une touche
    # .......

# On initialise l'écouteur d'événements clavier (ici : appui sur une touche)
keyboard.on_press(action_clavier)

while run:
    time.sleep(1)
    # les actions à réaliser périodiquement
    # .......
# On arrêter l'écouteur d'événements clavier
keyboard.unhook_all()
``` 

 

### Utilisation dans une classe
On peut également utiliser un gestionnaire d’événement sous la forme d’un objet utilisé par une classe parente.

```Python title="Exemple dans une classe"
import keyboard
class GestionnaireEvenements:
    def __init__(self, parent = None):
        # Classe qui exploite de gestionnaire d'événement
        self.parent = parent
        # On initialise l'écouteur d'événements clavier (ici : appui sur une touche)
        keyboard.on_press(self.action_clavier)

    def __del__(self):
        """ Méthode appelée automatiquement à la destruction de l'objet
            nécessaire pour arrêter l'écouteur d'événements clavier
        """
        keyboard.unhook_all()
    
    def action_clavier(self, event):
        """ Callback lancé à chaque appui sur une touche
        """
        if self.parent is not None:
            # On renvoie l'action à la classe parente
            self.parent.action_clavier(event.name) 
        else:
            print(event.name)
            
if __name__=="__main__":
    import time
    e = GestionnaireEvenements()
    while True:
        time.sleep(5)
```

!!! note
    Remarque : la classe parente, doit posséder une méthode `action_clavier` qui attend un argument de type `event.name` (type `str`). C’est cette classe qui doit s’occuper de détruire (instruction `del`) son gestionnaire d’événement afin de retrouver l’usage du clavier !