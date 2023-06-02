/*
{
    // File	
    var vFile = "data.json";
    // Reader
    var vReader = new FileReader();
    vReader.readAsText(vFile.files[0]);
    vReader.onload = function(pEvent) {
        // String Input
        var vContent = pEvent.target.result;   
        // JSON to object
        var vJson = JSON.parse(vContent);    
        // Query
        var vResult = "QUERY YOUR JSON HERE TO BUILD YOUR RESULT"
        // Output
        document.getElementById("mydiv").appendChild(document.createTextNode(vResult));
    };
    }

*/

const jsonData= require('./data.json'); 
console.log(jsonData);