
/*
 Filename: index.js
 Written by: Uladzimir Kasacheuski (UAK)
 Purpose: Simple Form Validation
 Date: 26 April 2016
 Modification History:
    Original Build
*/


///////////////////////////////////////////////////////////////////////////////////////////////////
// Initialize Jquery UI elements
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


//////////////////////////////////////
// Reset the form
//////////////////////////////////////
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

//////////////////////////////////////
// Initialize page elements
//////////////////////////////////////
function initializeElements(){
    //////////////////////////////////////
    // Initialize Buttons
    //////////////////////////////////////
    document.getElementById("resetButton").onclick = function(){
        resetForm();
    }
    document.getElementById("outputButton").onclick = function(){
        outputValues();
    }
    
    //////////////////////////////////////
    // Set up validation parameters
    //////////////////////////////////////
    jQuery.validator.addMethod("lettersonly", function(value, element) {
      return this.optional(element) || /^[a-z]+$/i.test(value);
    }, "Letters only please"); 
    $("#theForm").validate({
         rules: { // define valid user input
             name: { 
                 required: true,
                 lettersonly: true,
             },
             email: {  
                 required: true,
             },
             password: { 
                 required: true,
                 minlength: 6
             },
             datepicker: {  
                 required: true,
             },
             tel : {
                digits: true,
                minlength: 6,
                maxlength: 10,
             },
         }, // end rules
         messages: { // displayed when user input doesn't match the rules
             name: {  
                 required: "<Br> Please enter your name",
                 lettersonly : ("<br> Please use only letters in this field"),
             },
             email: {  
                 required: "<Br> Please enter an email",
             },
             password: {  
                 required: "<Br> Please provide a password",
                 minlength: $.validator.format("<Br>Must have at least {0} characters"),
             },
             datepicker: {  
                 required: "<Br> Please choose a date",
             },
             tel : {
                digits: "<Br> Please use only numbers in this field",
                 minlength: $.validator.format("<Br>Must have at least {0} characters"),
                 maxlength: $.validator.format("<Br>Can have at most {0} characters"),
             },
         } // end messages
    }); // end flintstoneForm.validate

    
    //////////////////////////////////////
    // Set up the slider to display values on change
    //////////////////////////////////////
    $( "#slider" ).on( "slidechange", function( event, ui ) { $("#sliderOutput").html("$" + window["get"].tip); } );
}

//////////////////////////////////////
// Global variable used to abstract geting values of the input fields
//////////////////////////////////////
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


//////////////////////////////////////
// Global variable used to store the input fields present as well as how to get their values
//////////////////////////////////////
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


//////////////////////////////////////
// Echo out values function
//////////////////////////////////////
function outputValues(){
    result = ($("#theForm").valid());
    
    if(result !== true){ // if result is false, then notify the user and return
        $("#preButton").html("Please Review the Above. There is something you did not fill out.");   
        return false;
    };
       
    $("#preButton").html("");   // since true, remove the error notification
    
    ////////////
    // Begin value output
    ////////////
    document.getElementById("outputElement").innerHTML = "Great. Lets Review! <br><Br>";
    keys = Object.keys(window['values']);
    total = keys.length;
    for(index = 0; index < total; index++){
        string = keys[index] + " : " + values[keys[index]]();
        document.getElementById("outputElement").innerHTML +=  string + "<br>";
    }
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