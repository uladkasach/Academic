#include <string>
#include <iostream>     // std::cout
using namespace std;
#include "dsLinkedList.h"
#include "cUserInput.h"

////////////////////////////
// Class Game Master ties together the user input, the solving of the knights treck, and the output.
////////////////////////////

    cUserInput::cUserInput(){
        //initialConditions.addNode(5);
    }
    
    int cUserInput::askForAPos(string whichPos){
        int pos = -1;
        while((pos < 1 || pos > 8)){
            cout << "Please define the " + whichPos + " position. (1-8)"<< endl;
            getline(cin, input);
            pos = atoi( input.c_str() );
            if(pos < 1 || pos > 8){
                cout << "Error, " + whichPos + "Pos was not a number from 1-8. Please try again." << endl;
            }
        }
        return pos;
    }
    int* cUserInput::getASetOfInitialPositions(){
        cout << "Please define which position you would like the system to be solved for. " << endl;
        
        int iPos = askForAPos("i (horizontal)");
        int jPos = askForAPos("j (vertical)");
        
        cout << "Solve the system for position (" << iPos << "," << jPos << "). Is this correct? ";
        
        if(!getYesOrNoInput()){
            cout << "Sorry about that, lets try again." << endl;
            getASetOfInitialPositions();
        } else {
            //cout << "return this i and j" << endl;
            int* positions = new int[2];
            positions[0] = iPos;
            positions[1] = jPos;
            return positions;
        }
    }
    bool cUserInput::getYesOrNoInput(){
        bool trueOrFalse;
        // Return false if no, return true if yes.
        input = "";
        while(input != "y" && input != "n"){
            cout << "(y/n)" << endl;
            getline(cin, input);
        }
        
        if(input == "y"){
            trueOrFalse = true;
        } else {
            trueOrFalse = false;   
        }
        
        return trueOrFalse;
    }
    int cUserInput::getNumberFromXToY(int x, int y){
        int theInt = -999;
        while(theInt < x || theInt > y){
            cout << "("<<x<<"-"<<y<<")"<< endl;
            getline(cin, input);
            theInt = atoi( input.c_str() );
            if(theInt < x || theInt > y){
                cout << "Error, that was not a number from "<<x<<"-"<<y<<". Please try again." << endl;
            }
        }
        return theInt;
    }
    //////////////////////////////////////////////////////////////////////
    // Details of Modify Initial Conditions
    //////////////////////////////////////////////////////////////////////
    void cUserInput::modifyASetOfInitialConditions(){
        cout << "Which condition would you like to modify?" << endl;
        initialConditions.readAll();
        int length = initialConditions.length();
        int indexToRemove = getNumberFromXToY(1,length) - 1;
        
        positions = getASetOfInitialPositions();
        int iPos = positions[0];
        int jPos = positions[1];
        delete []positions; // Free the memory for that set of positions.
        
        initialConditions.modifyNode(indexToRemove, iPos, jPos);
        cout << "Done." << endl;
    }
    //////////////////////////////////////////////////////////////////////
    void cUserInput::modifyConditionsUntillDone(){
        bool yesOrNo = true;
        while(yesOrNo == true){
            modifyASetOfInitialConditions();
            cout << "Do you want to modify another initial position? ";
            yesOrNo = getYesOrNoInput();
        }
    }
    //////////////////////////////////////////////////////////////////////
    
    //////////////////////////////////////////////////////////////////////
    // Details of Remove Initial Conditions
    //////////////////////////////////////////////////////////////////////
    void cUserInput::removeASetOfInitialConditions(){
        cout << "Which condition would you like to remove?" << endl;
        initialConditions.readAll();
        int length = initialConditions.length();
        int indexToRemove = getNumberFromXToY(1,length) - 1;
        initialConditions.removeNode(indexToRemove);
        cout << "Done." << endl;
    }
    //////////////////////////////////////////////////////////////////////
    void cUserInput::removeConditionsUntillDone(){
        bool yesOrNo = true;
        while(yesOrNo == true){
            removeASetOfInitialConditions();
            cout << "Do you want to remove another initial position? ";
            yesOrNo = getYesOrNoInput();
        }
    }
    //////////////////////////////////////////////////////////////////////
    
    //////////////////////////////////////////////////////////////////////
    // Details of Add Initial Conditions
    //////////////////////////////////////////////////////////////////////
    void cUserInput::saveThatSetOfPositions(int* positions){
        initialConditions.addNode(positions[0], positions[1]);
        //initialConditions.readAll();
    }
    void cUserInput::addANewSetOfInitialConditions(){
        positions = getASetOfInitialPositions();
        saveThatSetOfPositions(positions);
        delete []positions; // Free the memory for that set of positions.
    }
    //////////////////////////////////////////////////////////////////////
    void cUserInput::addInitialConditionsUntillDone(){
        bool yesOrNo = true;
        while(yesOrNo == true){
            addANewSetOfInitialConditions();
            cout << "Do you want to add another initial position to solve for? ";
            yesOrNo = getYesOrNoInput();
        }
    }    
    //////////////////////////////////////////////////////////////////////
    
    //////////////////////////////////////////////////////////////////////
    // Details of reviewing initial conditions
    //////////////////////////////////////////////////////////////////////
    int cUserInput::returnOneThroughThree(){
        int theInt = -1;
        while((theInt < 0|| theInt > 3)){
            cout << "(0-3)"<< endl;
            getline(cin, input);
            theInt = atoi( input.c_str() );
            if(theInt < 0 || theInt > 3){
                cout << "Error, that was not a number from 0-3. Please try again." << endl;
            }
        }
        return theInt;
    }
    int cUserInput::reviewInitialConditions(){
        cout << "Here are all the initial positions we will solve the system for :" << endl;
        initialConditions.readAll();
        cout << "Would you like to modify (1), remove (2), or add (3) any initial positions or are you satisfied with what you have chosen (0)? " << endl;
        int result = returnOneThroughThree();
    }
    //////////////////////////////////////////////////////////////////////
    void cUserInput::runReviewHandlerForResponse(int result){
        
        if(result == 1){
            modifyConditionsUntillDone();
        }
        if(result == 2){
            removeConditionsUntillDone();   
        }
        if(result == 3){
           addInitialConditionsUntillDone();
        }
    }
    //////////////////////////////////////////////////////////////////////
    
        
    ////////////////////////////////
    ////////////////////////////////
    // Puts it all together to loop through every initial condition the user wants to input, then review them.
    ////////////////////////////////
    ////////////////////////////////
    dsLinkedList cUserInput::getInitialConditionsWithReview(){
        // Start off by adding conditions
        addInitialConditionsUntillDone();
        // Then make sure the user is satisfied with what they have selected
        int result = -1;
        while(result != 0){
            result = reviewInitialConditions();
            runReviewHandlerForResponse(result);   
        }
        //        
        /*
        // finished setting initial conditions.
        initialConditions.addNode(1,2);
        //initialConditions.addNode(3,4);
        //initialConditions.addNode(5,6);
        //initialConditions.addNode(7,8);
        initialConditions.readAll();
        */
        
        return initialConditions;
    }
