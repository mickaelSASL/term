# **AMSER4 - Sécurisation des communications**

<center><img src="https://files.realpython.com/media/HTTPS-Fundamentals-with-Python_Watermarked.8da2b3c561b9.jpg" width="75%"></center>

<!-- <center><p style="font-style: italic;color=red;">Se connecter à votre compte office365 pour visualiser les vidéos</p></center> -->


<center><iframe width="560" height="315" src="https://www.youtube.com/embed/7W7WPMX7arI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>


<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/Ef6RXUX9zP9OrbaAvIgkoqsBs4Loq_rzaM8Y3kN0ix4Pzw?e=KiWbep" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>



===! "💾 Codage de César"
    ``` title="Communication réseau"
    1. Dans Spyder, ouvrir 2 onglets terminal.
    2. Dans le premier terminal, exécuter le programme `chat_client.py`
    3. Dans le second terminal, exécuter le programme `chat_serveur.py`
    
    4. Testez la communication 
    ```
    
=== "🐍 chat_client.py"
    ```python
    #!/usr/bin/env python3
    #  -*- coding: utf-8 -*-

    import socket ##### CLIENT UDP #####

    # Adresse et port du serveur :
    PORT = 12345 # N'importe quel port non réservé (> 1023)
    HOTE = "127.0.0.1" # <---Adresse du serveur, À ADAPTER À VOTRE SITUATION !! 
    sCli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    TAILLE_MAX_PAQUET = 1024 # Utile pour la réception uniquement.
    print("Saisir vos messages, suivi de [ENTRÉE].")
    print("Écrire FIN pour terminer, voire STOP pour arrêter aussi le serveur.\n")

    while 1 : # On envoie des
        msg = input("===(FIN / STOP pour terminer)==> ") # octets, donc on
        sCli.sendto(bytes(msg, encoding="utf8"), (HOTE,PORT)) # doit encoder
        # les chaînes...
        #### Facultatif : afficher l'accusé de réception #############
        paquet_recu, src = sCli.recvfrom(TAILLE_MAX_PAQUET)
        msg_recu = str(paquet_recu, encoding='utf-8')
        print("Serveur :", msg_recu)
        ##############################################################
        if msg == "FIN" or msg == "STOP" :
            sCli.close()
            print("Bye !")
            break
    ```

=== "🐍 Corrigé Q2"
    ```python
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
    ```


=== "🧩 Corrigé Q3"
    ### a. avec la méthode len()

    ```python
    def longueur(ma_liste):    
        return len(ma_liste)
    ```

    ### b. sans la méthode len()

    ```python
    def longueur(ma_liste):
        ct = 0    
        while ma_liste != []:
            ma_liste.pop()
            ct += 1
        return ct
    ```