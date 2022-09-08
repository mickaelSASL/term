# **P1: Relevé de température 🌡️**  
<center>![](https://cdn.sanity.io/images/ajwvhvgo/production/fd06eb79876afd582f5cc6064da724262312c875-4258x2496.png?w=325&q=80&fit=max&auto=format)
</center>


<table style="border: none;">
  <thead>
    <tr>
      <td align="center" style="color: green; font-weight: bold; font-size: 18px">
        📝 CONSIGNES
      </td>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
      La carte microBit relève la température et la transmet à l'ordinateur par la liaison USB. <br>
      Le PC (2nd programme python) réceptionne les données et les affiche dans la console python.
    </td>
    </tr>
    <tr>
      <td>
        <center><img src="Communication.png")>
        </center>
      </td>
    </tr>
  </tbody>
</table>

<table style="border: none;">
  <thead>
    <tr>
      <td align="center" style="color: red; font-weight: bold; font-size: 18px">
        🏆 EN PLUS
      </td>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
      Le système peut être amélioré :  <br>
      <bold>- Amélioration 1</bold> : Une seconde carte se charge du relevé de température et la transmet par radio à la première qqui communique avec le PC.<br>
      <bold>- Amélioration 2</bold> : L'ordinateur affiche la température et l'enregistre dans un fichier 'csv' affiche la date et l'heure.
    </td>
    </tr>
  </tbody>
</table>

___

> **Installer le module _pyserial_**  
> à exécuter dans la console python : ```pip install pyserial```

___

Exemple de communication radio



Exemple d'écriture sur le port série : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EeEU5xTQ82BIgRs76XpQ7VEBtwN90OIwkt-MMshMSTOQxg" target="_blank">`exemple_com-serie_µb.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Exemple de lecture sur le port série : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EWn37BtSWGNJvaH1BjiUnWYBlSV1JZ9YsuftKzIax-Azhw" target="_blank">`exemple_com-serie_PC.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a>

<a href="https://python.microbit.org/v/2" target="_blank">IDE microbit en ligne
![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a><br>


<a href="https://microbit-micropython.readthedocs.io/fr/latest/" target="_blank">Documentation microPython Microbit
![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a>


___
## Communication série µBit --> PC

### programme PC:

```Python
import serial

ser = serial.Serial(
    port='COM11',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

msg=""

while msg!="$":           #Lecture du message
    for c in ser.read():
        msg = msg + chr(c)

        if chr(c) == '\n':
            print(msg)
            msg = ""
            break
        
print("fin")
ser.close()
```

### Programme µBit
```Python
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