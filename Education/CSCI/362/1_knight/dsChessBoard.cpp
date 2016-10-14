#include <string>
#include <iostream>     // std::cout
using namespace std;
#include "dsChessBoard.h"
    
    dsChessBoard::dsChessBoard(){
        sizeX = 8;
        sizeY = 8;
        board = new int[sizeX*sizeY];
        setBoardToNull();
        //outputFullBoard();
    }
    
    // set the board to -1 in every position
    void dsChessBoard::setBoardToNull(){
        int indexX = 0;
        int indexY = 0;
        while(indexX < 8 && indexY < 8){
            
            modifyValueOfTo(indexX, indexY, -1);
            
            indexX += 1;
            if(indexX > 7){
                indexY += 1;
                indexX = 0;
            }
        }
    }
    
    // output the board using cout
    void dsChessBoard::outputFullBoard(){
        int indexX = 0;
        int indexY = 0;
        while(indexX < 8 && indexY < 8){
            int val = returnValueOf(indexX, indexY);
            //cout << " (" << indexX << "," << indexY << ") : "; 
            if(val >= 0 && val < 10){
                cout << " ";   
            }
            cout << val << " ";
            indexX += 1;
            if(indexX > 7){
                indexY += 1;
                indexX = 0;
                cout << endl; // break line for next row
            }
        }
    }
    
    // Get the address of the x,y coordinate's data;
    int* dsChessBoard::returnPointerToPosition(int iPos, int jPos){
        int* addr = &board[iPos * sizeY + jPos];
        return addr;
    }
    
    // modify value of x,y
    void dsChessBoard::modifyValueOfTo(int x, int y, int to){
        int* address = returnPointerToPosition(x,y);
        *address = to;
    }
    
    // return value of x,y
    int dsChessBoard::returnValueOf(int x, int y){
        int* address = returnPointerToPosition(x,y);
        return *address;
    }
    
    
    