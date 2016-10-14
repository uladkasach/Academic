/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Form Prototype
 Date: 20 April 2016
 Modification History:
    Original Build
*/


///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
 $(function() {
    $( "#accordion" ).accordion();
  });

  $(function() {
    $( "#slider" ).slider();
  });


  $(function() {
    $( "#datepicker" ).datepicker();
  });

  $(function() {
    var availableTags = [
      "Alder",
      "Ambrosia",
      "Amy root",
      "Apple",
      "Ash",
      "Azolla",
      "Bamboo",
      "Baobab",
      "Bearberry",
      "Bear corn ",
      "Bindweed",
      "Bird's nest",
      "Birch",
      "Daisy",
      "Earth",
      "Fellenwort",
      "Garlic",
      "Harlequin",
      "Inkberry",
      "Maple",
      "Nettle",
      "Poplar"
    ];
    $( "#tags" ).autocomplete({
      source: availableTags
    });
  });
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////


function resetForm(){
    document.getElementById('inputName').value = "";
    $('input[name=gender]').attr('checked',false);
    $('input[name=goals]').attr('checked',false);
    document.getElementById('inputEmail').value = "";
    document.getElementById('inputPassword').value = "";
    document.getElementById('inputTelephone').value = "";
    $( "#selector" ).slider( "value", 0 );
    document.getElementById('datepicker').value = "";
    document.getElementById('tags').value = "";
}

function initializeElements(){
    document.getElementById("resetButton").onclick = function(){
        resetForm();
    }
    document.getElementById("outputButton").onclick = function(){
        displayHello();
    }
    
    
}

function displayHello(){
    document.getElementById("outputElement").innerHTML = "Hello World!";   
}

////////////////////////////////////////////////////////////
// Function to run on page load
////////////////////////////////////////////////////////////
function theFunction(){
    initializeElements();
    
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// Attach function to pageload event
////////////////////////////////////////////////////////////
$(document).ready(theFunction); // end of $(document).ready()
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////