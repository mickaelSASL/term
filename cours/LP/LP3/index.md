# **LP3 : Modularité**

<center><img src="https://files.realpython.com/media/Consuming-APIs-in-Python_Watermarked.beb5a262ae01.jpg" width="75%"></center>


<a href="https://sasl56-my.sharepoint.com/:w:/g/personal/mickael_kerviche_sa-sl_fr/ETD-O2EUZxhMhjeCcz_zIhwBIHRTG1uXWtzqOeY_gYRojA?e=ERAqjW
" target="_blank">Document de cours<img src="https://c1-word-view-15.cdn.office.net/wv/resources/1033/FavIcon_Word.ico"></a>


<a href="https://openweathermap.org/current" target="_blank">API Open Weather<img src="https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png"></a>

<a href="https://samples.openweathermap.org/data/2.5/weather?zip=14200,fr&appid=439d4b804bc8187953eb36d2a8c26a02" target="_blank">Exemple d'utilisation de l'API Open Weather<img src="https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png"></a>

`https://samples.openweathermap.org/data/2.5/weather?zip=14200,fr&appid=439d4b804bc8187953eb36d2a8c26a02`

```JSON
{
   "coord":{
      "lon":-122.09,
      "lat":37.39
   },
   "weather":[
      {
         "id":500,
         "main":"Rain",
         "description":"light rain",
         "icon":"10d"
      }
   ],
   "base":"stations",
   "main":{
      "temp":280.44,
      "pressure":1017,
      "humidity":61,
      "temp_min":279.15,
      "temp_max":281.15
   },
   "visibility":12874,
   "wind":{
      "speed":8.2,
      "deg":340,
      "gust":11.3
   },
   "clouds":{
      "all":1
   },
   "dt":1519061700,
   "sys":{
      "type":1,
      "id":392,
      "message":0.0027,
      "country":"US",
      "sunrise":1519051894,
      "sunset":1519091585
   },
   "id":0,
   "name":"Mountain View",
   "cod":200
}
```

clé API = 3f1aa1fecdccf8c6cdeeb41957ff33b4

<a href="https://openweathermap.org/api/air-pollution" target="_blank">Air Pollution<img src="https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png"></a>

<a href="https://openweathermap.org/api/geocoding-api" target="_blank">Geo Coding<img src="https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png"></a>

[Liste d'API gratuites](APIs.md)