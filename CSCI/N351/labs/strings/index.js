/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Strings Lab
 Date: 29 Feb 2016
 Modification History:
    Original Build
*/






function output(string){
    document.getElementById("outputDiv").innerHTML += string + "<Br>";   
}

function generateNameFromString(string, length){
    // Create a random string of length length from string
    var d = new Date();
    var nMain = d.getTime(); 
    newString = "";
    while(newString.length < length){
        n = nMain * Math.random();
        n = n % string.length;
        newString += string.charAt(n);
    }
    return newString;
}


////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    inputName = prompt("Please enter your favorite persons name, y'r magesty");
    inputName = inputName.trim();
    inputName = inputName.replace("ou","'");
    inputName = inputName.replace("ea","'");
    shipNames = [];
    
    thisName = inputName.toUpperCase().substr(0,2) + "-en scurv'enaytor-" + inputName.toLowerCase().substr(-3, 2) + inputName.toUpperCase().substr(-1);
    shipNames.push(thisName);
    
    thisName = inputName.replace("a", "a-RRRRRRRGGgggh-") + " "+ inputName.toUpperCase().indexOf("A") + inputName.toUpperCase().indexOf("E") + inputName.toUpperCase().indexOf("I");
    shipNames.push(thisName);
    
    thisName = inputName.replace("s", "s-callywag-")+" "+  inputName.toUpperCase().indexOf("E") + inputName.toUpperCase().indexOf("U") + inputName.toUpperCase().indexOf("N");
    shipNames.push(thisName);
    
    thisName = "Man O' War Class " + inputName.charAt(3).toUpperCase() + inputName.toUpperCase().indexOf("A") + inputName.toUpperCase().indexOf("E") ;
    shipNames.push(thisName);
    
    thisName = "Man O' War Class " + inputName.charAt(1).toUpperCase() + inputName.toUpperCase().indexOf("C") + inputName.toUpperCase().indexOf("Z") ;
    shipNames.push(thisName);
    
    thisName = "Brigader Class " + inputName.charAt(0).toUpperCase() + inputName.charAt(1).toUpperCase() + (inputName.split(inputName.charAt(0)).length - 1) +  (inputName.split(inputName.charAt(1)).length - 1) +  (inputName.split(inputName.charAt(2)).length - 1) ; // First 2 char and how many times those char occur
    shipNames.push(thisName);
    
    thisName = "Brigader Class " + inputName.charAt(2).toUpperCase() + inputName.charAt(3).toUpperCase() + (inputName.split(inputName.charAt(2)).length - 1) +  (inputName.split(inputName.charAt(3)).length - 1) +  (inputName.split(inputName.charAt(4)).length - 1) ; // First 2 char and how many times those char occur
    shipNames.push(thisName);
    
    
    thisName = "Supply Boat " + generateNameFromString(inputName,6);
    shipNames.push(thisName);
    
    thisName = "Supply Boat " + generateNameFromString(inputName,6);
    shipNames.push(thisName);
    
    thisName = "Supply Boat " + generateNameFromString(inputName,6);
    shipNames.push(thisName);
    
    thisName = "Supply Boat " + generateNameFromString(inputName,6);
    shipNames.push(thisName);
    
    thisName = "Supply Boat " + generateNameFromString(inputName,6);
    shipNames.push(thisName);
    
    total = shipNames.length;
    index = 0;
    while(index < total){
        output(shipNames[index]);
        index += 1;
    }
	
    
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////