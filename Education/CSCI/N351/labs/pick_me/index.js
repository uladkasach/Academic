/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Pick Me Lab
 Date: 30 March 2016
 Modification History:
    Original Build
*/


///////////////////////////////////
// Toggle Ugly Border on all divs on page
///////////////////////////////////
window["Uglified"] = false;
function drawGridForAllDivs(){
    if(window["Uglified"] == false){
        $("div").css({border:"1px solid gray",}); 
        window["Uglified"] = true;
    } else {
        $("div").css({border:"1px solid white",}); 
        window["Uglified"] = false;
    }
}

/////////////////////////////////
// Make buttons purdy
/////////////////////////////////
function makeButtonsNice(){
    $(".button").css({borderRadius : "3px", backgroundColor : "#175d17", color: "white", padding : "15px"});
}

/////////////////////////////////
// Make ele 2&9 easy to see
/////////////////////////////////
function makeEasyToSee(){
    $("#ele2").css({fontWeight : "bold", color: "blue",});
    $("#ele9").css({fontWeight : "bold", color: "blue",});
}



/////////////////////////////////
// Multiple Instructions
/////////////////////////////////
function multiInstruct(){
    $("#ele5").css({fontWeight : "bold", color: "purple",}).html("Look Ma, I'm Changing!").fadeOut("slow").css({backgroundColor:"purple",color:"white"}).fadeIn("slow");
}

/////////////////////////////////
// Modify only first span
/////////////////////////////////
function divModify(){
    $("span:first").css({border : "5px solid purple"});
}


/////////////////////////////////
// Modify only spans in buttons
/////////////////////////////////
function buttonSpanMod(){
    $(".button span").css({fontSize : "25px"});
}



/////////////////////////////////
// Find It!
/////////////////////////////////
function findIt(){
    $("#ele6 p").css({display : "inherit"});
}



////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    $("#button1").click(function() {
        drawGridForAllDivs();
    });
    $("#button2").click(function() {
        makeButtonsNice();
    });
    $("#button3").click(function() {
        makeEasyToSee();
    });
    $("#button4").click(function() {
        multiInstruct();
    });
    $("#button5").click(function() {
        divModify();
    });
    $("#button6").click(function() {
        buttonSpanMod();
    });
    $("#button7").click(function() {
        findIt();
    });
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////