var requestURL = 'data.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  creer_capteur();
}

function lecture(){

  //console.log(data_capteurs);
}


function creer_capteur(){
data_capteurs = request.response;
lecture();
  for(id in data_capteurs)
  {
    capteur = document.getElementById('capteurs').appendChild(document.createElement('div'));
    capteur.id = id;
    capteur.classList.add("capteur");
    capteur.style.top = data_capteurs[id]['top'];
    capteur.style.left = data_capteurs[id]['left'];
    texte = capteur.appendChild(document.createElement('p'));
    
    if (data_capteurs[id]['valeur']==""){
      texte.textContent = "erreur";
      capteur.style.background = "gray";
    }
    else{
      texte.textContent = data_capteurs[id]['valeur']+String.fromCharCode(176)+"C";
      if (data_capteurs[id]['valeur'] > 30){
        capteur.style.background = "red";
      }
      if (data_capteurs[id]['valeur'] <= 30){
        capteur.style.background = "yellow";
      }
      if (data_capteurs[id]['valeur'] <= 20){
        capteur.style.background = "orange";
      }
      if (data_capteurs[id]['valeur'] <= 15){
        capteur.style.background = "light blue";
      }
      if (data_capteurs[id]['valeur'] <= 8){
        capteur.style.background = "blue";
      }
      if (data_capteurs[id]['valeur'] <= 0){
        capteur.style.background = "dark blue";
      }
    }
  }
  setTimeout('creer_capteur',10000);
}