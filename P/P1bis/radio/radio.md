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

    #Renseigner votre identifiant carte
    my_card_identifier="1A"

    radio.on()
    radio.config(channel=1)         # n° Canal de communication
    radio.config(power=7)           # Signal à la puissance maximale

    display.show('R')

    def get_serial_number(type=hex):
        NRF_FICR_BASE = 0x10000000
        DEVICEID_INDEX = 25 # deviceid[1]

        @micropython.asm_thumb
        def reg_read(r0):
            ldr(r0, [r0, 0])
        return type(reg_read(NRF_FICR_BASE + (DEVICEID_INDEX*4)) & 0xFFFFFFFF)        
        
    while True:
        if button_a.was_pressed():
            display.show(">>>")
            # Send a message
            radio.send(my_card_identifier+';'+get_serial_number())   
            sleep(1000)
            display.show('R')
            
        sleep(100)

    ```