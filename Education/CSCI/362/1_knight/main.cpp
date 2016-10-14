///////////////////////////////////////
//main.cpp
///////////////////////////////////////
//Knights Tour Problem
/*
1) User Input Linked list 
2) Solve Each Initial Condition
*/
///////////////////////////////////////
// Implementation 
/*
This program uses 3 data structures - dsLinkedList, dsStack, and dsChessBoard (which is an 8by8 array);

The program starts with cUserInput getting the user's input - including reviewing and modifying the data before starting solving the users initial conditions.

After the input is received, a linked list of initial positions is looped through, every initial position is passed to the cKnight class, which then solves the board for each initial position and returns the completed board back the the loop. The loop then displays the board and continues to the next initial position.

*/
// Uladzimir Kasacheuski
// Started 2/17/16
// Completed 2/22/16
///////////////////////////////////////
//   
/*
cd /var/www/CSCi/362/1_knight
*/

#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;

#include "dsChessBoard.h" 
#include "dsLinkedList.h" 
#include "dsStack.h" 

#include "cUserInput.h" 
#include "cKnight.h" 

void solveEachInitialCondition(dsLinkedList initialConditions); // function is below. Ties multiple classes together, but is too small to become need own, so its kept in main;

int main() {
    
    /////////////////////////////
    // Initialize the "Game Master" - handles inputs and solving the problem
    /////////////////////////////
    cUserInput userInputHandler;
    ////////////
    
    /////////////////////////////
    // Get initial conditions set.
    /////////////////////////////
    dsLinkedList initialConditions = userInputHandler.getInitialConditionsWithReview();
    ////////////
    
    /////////////////////////////
    // Get solve all initial conditions 
    /////////////////////////////
    solveEachInitialCondition(initialConditions); // Function is below. 
    ////////////
    
    
    return 0;
}


/////////////////////////////
// Loops through every initial condition, plugs it into cKnight, outputs the board.
/////////////////////////////
void solveEachInitialCondition(dsLinkedList initialConditions){
    cout << "Solving each initial position now : " << endl;
    //cout << initialConditions.length() << endl;

    int index = 0;
    int* thisPosition;
    while(index < initialConditions.length()){
        
        // Get this initial position
        thisPosition = initialConditions.getPositionFor(index);
        int iPos = thisPosition[0];
        int jPos = thisPosition[1];
        cout << "Solving for (" << iPos << "," << jPos << ") " << endl;
        
        // Solve the system
        cKnight knight(iPos-1, jPos-1); //5,3 5,5 5,6 -- 0,1 1,2 2,3 3,4 4,5 5,6 6,7
        knight.solveTheSystem();
        
        // Output the board
        dsChessBoard thisBoard = knight.returnThisBoard();
        thisBoard.outputFullBoard();
        
        index += 1;
    }
}