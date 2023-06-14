# micro:bit IoT v0.1
# Olivier Lecluse
# Novembre 2019

# Ce programme est a l'ecoute de la MB maitre

import serial
import serial.tools.list_ports as list_ports
import time
import json

# Detection automatique de la carte MB
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1
JSON_FICHIER = 'data.json'


def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

def lecture_json():
    with open(JSON_FICHIER, 'r') as mon_fichier:
    	return json.loads(mon_fichier.read())
    
def ecrire_json(donnees):
    with open(JSON_FICHIER, 'w') as mon_fichier:
    	json.dump(donnees, mon_fichier)



#
# Programme principal
#

#ecrire_json({})
run = True

while run:
    # Boucle d'attente MB
    print('Detection microbit')
    mb_serie = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not mb_serie:
        print('microbit absente')
        time.sleep(1000)
    else:
        
        mb_serie.open()
        
        #
        # boucle principale
        #
    

        while run:
            # Atttente d'une consigne du maitre
            data = mb_serie.readline().decode('utf-8')
            if data:

                if data[0:3] == "FIN" :
                    run = False
                elif data[0:3] == "CAP":
                    # Reception d'un capteur
                    print("Capteur ", data[3:])
                    print(data[3:])
                    
                    # Mise a jour du fichier json
                    capteur_id = data[3]
                    donnees=lecture_json()
                    donnees[f'capteur{capteur_id}']['valeur']=data[5:]
                    ecrire_json(donnees)
                    
                    # Accuse de reception
                    accuse = "ACK"+data[3:5]
                    mb_serie.write(accuse.encode("utf-8"))
                    print(accuse)

mb_serie.close()             