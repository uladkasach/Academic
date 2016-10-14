#include <string>
#include <iostream>     // std::cout
using namespace std;
#include "dsLinkedList.h"
#include "dsStack.h"

// Remove the last entry on stack
void dsStack::popStack(){
    removeNode(length() - 1);
}

// Add an entry to the stack
void dsStack::pushStack(int iPos, int jPos){
    addNode(iPos, jPos);
}

// return the i,j position on top of stack with int* position = new int[2] 
int* dsStack::returnTop(){
    dsLinkedList::Node* topNode;
    topNode = selectNodeAtIndex(length()-1);
    int* currentPosition = new int[2]; // Dont forget to delete []currentPossition. Dont memory leak.
    currentPosition[0] = topNode->iPos;
    currentPosition[1] = topNode->jPos;
    return currentPosition;
}

    