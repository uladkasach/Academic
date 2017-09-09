/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Functions Lab
 Date: 3 Feb 2016
 Modification History:
    Original Build
*/



//////////////////////////////////////
///////////
/*
Purpose : Engage the battle
Parameters : text display div
Return : n/a
*/
///////////
function engage(ele){
    alert("Yarghhhhh, me harties! Man D'e battle Stations!");   
    ele.innerHTML += "Your ship has come across its mortal enemy! The not-enough-time-in-a-day-ador! It engaged in combat! ";
}
//////////////////////////////////////

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
Purpose : Fire X cannonballs
Parameters : text display div, # of cannonballs
Return : n/a
*/
///////////
function Faiyer(ele, number){
    alert("Faiyer, yu dawgs! Blow em to BITS!");
    ele.innerHTML += "Our ship has fired on the enemy. " + number + " cannonballs have connected.";
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
    alert("Alass! We got em!");
    ele.innerHTML += "Enemy ship recieved damages ranking severity of " + number + "/10.";
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
    alert("Scatter you rats! Return Faiyer approaching!");
    ele.innerHTML += "Enemy ship has retaliated with " + number + " cannon balls.";
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
    alert("All yee wounded say Arrrrrrrrghhhhhh!");
    ele.innerHTML += "Casualties suffered by your ship : " + number + ".";
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
    alert("Laddie, how is the hull!?");
    ele.innerHTML += "Your ship recieved damages ranking severity of " + number + "/10.";
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
    alert("Yarrrr! Watch them flee!");
    ele.innerHTML += "Enemy ship is fleeing at " + number + " knots. We can still catch them.... Yarrrrrrgh";
}
//////////////////////////////////////

//////////////////////////////////////
///////////
/*
Purpose : Dont start script untill youtube loads
Parameters : n/a
Return : n/a
*/
///////////
function runMeAfterMusicLoads(){
    // Set timeout to hopefully give youtube time to load the video
    setTimeout(function(){
        var ele = document.getElementById("theResult");
        Faiyer(ele, 21);
        showTimePassed(ele);
        Damage(ele, 7);
        showTimePassed(ele);
        Retaliation(ele, 65);
        showTimePassed(ele);
        Casualties(ele, 3);
        showTimePassed(ele);
        YourShipsDamage(ele, 8);
        showTimePassed(ele);
        Faiyer(ele, 89);
        showTimePassed(ele);
        Damage(ele, 9.5);
        showTimePassed(ele);
        Victory(ele, 10);   
    }, 3500);
}
//////////////////////////////////////

////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    var ele = document.getElementById("theResult");
    engage(ele);
    showTimePassed(ele);
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////