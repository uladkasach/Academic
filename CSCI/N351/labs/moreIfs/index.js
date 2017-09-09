/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: More Ifs Lab
 Date: 15 Feb 2016
 Modification History:
    Original Build
*/

function askTheUserForADegree(type){
    response = parseInt(prompt("Yar, Matey - what is your " + type));
    return response;
}

function ifStatementRun(intCurrentLatitude, intDestinationLatitude, intCurrentLongitude, intDestinationLongitude){
    output = "Head ";
    if(intCurrentLatitude <= intDestinationLatitude){
        output += "North";   
    } else if(intCurrentLatitude !== intDestinationLatitude){
        output += "South";   
    }
    output += " ";   
    if(intCurrentLongitude <= intDestinationLongitude){
        output += "East";   
    } else if (intCurrentLongitude !== intDestinationLongitude){
        output += "West";   
    }
    document.getElementById("ifsOutput").innerHTML = output;
}

function switchStatementRun(intCurrentLatitude, intDestinationLatitude, intCurrentLongitude, intDestinationLongitude){
    output = "Head ";
    switch (true){
        case(intCurrentLatitude <= intDestinationLatitude):
            output += "North";  
        break;
        case(intCurrentLatitude >= intDestinationLatitude):
            output += "South";  
        break;
    }
    output += " ";   
    switch (true){
        case(intCurrentLongitude <= intDestinationLongitude):
            output += "East";  
        break;
        case(intCurrentLongitude >= intDestinationLongitude):
            output += "West";  
        break;
    }
    document.getElementById("switchOutput").innerHTML = output;
}
/*
 if intCurrentLatitude <= intDestinationLatitude && intCurrentLongitude <= intDestinationLongitude, output "Head North East"
- else if intCurrentLatitude <= intDestinationLatitude && intCurrentLongitude >= intDestinationLongitude, output "Head North West"
- else if intCurrentLatitude >= intDestinationLatitude && intCurrentLongitude >= intDestinationLongitude, output "Head South West"
- else if intCurrentLatitude >= intDestinationLatitude && intCurrentLongitude <= intDestinationLongitude, output "Head South East"
*/


////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    var intCurrentLatitude = askTheUserForADegree("Current Latitude");
    var intDestinationLatitude = askTheUserForADegree("Destination Latitude");
    var intCurrentLongitude = askTheUserForADegree("Current Longitude");
    var intDestinationLongitude = askTheUserForADegree("Destination Longitude");
    
    ifStatementRun(intCurrentLatitude, intDestinationLatitude, intCurrentLongitude, intDestinationLongitude);
    switchStatementRun(intCurrentLatitude, intDestinationLatitude, intCurrentLongitude, intDestinationLongitude);
    
    console.log(intCurrentLatitude);
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////