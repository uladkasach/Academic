/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Movers And Shakers Lab
 Date: 6 April 2016
 Modification History:
    Original Build
*/

function hideIt(ele){
    ele.hide();
}
function showIt(ele){
    ele.show();
}
function toggleIt(ele){
    ele.toggle();
}
function slideItUp(ele){
    ele.slideUp();
}
function slideItDown(ele){
    ele.slideDown();
}
function fadeOut(ele){
    ele.fadeOut();
}
function fadeIn(ele){
    ele.fadeIn();
}
function specialOne(ele){
    ele.fadeOut().delay(500).fadeIn();
}
function specialTwo(ele){
    ele.animate({
        opacity: 0.25,
        left: "+=50",
        height: "toggle"
      }, 5000).fadeTo(1,1);
}

////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    var shipEle = $("#shipEle");
    $("#button1").click( function(){ hideIt(shipEle); } );
    $("#button2").click( function(){ showIt(shipEle); } );
    $("#button3").click( function(){ toggleIt(shipEle); } );
    $("#button4").click( function(){ slideItUp(shipEle); } );
    $("#button5").click( function(){ slideItDown(shipEle); } );
    $("#button6").click( function(){ fadeIn(shipEle); } );
    $("#button7").click( function(){ fadeOut(shipEle); } );
    $("#button8").click( function(){ specialOne(shipEle); } );
    $("#button9").click( function(){ specialTwo(shipEle); } );
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////