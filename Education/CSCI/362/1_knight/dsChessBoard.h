#ifndef DS_CCHESSBOARD_EXISTS
#define DS_CCHESSBOARD_EXISTS     
// dont forget #endif at bottom

#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;


class dsChessBoard{
    
public: 
    dsChessBoard();
    
    // set the board to -1 in every position
    void setBoardToNull();
    
    // output the board using cout
    void outputFullBoard();
    
    // Get the address of the x,y coordinate;
    int* returnPointerToPosition(int iPos, int jPos);
    
    // modify value of x,y
    void modifyValueOfTo(int x, int y, int to);
    
    // return value of x,y
    int returnValueOf(int x, int y);
    
    
private:
    int* board;
    int sizeX;
    int sizeY;
    
};

#endif