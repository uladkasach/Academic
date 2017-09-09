
#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;
#include "dsLinkedList.h"
#include "dsStack.h"
#include "dsChessBoard.h"
#include "cKnight.h"

    cKnight::cKnight(int iPos, int jPos){
        setNewPosition(iPos, jPos);
    }
    
    ///////////////////////
    // Get all positions that knight can move from a position to in form **array
    ///////////////////////
    int* cKnight::getPositionToMoveToFor(int iPos, int jPos, int index){
        int xMod = 0;
        int yMod = 0;
        
        if(index == 0){
            xMod = -2;
            yMod = -1;
        } else if (index == 1){
            xMod = -1;
            yMod = -2;
        } else if (index == 2){
            xMod = 2;
            yMod = 1;
        } else if (index == 3){
            xMod = 1;
            yMod = 2;
        } else if (index == 4){
            xMod = -2;
            yMod = 1;
        } else if (index == 5){
            xMod = -1;
            yMod = 2;
        } else if (index == 6){
            xMod = 2;
            yMod = -1;
        } else if (index == 7){
            xMod = 1;
            yMod = -2;
        }
        
        int newI = iPos + xMod;
        int newJ = jPos + yMod;
        //cout << "testing" << newI << "," << newJ << endl;
        
        if(newI < 0 || newI > 7 || newJ < 0 || newJ > 7){ 
            // out of bounds
            return NULL;
        } else if (thisBoard.returnValueOf(newI, newJ) != -1){
            // already visited
            return NULL;   
        } else {
            int* position = new int [2];
            position[0] = newI;
            position[1] = newJ;
            return position;
        }
    }
    int** cKnight::returnPositionsToMoveToFrom(int iPos, int jPos){
        int **positions = new int* [8];
        int index = 0;
        while(index < 8){
            //positions[index] = NULL;//new int[2];
            positions[index] = getPositionToMoveToFor(iPos, jPos, index); // Index decides how to modify x and y to where knight can move
            index += 1;
        }
        return positions;
    }
    ///////////////////////

    
    ///////////////////////
    // Save New Position
    ///////////////////////
    void cKnight::setNewPosition(int iPos, int jPos){
        // Add move to Board
        int moveIndex = thisStack.length();
        thisBoard.modifyValueOfTo(iPos, jPos, moveIndex);
        
        //cout << "--- Knight Moved To (" << iPos << "," << jPos << ")" << endl; 
        //cout << " Stack length was " << thisStack.length();
        // Add move to stack
        thisStack.pushStack(iPos, jPos);
        //cout << " Stack now is " << thisStack.length() << endl;
        //thisBoard.outputFullBoard();
        //thisStack.readAll();
        
    }
    ///////////////////////
    
    ///////////////////////
    // Make A New Move
    ///////////////////////
    bool cKnight::makeANewMove(int* backtrackedPosition){
        //////////////////////////////////////
        // Get all positions knight can move to from current position
        //////////////////////////////////////
        int* currentPosition = thisStack.returnTop(); // dont forget delete []currentPosition;
        int** positionsCanMoveTo = returnPositionsToMoveToFrom(currentPosition[0], currentPosition[1]); // dont forget to delete positions can move to
        delete []currentPosition;
        
        //cout << "Stack Length : " << thisStack.length() << endl;
        
        //////////////////////////////////////
        // Determine where to move to next
        //////////////////////////////////////
        int* whereToMove;  // remember to delete it.
        if(thisStack.length() < 32){
            // if moved less than 32 times, use Warnsdoff's rule 
            whereToMove = pickAMoveWithWarnsdoff(positionsCanMoveTo);
        } else {
            whereToMove = moveWithBackTracking(positionsCanMoveTo, backtrackedPosition);  
            if(whereToMove == NULL){
                return false;
            }
        }
        
        delete []positionsCanMoveTo;
        delete []backtrackedPosition;
        
        //////////////////////////////////////
        // Make the move
        //////////////////////////////////////
        int newI = whereToMove[0];
        int newJ = whereToMove[1];
        setNewPosition(newI, newJ);
        
        return true;
    }
    
    //////////////////////////
    // Pick a move with Warnsdoff
    //////////////////////////
    int cKnight::countNumberOfPositionsCanMoveTo(int** positions){
        // helper function for pickAMoveWithWarnsdoff
        int index = 0;
        int count = 0;
        while(index < 8){
            if(positions[index] != NULL){
                count += 1;   
            }
            index += 1;
        }
        return count;
    }
    int* cKnight::pickAMoveWithWarnsdoff(int** positionsCanMoveTo){
        //find the position that has the least positions availible to it - max positions = 8;
        int* minPosition = NULL; // stores the min position
        int minPositionMoveCount = 9; // stores the moves from that position
        int index = 0;
        while(index < 8){
            if(positionsCanMoveTo[index] == NULL){
                //cout << "Not a possible move " << endl;
                index += 1;
                continue; // if this possible movement for the knight is not a valid position, skip it.   
            }
            int thisI = positionsCanMoveTo[index][0];
            int thisJ = positionsCanMoveTo[index][1];
            int** positionsForThisOne = returnPositionsToMoveToFrom(thisI, thisJ);
            int moveCountForThisOne = countNumberOfPositionsCanMoveTo(positionsForThisOne);
            
            
            if(minPositionMoveCount > moveCountForThisOne){
                //cout << "found a new min : " ;
                minPositionMoveCount = moveCountForThisOne;
                minPosition = positionsCanMoveTo[index];
            }
            //cout << moveCountForThisOne << endl;
            
            index += 1;   
        }
        if(minPosition == NULL){
            cout << "ERROR = WARNSDOFF RULE HAS FAILED." << endl;   
        }
        return minPosition;
    }
        
    //////////////////////////
    // Pick a move with backtracking
    //////////////////////////
    int* cKnight::backtrackMovement(){
        // Helper function for moveWithBacktracking - but this one is used in the solveSystem loop
        
        //1) Undo last move - get current position, set it to -1 on board, pop from stack
        //2) Return the position we just removed so that it can be used in makeNewMove()
        
        ///////////
        // 1)
        ///////////
        int* currentPosition = thisStack.returnTop(); // dont forget delete []currentPosition;
        int iPos = currentPosition[0];
        int jPos = currentPosition[1];
        
        
        // cout << "BACK TRACKING FROM " << iPos << "," << jPos << endl;
        // cout << " Stack length was " << thisStack.length();
        
        // Remove from board
        thisBoard.modifyValueOfTo(iPos, jPos, -1);
        // Remove from stack
        thisStack.popStack();
        
        //cout << " Stack now is " << thisStack.length() << endl;
        
        //thisBoard.outputFullBoard();
        //thisStack.readAll();
        ///////////
        // 2)
        ///////////
        return currentPosition;
        
    }
    int* cKnight::moveWithBackTracking(int** positionsCanMoveTo, int* backtrackedPosition){
        //cout << "=" << backtrackedPosition << endl;
        int index = 0;
        
        if(backtrackedPosition != NULL){
            //cout << backtrackedPosition[0] << "," << backtrackedPosition[1] << endl;
            // find the position we backtracked from and skip all including it and before it
            bool equal = false;
            while(equal == false && index < 8){
                //cout << "index : " << index << endl;
                if(positionsCanMoveTo[index] != NULL){
                    //cout << "-vs- " << positionsCanMoveTo[index][0] << "," << positionsCanMoveTo[index][1] << endl;
                    if(positionsCanMoveTo[index][0] == backtrackedPosition[0] && positionsCanMoveTo[index][1] == backtrackedPosition[1]){
                        equal = true;   
                    }
                }
                index += 1;
            }
            if(index > 7){
            }
        }
        
        //cout << "here" << endl;
        
        // find the first position can move to thats not null
        while(positionsCanMoveTo[index] == NULL && index <= 7){
            index += 1;   
        }
        //cout << "ere" << endl;
        
        if(index > 7){
            // cout << "No More Options" << endl;        
            // cout << "At level " << thisStack.length() << endl;   
            return NULL;
        } else {
            return positionsCanMoveTo[index];
        }
    }
    
    
    
    //////////////////////////
    // Solve System
    //////////////////////////
    void cKnight::solveTheSystem(){
        bool allClear = true; // used for backtracking
        int* backtrackedPosition = NULL; // used for backtracking
        
        
        bool devStillRun = true; // used for debuging
        int index = 0; // used for debuging
        int backtracked = 0; // used for debuging
        int maxStackLength = 0; // used for debuging
        
        
        while(thisStack.length() < 64 && devStillRun){
            allClear = makeANewMove(backtrackedPosition);
            if(backtrackedPosition != NULL){
                backtrackedPosition = NULL;   // remember to change backtrack to null after setting it 
            }
            if(allClear == false){
                backtrackedPosition = backtrackMovement();   
                backtracked += 1;
            }
            
            /*
            if(thisStack.length() < 32 && backtracked != 0){
                cout << "Backtracked warensdoff rule" << endl;
                devStillRun = false;
            }
            if(backtracked > 2000000){
                cout << "backtracked more than 50 times" << endl;
                devStillRun = false;
            }
            
            if(maxStackLength < thisStack.length()){
                maxStackLength = thisStack.length(); 
                cout << "!!!Max Stack Length : " << maxStackLength << endl;
            }
            */
            
            outputBacktrackList();
            index += 1;
        }
        
        
        //cout << thisStack.length() << " : length of stack " << endl;
        //thisBoard.outputFullBoard();
    }
    
    
    //////////////////////////
    // Outputs for program use
    //////////////////////////
    dsChessBoard cKnight::returnThisBoard(){
        return thisBoard;
    }

    //////////////////////////
    // Outputs for Debugging
    //////////////////////////
    void cKnight::readOffPositionsArray(int** positions){
        int index = 0;
        while(index < 8){
            cout << positions[index] << " : (" << positions[index][0] << "," << positions[index][1] << ")" <<endl;
            index += 1;
        }
    }
    void cKnight::outputBacktrackList(){
        int index = 0;
        while(index < 64 && index < thisStack.length()){
            if(index > 32){
                int* position = thisStack.getPositionFor(index);  
                cout << " (" << position[0] << "," << position[1] << ")";
            }
            index += 1;
        }
        cout << endl;
    }
    
    
           