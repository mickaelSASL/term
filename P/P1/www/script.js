var requestURL = 'data.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  refresh_capteur();
}

// window.onload = refresh_capteur();


function refresh_capteur(){
  data = request.response;
 
  for (capteur of document.getElementById("capteurs").children)
  {
    id = capteur.id;
    capteur = document.getElementById(id[7]+"_temp")
    temp = data[id].valeur;
    // couleur_capteur = data;
    capteur.textContent = temp;

    if (temp==""){
      capteur.parentElementElement.style.background = "gray";
      temp.textContent = "erreur";
    }
    if (temp > 30){
      capteur.parentElement.style.background = "red";
    }
    if (temp <= 30){
      capteur.parentElement.style.background = "yellow";
    }
    if (temp <= 20){
      capteur.parentElement.style.background = "orange";
    }
    if (temp <= 15){
      capteur.parentElement.style.background = "light blue";
    }
    if (temp <= 8){
      capteur.parentElement.style.background = "blue";
    }
    if (temp <= 0){
      capteur.parentElement.style.background = "dark blue";
    }
  }
  
  setTimeout('refresh_capteur',10000);
}