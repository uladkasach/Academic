/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Buttons Lab
 Date: 10 March 2016
 Modification History:
    Original Build
*/


//////////////////////////////////////
///////////
/*
Purpose : Show that time has passed
Parameters : text display div
Return : n/a
*/
///////////
function showTimePassed(ele){
    ele.innerHTML +=  "<Br> ... <Br>" ;
}
//////////////////////////////////////



//////////////////////////////////////
///////////
/*
Purpose : Engage the battle
Parameters : text display div
Return : n/a
*/
///////////
function engage(ele){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Yarghhhhh, me harties! Man D'e battle Stations!");   
    ele.innerHTML += "Your ship has come across its mortal enemy! The not-enough-time-in-a-day-ador! It engaged in combat! ";
    showTimePassed(ele);
}
//////////////////////////////////////


//////////////////////////////////////
///////////
/*
Purpose : Fire X cannonballs
Parameters : text display div, # of cannonballs
Return : n/a
*/
///////////
function Faiyer(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Faiyer, yu dawgs! Blow em to BITS!");
    ele.innerHTML += "Our ship has fired on the enemy. " + number + " cannonballs have connected.";
    showTimePassed(ele);
}
//////////////////////////////////////

//////////////////////////////////////
///////////
/*
Purpose : Report Damage
Parameters : text display div, # of severity
Return : n/a
*/
///////////
function Damage(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Alass! We got em!");
    ele.innerHTML += "Enemy ship recieved damages ranking severity of " + number + "/10.";
    showTimePassed(ele);
}
//////////////////////////////////////

//////////////////////////////////////
///////////
/*
Purpose : Report Retalliation
Parameters : text display div, # of Cannonballs
Return : n/a
*/
///////////
function Retaliation(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Scatter you rats! Return Faiyer approaching!");
    ele.innerHTML += "Enemy ship has retaliated with " + number + " cannon balls.";
    showTimePassed(ele);
}
//////////////////////////////////////


//////////////////////////////////////
///////////
/*
Purpose : Report Casualties
Parameters : text display div, # of Casualties
Return : n/a
*/
///////////
function Casualties(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("All yee wounded say Arrrrrrrrghhhhhh!");
    ele.innerHTML += "Casualties suffered by your ship : " + number + ".";
    showTimePassed(ele);
}
//////////////////////////////////////


//////////////////////////////////////
///////////
/*
Purpose : Report Your ships damage
Parameters : text display div, # of Casualties
Return : n/a
*/
///////////
function YourShipsDamage(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Laddie, how is the hull!?");
    ele.innerHTML += "Your ship recieved damages ranking severity of " + number + "/10.";
    showTimePassed(ele);
}
//////////////////////////////////////



//////////////////////////////////////
///////////
/*
Purpose : Report Your ships damage
Parameters : text display div, # of Casualties
Return : n/a
*/
///////////
function Victory(ele, number){
    if(ele == undefined){
        var ele = document.getElementById("theResult");
    }
    alert("Yarrrr! Watch them flee!");
    ele.innerHTML += "Enemy ship is fleeing at " + number + " knots. We can still catch them.... Yarrrrrrgh";
    showTimePassed(ele);
}
//////////////////////////////////////


////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    value =  3.141592653 ;
    console.log((value.length));
    
    var ele = document.getElementById("theResult");
    
    var button = document.getElementById("button-1");
    button.onclick = function(){Faiyer(ele, 1)};
    button.getElementsByTagName("div")[0].innerHTML = "Faiyer!";
    
    var button = document.getElementById("button-2");
    button.onclick = function(){Damage(ele, 2)};
    button.getElementsByTagName("div")[0].innerHTML = "Damage!";
    
    var button = document.getElementById("button-3");
    button.onclick = function(){Retaliation(ele, 3)};
    button.getElementsByTagName("div")[0].innerHTML = "Retaliation!";
    
    var button = document.getElementById("button-4");
    button.addEventListener("click", function(){ Casualties(ele, 4) }, false);
    button.getElementsByTagName("div")[0].innerHTML = "Casualties!";
    
    var button = document.getElementById("button-5");
    button.addEventListener("click", function(){ YourShipsDamage(ele, 5) }, false);
    button.getElementsByTagName("div")[0].innerHTML = "YourShipsDamage!";
    
    var button = document.getElementById("button-6");
    button.addEventListener("click", function(){ Victory(ele, 6) }, false);
    button.getElementsByTagName("div")[0].innerHTML = "Victory!";
    
    engage(ele);
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////