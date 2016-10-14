/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Conversions Lab
 Date: 1 Feb 2016
 Modification History:
    Original Build
*/


////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    var strName = prompt("Yar, matey - What be yur nomenclature-ation?", "Cannon Balls Bob"); 
    var strDoubloons = prompt("Avast, me hearties - how much Booty've ya got in da Trunk?", "6 B-arrrr-illion Doubloons"); 
    var intDoubloons = parseInt(strDoubloons);
    var intProfits = intDoubloons * 287;
    var strStr = "I, " + strName + ", have plundered " + intDoubloons + " doubloons resulting in a p-arrrrr-ofit of $"+intProfits+".   I can finally arrrrrrrr-ford to get my speach impediment f-arrrrr-ixed.";
    //alert(strStr);
    document.getElementById("theResult").textContent = strStr;
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////