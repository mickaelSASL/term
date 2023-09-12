import microbit as mb
from time import ticks_ms
import radio

# Initialisation des communications
mb.uart.init(115200)
radio.on()
radio.config(group=2)

NB_MICROBITS = 2
MAX_RETRY = 20
DELAI_MESURE = 10  # en secondes

retry = 0
tick_derniere_requete = 0
mb_requete = 0
en_attente = []

def lecture_boutons():
    """Lecture boutons"""
    if mb.button_a.was_pressed():
        mb.uart.write("FIN")

def lecture_radio():
    """Lecture signaux radio
    en provenance des capteurs MB"""
    radio_recu = radio.receive()
    if radio_recu:
        if radio_recu[0:3] == "CAP":
            # reception donnees d'un capteur
            en_attente.append(radio_recu[3:5])
            if radio_recu[3] in en_attente:
                # On a reçu la premiere donnee du capteur
                # On peut l'enlever de la liste d'attente
                en_attente.remove(radio_recu[3:4])
            # Transmission de l'info au PC
            mb.uart.write(radio_recu)

def lecture_serie():
    """Lecture messages en provenance du PC"""
    ser_recu = mb.uart.readline()
    if ser_recu:
        message = str(ser_recu, "utf-8")
        if message[0:3] == "ACK":
            # accuse de transmission capteur
            try:
                en_attente.remove(message[3:5])
            except:
                pass
        else:
            # Affichage message PC
            mb.display.show(message)

def envoi_requete():
    """Envoi d'une requete de capteur"""
    global mb_requete, retry, tick_derniere_requete

    if ticks_ms()-tick_derniere_requete < DELAI_MESURE*1000/NB_MICROBITS:
        # requete trop rapprochee, on ignore
        mb.sleep(100)
        return

    if len(en_attente) == 0:
        # pas de requete en attente, on passe au suivant
        capteur = chr(mb_requete+65)
        mb.display.show(capteur, wait=False)
        radio.send("REQ"+capteur)
        en_attente.append(capteur)
        mb_requete = (mb_requete+1) % NB_MICROBITS
        retry = 0
        tick_derniere_requete = ticks_ms()
    else:
        retry += 1
        mb.sleep(500)

    if retry > MAX_RETRY:
        # Quelque chose ne s'est pas bien passé
        # On vide la liste en attente
        mb.uart.write("Echec : "+str(en_attente))
        # suppression de la derniere requete
        en_attente.clear()
        retry = 0

#
# Boucle principale
#

while True:
    lecture_boutons()
    lecture_radio()
    lecture_serie()
    envoi_requete()