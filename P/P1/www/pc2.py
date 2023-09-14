# -*- coding: UTF-8 -*-
import serial
import serial.tools.list_ports as list_ports
import time
import cgitb
import sys
import codecs
import json


# Detection automatique de la carte MB
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

# Fichier JSON
JSON_FICHIER = 'data.json'


def find_comport(pid, vid, baud):
    ''' Recherche du port série et connexion à la carte microbit maitre '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    for p in ports:
        try:
            pass
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            ser_port.port = str(p.device)
            return ser_port
    return None


def lecture_json():
    """
    Lit le contenant JSON du fichier et le convertit en dictionnaire

    Returns
    -------
    Dict
        Données JSON lues.

    """
    with open(JSON_FICHIER, 'r') as mon_fichier:
    	return json.loads(mon_fichier.read())
    
def ecrire_json(donnees):
    """
    Convertit un dictionnaire en flux json et l'écrit dans le fichier.

    Parameters
    ----------
    donnees : dictionnaire contenant les données JSON.

    Returns
    -------
    None.

    """
    with open(JSON_FICHIER, 'w') as mon_fichier:
    	json.dump(donnees, mon_fichier)

#
# Programme principal
#

############################################
# CODE HTML page d'attente
############################################
print ("Content-type:text/html\r\n\r\n")
print('<!DOCTYPE html>')
print ('<html>')

print("EN CHARGEMENT")
run=True

############################################
# Boucle d'attente de la carte µbit
############################################

while run:
	mb_serie = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
	if not mb_serie:
		time.sleep(1000)
	else:
		mb_serie.open()
		run=False


##############################################
# CODE HTML affichage des températures
# le code est importé d'un fichier externe
# la mise à jour des valeurs est automatique 
##############################################
print ("Content-type:text/html\r\n\r\n")
print('<!DOCTYPE html>')

#ici débute le contenu du <HTML> provenant du fichier 'temperatures.html'
with open('temperature.html', 'r') as mon_fichier:
	print(mon_fichier.read())

#fin de la page
print("FIN")
print ('</html>')



run=True
while run:
	# Atttente d'une consigne du maitre
	data = mb_serie.readline().decode('utf-8')

	if data:
		if data[0:3] == "FIN" :
            # Appui sur le bouton B de la carte maitre
			...
		elif data[0:3] == "...":
			# Reception d'un capteur
			
			# Mise a jour du fichier json
			capteur_id = ...
			donnees = ...
			...
			ecrire_json(...)
			
			# Accuse de reception
			accuse = "ACK"+data[3:5]
			mb_serie.write(accuse.encode("utf-8"))

mb_serie.close()	


