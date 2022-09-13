# Communication série

> *La liaison série va se faire au travers du cable USB. Il vous faut donc raccorder votre carte micro:bit au PC via un cable USB. Sous Windows votre carte va être raccordée via un port série avec un nom du type COM1,COM2,COM3,etc.*  
*Il vous faut savoir sous quel port votre carte micro:bit est raccordée.*  
*Pour cela, vous pouvez ouvrir une console Windows (cmd) puis de taper la commande `mode` : vous devriez voir apparaître le nom de votre port COM et son numéro.*  
*OU*  
*Ouvrir le gestionnaire de périphériques et dérouler la catégorie 'Ports (COM et LPT)'.*

## Communication µBit --> PC
![](série1.png)

===! "Programme µBit 1"

    ```{.python .extra-class #id linenums="1"}
    from microbit import *
    uart.init(baudrate=115200)
    display.scroll('Pret')

    msg_str="coucou"

    while not button_a.was_pressed():
        uart.write(msg_str + "\n")     # Ecriture du message
        sleep(1000)
        
    uart.write("$")	
    display.scroll("FIN") 
    ```

=== "Programme µBit 2"

    La méthode `print()` écrit directement sur le port série de la carte à la vitesse 115200.

    ```{.python .extra-class #id linenums="1"}
    from microbit import *
    display.scroll('Pret')

    msg_str="coucou"

    while not button_a.was_pressed():
        print(msg_str + "\n")     # Ecriture du message
        sleep(1000)
        
    print("$")	
    display.scroll("FIN") 
    ```

=== "Programme PC"

    > Le module `pyserial` est installé en exécutant dans la console python : ```pip install pyserial```  

    ```{.python .extra-class #id linenums="1"}
    import serial

    ser = serial.Serial(
        port='COM11',\
        baudrate=115200,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
            timeout=0)

    msg=""

    while msg!="$":             # Lecture du message
        for c in ser.read():    # Caractère par caractère
            msg = msg + chr(c)

            if chr(c) == '\n':  # Si le caractère '\n' (fin de ligne)
                print(msg)      # Affichage du message
                msg = ""
                break           # Stopper boucle FOR
            
    print("fin")
    ser.close()
    ```
=== "Programme PC 2"

    ```{.python .extra-class #id linenums="1"}
        ser.flushInput()
        time.sleep(0.1)
        line = ser.readline().rstrip().decode()
        tokens = line.split(':')
        if len(tokens)==2:
            print(str(count)+":"+tokens[0]+"-->"+tokens[1]+"["+line+"]")
        count +=1
    ```
    


## Communication PC --> µBit
![](série2.png)

===! "Programme µBit"

    ```{.python .extra-class #id linenums="1"}
        from microbit import *
        uart.init(baudrate=115200)
        display.scroll('Pret')

        msg_str=""

        while msg_str != "exit":
            if uart.any():
                display.scroll('Recu')
                msg_bytes = uart.read()             # Lecture du port série (message sous forme de Bytes)

                msg_str = str(msg_bytes, 'UTF-8')   # Conversion en chaine de caractères
                display.scroll(msg_str)             # Affichage du message
            sleep(1000)
            
        display.scroll("FIN") 
    ```
    

=== "Programme PC"

    > Le module `pyserial` est installé en exécutant dans la console python : ```pip install pyserial```  

    ```{.python .extra-class #id linenums="1"}
        import serial  # INSTALLER LE MODULE pyserial ( dans la console python : 'pip install pyserial')

        ser = serial.Serial(
            port='COM5',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)

        texte_message=""

        while texte_message != "exit":
            texte_message = input("Saisir le message : ")
            message_bytes = bytes(texte_message, 'utf-8')   # (message str converti en bytes)
            ser.write(message_bytes)                        # Ecriture d'un message sur le port série

        print("FIN")
        ser.close()
    ```

