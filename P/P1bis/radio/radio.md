===! "Réception"
    ```{.python .extra-class #id linenums="1"}
    from microbit import *
    import radio

    radio.on()
    radio.config(channel=1)         # n° Canal de communication
    radio.config(power=7)           # Signal à la puissance maximale

    
    while True:
            incoming = radio.receive()
            if incoming is not None:
                display.show('R')
                print(incoming)
            sleep(500)
  
    ```

=== "Emission"
    ``` {.python .extra-class #id linenums="1"}
    from microbit import *
    import radio

    radio.on()
    radio.config(channel=1)         # n° Canal de communication
    radio.config(power=7)           # Signal à la puissance maximale

    msg = "coucou"

    display.show('E')

    
    while True:
        if button_a.was_pressed():
            display.show(">>>")
            # Envoi du message
            radio.send(message)   
            sleep(1000)
            display.show('E')
            
        sleep(100)

    ```