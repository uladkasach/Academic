#ifndef KNIGHT_EXISTS
#define KNIGHT_EXISTS     
// dont forget #endif at bottom

#include "dsLinkedList.h"
#include "dsStack.h"
#include "dsChessBoard.h"

class cKnight {
    
public:
    cKnight(int iPos, int jPos);
    
    ///////////////////////
    // Get all positions that knight can move from a position to in form **array
    ///////////////////////
    int* getPositionToMoveToFor(int iPos, int jPos, int index);
    int** returnPositionsToMoveToFrom(int iPos, int jPos);
    ///////////////////////

    
    ///////////////////////
    // Save New Position
    ///////////////////////
    void setNewPosition(int iPos, int jPos);
    ///////////////////////
    
    ///////////////////////
    // Make A New Move
    ///////////////////////
    bool makeANewMove(int* backtrackedPosition);
    
    //////////////////////////
    // Pick a move with Warnsdoff
    //////////////////////////
    int countNumberOfPositionsCanMoveTo(int** positions);
    int* pickAMoveWithWarnsdoff(int** positionsCanMoveTo);
    
    
    //////////////////////////
    // Pick a move with backtracking
    //////////////////////////
    int* backtrackMovement();
    int* moveWithBackTracking(int** positionsCanMoveTo, int* backtrackedPosition);
    
    
    
    //////////////////////////
    // Solve System
    //////////////////////////
    void solveTheSystem();
    
    
    //////////////////////////
    // Outputs for program use
    //////////////////////////
    dsChessBoard returnThisBoard();
        
    //////////////////////////
    // Outputs for debuging
    //////////////////////////
    void readOffPositionsArray(int** positions);
    void outputBacktrackList();
    
    
           
private: 
    dsChessBoard thisBoard;
    dsStack thisStack;
    //int movesMade; // will determine which position to put in 8by8 array by counting stack O(64) vs constant time. O(64) is not big deal to sacrifice for sake of simplifying code readibility. 
    
    
};

#endif