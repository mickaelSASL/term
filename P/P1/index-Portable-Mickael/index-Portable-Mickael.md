---
hide:
    - toc
---    

# **P1: Relevé de température 🌡️ (Projet révision de première)**  
<center>![](https://cdn.sanity.io/images/ajwvhvgo/production/fd06eb79876afd582f5cc6064da724262312c875-4258x2496.png?w=325&q=80&fit=max&auto=format)
</center>

<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/EfrxVkS2glxLiPjjZkL4xi4BGGOwQtYzkXi6ujiCNBub0A" target="_blank">Document de consignes
![](https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico)</a>


<table style="border: none;">
  <thead>
    <tr>
      <td align="center" style="color: red; font-weight: bold; font-size: 18px">
        ⚠️ ATTENTION
      </td>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
      La communication série entre une carte microbit et l'ordinateur se fait sous forme de bytes.
        <ul>
          <li>Sur la carte : Vous devrez créer un dictionnaire, qui sera automatiquement converti en chaine de caractères puis en bytes lors de l'envoi (<code>print()</code>)</li>
          <li>Sur l'ordinateur : Les bytes reçus (octets) correspondent aux codes numériques des caractères de la chaine de caractères communiqués. Il faudra alors utiliser le module <code>dico.py</code> pour transformer cette série d'octets en dictionnaire.</li>
        </ul>
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
___

module <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EUrSx7x4WFpJlhjnSZGSjP8BAoZ-ke0WaLECIVa9faW-7w" target="_blank">`dico.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Exemple d'écriture sur le port série : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EeEU5xTQ82BIgRs76XpQ7VEBtwN90OIwkt-MMshMSTOQxg" target="_blank">`exemple_com-serie_µb.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Exemple de lecture sur le port série : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EWn37BtSWGNJvaH1BjiUnWYBlSV1JZ9YsuftKzIax-Azhw" target="_blank">`exemple_com-serie_PC.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a>

Fichier à compléter partie A : carte microbit : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/ETtl03HKbztFjhhNPP-8EP8BttHEvRh3BUO3b7rHlmtoGQ?e=LWSVke" target="_blank">`microbit.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Fichier à compléter partie B : carte microbit (côté PC) : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EVTmEcw_sjFFqpZSCROzE4ABfR8E788lIWEym9ohIvWHBQ?e=wO5koT" target="_blank">`microbit_PC.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Fichier à compléter partie C : carte microbit : <a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EbyzsOLyKdxNlwH56P8AxnoB5zKje5i0s81MZHbHXhH5lA?e=Srn3rV" target="_blank">`serveur_web.py`
![](https://icons.iconarchive.com/icons/untergunter/leaf-mimes/32/text-x-python-icon.png)</a><br>
Fichier de configuration de Laragon :<a href="https://sasl56-my.sharepoint.com/:u:/g/personal/mickael_kerviche_sa-sl_fr/EXOgTC_H2BZGu-LHLHbZWJABz5HuZsmK_nmZVFXe6F6P7g?e=Tqi6c2" target="_blank">`httpd.conf`
![](https://icons.iconarchive.com/icons/icojam/blue-bits/32/document-settings-icon.png)</a><br>

<a href="https://python.microbit.org/v/2" target="_blank">IDE microbit en ligne
![](https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a><br>