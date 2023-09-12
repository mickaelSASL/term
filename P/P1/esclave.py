# Ce programme gere l'envoi de données
# de capteurs vers le µBit maitre

import microbit as mb
import radio

radio.on()
radio.config(group=2)

NOM_MICROBIT = 'A'

def envoi_temperature():
    """Envoi de la temperature par radio"""
    NO_CAPTEUR = "1"
    temp = mb.temperature()
    message = "CAP"+NOM_MICROBIT+NO_CAPTEUR+str(temp)
    radio.send(message)
    print(message)

def lecture_radio():
    """Lecture des consignes par radio"""
    radio_recu = radio.receive()
    if radio_recu:
        print(radio_recu)
        if radio_recu[0:4] == "REQ"+NOM_MICROBIT:
            envoi_temperature()

#
# Boucle principale
#

while True:
    lecture_radio()