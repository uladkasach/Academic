/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Arrays Lab
 Date: 24 Feb 2016
 Modification History:
    Original Build
*/






/*****			
Purpose: *** translate string char to character code ***			
Parameters: single character / letter		
Return: integer representing an ascii value
*****/
function parseAscii(chrCharacter)
{
    intAscii = chrCharacter.charCodeAt(0);
    return intAscii;
}

/*****			
Purpose: *** translate the anscii code into a binary string ***			
Parameters: single integer representing an ascii value	
Return: binary, base 2 representation of the number passed to this function
*****/
function parseBin(intAscii)
{
    strBin = parseInt(intAscii, 10).toString(2);
    if(strBin.length < 8)
    {
        var intPlaceHolders = 8 - strBin.length;
        for(var i = 0; i < intPlaceHolders; i++)
        {
            strBin = "0" + strBin;
        }

    }
    return strBin;
}


function output(string){
    document.getElementById("outputDiv").innerHTML += string;   
}


////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    
    /////////////////
    // Check to make sure exactly one character
    /////////////////
    chrCharacter = "";
    while(chrCharacter.length !== 1){
        chrCharacter = prompt(" Please enter one character ");
    }
    /////////////////
    
    intAscii = parseAscii(chrCharacter);
    strBin = parseBin(intAscii);
    array = strBin.split("");
    
    total = array.length;
    index = 0;
    while(index < total){
        if(array[index] == "0"){
            output("true");   
        } else {
            output("false");   
        }
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