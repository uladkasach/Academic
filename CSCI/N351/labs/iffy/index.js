/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Iffy Lab
 Date: 10 Feb 2016
 Modification History:
    Original Build
*/

function askTheUser(){
    response = prompt("Did yee land at port at noon?").toUpperCase();
    if(response == "YES"){
        document.getElementById("speaker").innerHTML += ("Yargh. Good. Yu get yerself 4 extra doubloons. <Br><Br>");
    } else if (response == "NO"){
        document.getElementById("speaker").innerHTML += ("ARGHHHH! Off to the gallows you go! <Br><Br>");   
    }  else {
        //////////////////
        //////////////
        // If user enters an answer other than yes or no
        //////////////
        document.getElementById("speaker").innerHTML += "hWhat did you say, laddie? Yes or No answers! <Br><Br>";
        alert("hWhat did you say, laddie? Yes or No answers!");
        askTheUser();
        //////////////////
    }
}

////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    askTheUser();
    
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////