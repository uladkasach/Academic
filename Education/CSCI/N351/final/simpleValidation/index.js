/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Simple Form Validation
 Date: 26 April 2016
 Modification History:
    Original Build
*/


///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
  $(function() {
    $.validator.setDefaults({ ignore: [] });
  });

 $(function() {
    $( "#accordion" ).accordion({ autoHeight: true, navigation: true, });
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


  $(function() {
    $( "#tabs" ).tabs();
  });
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////


function resetForm(){
    document.getElementById('inputName').value = "";
    $('input[name=gender]').attr('checked',false);
    $('#otherRadio').prop('checked',true);
    document.getElementById('inputEmail').value = "";
    document.getElementById('inputPassword').value = "";
    document.getElementById('inputTelephone').value = "";
    $( "#slider" ).slider( "value", 0 );
    document.getElementById('datepicker').value = "";
    document.getElementById('tags').value = "";
}

function initializeElements(){
    document.getElementById("resetButton").onclick = function(){
        resetForm();
    }
    document.getElementById("outputButton").onclick = function(){
        outputValues();
    }
    
    $("#commentForm").validate();
    
    $( "#slider" ).on( "slidechange", function( event, ui ) { $("#sliderOutput").html("$" + window["get"].tip); } );
}

window["get"] = {
      get name () {
         return document.getElementById('inputName').value;
      },
      get gender () {
         return $('input[name="gender"]:checked').val();
      },
      get goals () {
        var selected = [];
        $.each($("input[name='goals']:checked"), function(){            
            selected.push($(this).val());
        });
         return selected.join(", ");
      },
      get email () {
         return document.getElementById('inputEmail').value;
      },
      get password () {
         return document.getElementById('inputPassword').value;
      },
      get telephone () {
         return document.getElementById('inputTelephone').value;
      },
      get tip(){
        return $('#slider').slider("option", "value");  
      },
      get date(){
         return document.getElementById('datepicker').value;  
      },
      get plant(){
         return document.getElementById('tags').value;
      },
};
window['values'] = {
    name : function(){return window["get"].name},
    gender : function(){return window["get"].gender},
    goals : function(){return window["get"].goals},
    email : function(){return window["get"].email},
    password : function(){return window["get"].password},
    telephone : function(){return window["get"].telephone},
    tip : function(){return window["get"].tip},
    date : function(){return window["get"].date},
    plant : function(){return window["get"].plant},
};
function outputValues(){
    result = ($("#theForm").valid());
    
    if(result !== true){ 
        $("#preButton").html("Please check all tabs, there is something that you did not fill out. Thank you.");   
        return false;
    };
       
    $("#preButton").html("");   
    document.getElementById("outputElement").innerHTML = "Great. Lets Review! <br><Br>";
    keys = Object.keys(window['values']);
    total = keys.length;
    for(index = 0; index < total; index++){
        string = keys[index] + " : " + values[keys[index]]();
        document.getElementById("outputElement").innerHTML +=  string + "<br>";
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