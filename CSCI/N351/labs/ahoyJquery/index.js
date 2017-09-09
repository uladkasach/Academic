/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Ahoy jQuery Lab
 Date: 23 March 2016
 Modification History:
    Original Build
*/



function appendToP(){
    $("p").append("<br>Yarrrrrrrghhhh, you scaller wagger!");
}   

function replaceHTMLToP(){
    $("p").html("HA! You replaced it all! You'll never find the treasure now.");
}   

////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    $("p").html("Ahoy Matey!");
    
    document.getElementById("appendHTMLDiv").onclick = function(){
        appendToP();
    }
    document.getElementById("replaceHTMLDiv").onclick = function(){
        replaceHTMLToP();
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