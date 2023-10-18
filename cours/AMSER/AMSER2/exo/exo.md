# **AMSER2 -  Gestion des processus et des ressources par un système d’exploitation**

## Illustration de l'interblocage en Python

### Commençons par une simple fonction qui doit incrémenter 100 fois une variale compteur :

```Python
from time import sleep
 
compteur = 0 # Variable globale
limite = 100
 
def calcul():
    global compteur
    for c in range(limite):
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1
compteur = 0
calcul()
compteur

100
```

Sans surprises, la valeur de la variable compteur vaut 100. Vous remarquerez la manière dont l'incrémentation du compteur a été volontairement complexifié. La raison va apparaître maintenant car nous allons maintenant lancer 4 processus légers (appelés threads) qui vont tous les 4 exécuter la fonction calcul.

On pourrait imaginer que puisque `calcul` est exécuté 4 fois le résultat final sera 400. En réalité, il n'en est rien :

```Python

compteur = 0
for i in range(4): # Lance en parallèle 4 exécutions dd calcul
    p = Thread(target = calcul)
    p.start()      # Lance calcul dans un processus léger à part.
compteur

149
```

### Threads are evil, don't use them !
En réévaluant plusieurs fois l'exécution du calcul parallèle, on s'aperçoit que

1. le résultat n'est pas 400 !
2. d'une exécution à l'autre le résultat est différent !!

Voila qui est très perturbant : Un même programme - très simple - exécuté plusieurs fois qui ne donne pas le même résultat. Bienvenue dans le monde infernal des thread. Cela explique la réticence de certains à les utiliser : **Threads are evil, don't use them !** lit-on souvent sur les forums de développeurs...

Et pourtant ils sont nécessaires à bon nombre de tâches. Sans threads, pas de serveurs webs capables d'encaisser des millions de requêtes à la seconde !

### Explication
Il n'y a rien d'illogique ou d'aléatoire dans le fonctionnement de notre programme. Il faut simplement habituer notre esprit à l'exécution en parallèle :

- quatre processus (appelons les P1, P2, P3 et P4) exécutent la fonction calcul simultanément. Celle-ci utilise une variable globale qui sera donc modifiée par chacun de ces processus et une variable locale temp qui sera spécifique à chacun de nos processus. Nous la désignerons par temp(P1) temp(P2) etc... Un scénario possible est le suivant : Imaginons au départ que compteur vaille 10.

- P1 sauvegarde `compteur` dans temp(P1) --> temp(P1) vaut 10

- P2 sauvegarde `compteur` dans temp(P2) --> temp(P2) vaut 10
- P3 sauvegarde `compteur` dans temp(P3) --> temp(P3) vaut 10
- P1 et P2 incrémentent temp et sauvegardent la réponse dans `compteur` --> `compteur` vaut 11
- P4 sauvegarde `compteur` dans temp(P4) --> temp(P4) vaut 11
- P3 et P4 incrémentent temp et sauvegardent la réponse dans `compteur`

au final, `compteur` a été incrémenté 4 fois mais de fait de l'exécution en parallèle `compteur` ne vaut pas 14 mais 12 ! cela explique que notre compteur au final ne vaut pas 400 car sa sauvegarde dans des variables temporaires fait que la plupart des incrémentations ne sont pas prises en compte.

Quand au résultat apparemment aléatoire, il est du au scénario d'exécution. j'en ai cité un au hasard mais bien d'autres sont possibles qui mèneraient à des résultats différents. Un problème avec les threads est que l'on ne maîtrise pas du tout l'ordre dans lequel ils sont exécutés. Une fois lancés, chacun vit sa vie...

### Fiabiliser l'algorithme

Il est possible d'éviter que nos threads interfèrent les uns avec les autres : il suffit de s'assurer que la partie centrale qui incrémente notre compteur ne soit pas exécutée par 2 threads à la fois. Pour ce faire, on introduit la notion de **verrou**: un **verrou** peut être vu comme un témoin qui passe de thread en thread. Seul celui qui possède ce témoin peut exécuter l'incrémentation du compteur, les autres doivent attendre leur tour.

Nous allons donc légèrement modifier notre fonction `calcul` afin d'utiliser la partie critique de notre algorithme, à savoir l'incrémentation du compteur. Le module `threading` propose un objet `Lock()` destiné à cette tâche. Deux méthodes seront utilisées ici:

`verrou.acquire()` : attend que le vérrou soit libéré pour se l'accaparer et l'activer
`verrou.release()` : libère le verrou

from threading import Lock
verrou = Lock()
 
def calcul1():
    global compteur
    for c in range(limite):
        verrou.acquire()
        # Début de la section critique
        temp = compteur
        sleep(0.000000001)
        compteur = temp + 1
        # Fin de la section critique
        verrou.release()
Grâce à ce système, il est impossible que la partie critique du code soit exécutée simultanément par deux threads. On est donc assuré qu'il n'y aura pas d'interaction entre les threads.

Au final on constate bien que le le compteur vaut 400, ce qui est le résultat attendu.

En mémorisant les threads créés, on constate qu'ils se sont tous bien terminés.

compteur = 0
 
mes_threads = []
for i in range(4):
    p = Thread(target = calcul1)
    p.start()
    mes_threads.append(p)
compteur
400
mes_threads[0]
<Thread(Thread-20, stopped 140507816642304)>
mes_threads[0].is_alive()
False
Et l'interblocage ?
La situation d'interblocage ne peut pas arriver dans le scénario précédent car nous n'avons qu'un verrou donc une seule resssource convoitée par 4 threads : celle-ci va passer de threads en threads sans conflits. Pour faire apparaître l'interblocage, nous avons besoin de plusieurs verrous afin de créer une attente circulaire.

Nous allons donc créer 4 verrous : V0 V1 V2 et V3. La fonction calcul2 va utiliser deux verrous.

Le Thread P0 va donc réserver V0 puis V1
Le Thread P1 va donc réserver V1 puis V2
Le Thread P2 va donc réserver V2 puis V3
Le Thread P3 va donc réserver V3 puis V0
ces verrous seront libérés à la fin... sauf si le thread est en attente pour acquerir un verrou ! Et voilà une situation d'interblocage qui s'annonce...

def calcul2(verrou1, verrou2):
    global compteur
    for c in range(limite):
        verrou1.acquire()
        # Début de la section critique 1 
        temp = compteur
        sleep(0.000000001)
        # Début de la section critique 2
        verrou2.acquire()
        compteur = temp + 1
        # Début de la section critique 2
        verrou2.release()
        # Fin de la section critique 1
        verrou1.release()
compteur = 0
 
# On crée 4 verrous dans un tableau
verrous = [Lock() for i in range(4)] 
mes_threads = []
for i in range(4):
    p = Thread(target = calcul2, args = [verrous[i], verrous[(i+1)%4]])
    p.start()
    mes_threads.append(p)
compteur
1
mes_threads
[<Thread(Thread-24, started 140507833427712)>,
 <Thread(Thread-25, started 140507816642304)>,
 <Thread(Thread-26, started 140507841820416)>,
 <Thread(Thread-27, started 140507825035008)>]
On constate que tous les threads sont actifs et que le compteur ne s'incrémente pas. Nous sommes en situation d'interblocage !

Il n'y a pas d'autre choix que de tuer le processus Python et les threads afférents.