/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Randomness Lab
 Date: 8 Feb 2016
 Modification History:
    Original Build
*/

var aPirate = {
    rank : null,
    name: null,
    favoriteNumber : null,
    speakingElement : null,
    
    pickANumber : function(){
        var number = Math.floor(Math.random() * 10) + 1  
        return number;
    },
    speak : function(speech){
        var strUAK = "buried treasure";
        this.speakingElement.innerHTML += speech;  
    },
}
////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){

    /////////////////////////////////////////////
    // Initiate the Captain
    /////////////////////////////////////////////
    var Captain = Object.create(aPirate);
    Captain.speakingElement = document.getElementById("captainSpeaker");
    Captain.rank = "Captain";
    Captain.name = "Slashin' Sam";
    Captain.favoriteNumber = Captain.pickANumber();
    Captain.speak("Yargh - Its yur Captain " + Captain.name + ". You fools are about to play a game for me bottle o'Grogg. Guess my number, 1 - 10. <Br><Br>");
    /////////////////////////////////////////////
    /////////////////////////////////////////////
    
    
    /////////////////////////////////////////////
    // Initiate the crew members
    /////////////////////////////////////////////
    var crewMembers = [];
    var crewNames = ["Jirmmy", "Blackbeard", "Sparrow"];
    /////////////////////////////////////////////
    total = crewNames.length;
    index = 0;
    while(index < total){
        thisName = crewNames[index];
        thisMember = Object.create(aPirate);
        thisMember.name = thisName;
        thisMember.rank = "Crew";
        thisMember.speakingElement = document.getElementById(thisName+"Speaker");
        crewMembers.push(thisMember);
        index += 1;
    }
    /////////////////////////////////////////////
    /////////////////////////////////////////////
    
    
    /////////////////////////////////////////////
    // Start Loop of Guesses
    /////////////////////////////////////////////
    total = crewMembers.length;
    index = 0;
    while(index < total){
        thisMember = crewMembers[index];
        thisMember.favoriteNumber = thisMember.pickANumber();
        thisMember.speak("I, " + thisMember.name + ", guess da number " + thisMember.favoriteNumber);
        index += 1;
    }
    /////////////////////////////////////////////
    /////////////////////////////////////////////
    
    
    /////////////////////////////////////////////
    // Start Captain Determining if there are any winners
    /////////////////////////////////////////////
    total = crewMembers.length;
    winningNumber = Captain.favoriteNumber;
    winningMembers = [];
    index = 0;
    while(index < total){
        thisMember = crewMembers[index];
        if(thisMember.favoriteNumber == winningNumber){
            winningMembers.push(thisMember.name);   
        }
        index += 1;
    }
    
    console.log(winningMembers);
    if(winningMembers.length == 0){
        Captain.speak("Ha! Ye fools! The winning number was " + Captain.favoriteNumber +"! Looks like this old bottle o'Grogg's stayin with papa.");
    } else {
        speech = "Shiver me timbers. ";
        total = winningMembers.length;
        index = 0;
        while(index < total){
            if(index !== 0){
                speech += " and ";   
            }
            thisName = winningMembers[index];
            speech += thisName;   
            index += 1;
        }
        speech += " have won.";
        if(total > 1){
            speech += " Share it wisely. L'est it corrupt your relations!";   
        }
        Captain.speak(speech);
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