# Lemmings 🏃🏻🧍🚶🤸  

## Ressources possibles
### Gestion des touches du clavier
On peut utiliser la classe `GestionnaireEvenement` qui utilise la bibliothèque <a href="https://pypi.org/project/keyboard/" target="_blank">`keyboard`</a>, décrite ici.

 

### Gestion des tableaux
On peut stocker les tableaux de jeux dans un fichier texte *.txt*. Pour ouvrir et lire ce fichier, rien de tel que le module <a href="https://pypi.org/project/os/" target="_blank">`os`</a> et la structure `with … as …` .
 
 Vous pouvez consulter <a href="https://python.doctor/page-lire-ecrire-creer-fichier-python" target="_blank">cette page</a>.


### Gestion du temps

#### Avec le planificateur du module `Scheduler`

Cette solution est très simple à mettre en oeuvre. 

```Python
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()

def some_job():
    print "Every 10 seconds"

sched.add_interval_job(some_job, seconds = 10)

....
sched.shutdown()
```

#### Fonction auto-exécutée avec retard

Ici lors de l'exécution de la fonction appelée, elle se rappelle elle-même avec un retard paramétré. Cela crée une répétition à intervalle régulier.

```Python title="Paramétrage""
from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
```

```Python title="Utilisation"
from time import sleep

def hello(name):
    print "Hello %s!" % name

print "starting..."
rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
```


## Interface graphique

* <a href="http://math.univ-lyon1.fr/irem/Formation_ISN/formation_interfaces_graphiques/module_tkinter/exo_canevas.html" target="_blank">Exemple pour créer une grille avec Tkinter
![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a>
* <a href="https://ismvsectioninfo.wordpress.com/2020/09/21/digital-clock-poo-tkinter-gui-avec-sous-menu" target="_blank">Utiliser Tkinter avec la POO
![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a>
