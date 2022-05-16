# coding: utf-8

#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import socket ##### SERVEUR UDP #####

HOTE = "127.0.0.1" # <---Adresse IP À ADAPTER À VOTRE SITUATION ex. 'localhost' en local
PORT = 12345 # N'importe quel port non réservé (> 1023)
TAILLE_MAX_PAQUET = 1024
sSrv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # On crée le socket
sSrv.bind((HOTE,PORT)) # On l'associe à un couple (adresse_IP ; port)
print("Serveur en attente de message, sur le port", HOTE)
print("Saisir STOP sur un client pour arrêter le serveur.\n")
while 1 :
   paquet, source = sSrv.recvfrom(TAILLE_MAX_PAQUET)    # Réception du paquet (octets)
   msg_recu = str(paquet, encoding='utf-8')             # transformé en chaîne
   
   # /!\ On reçoit des octets, à re-coder ici en texte !
   print("↳ Reçu du client d'IP", source[0], "sur le port", source[1], ":", msg_recu)
   # Là aussi, source = (adresse_IP , port)
   

   #########################################################################
   # /!\ Idem ici, on a converti : chaîne msg --> octets à envoyer
    
   if msg_recu == "STOP" :
        sSrv.close()
        print("Message 'STOP' reçu, serveur arrêté !")
        break   
    
   #### Facultatif : envoi d'accusé de réception ###########################
   message = input(">> ")
   sSrv.sendto(bytes(message, encoding="utf8"), (source[0], source[1]))