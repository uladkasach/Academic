#ifndef DS_STACK_EXISTS
#define DS_STACK_EXISTS     

#include "dsLinkedList.h"

class dsStack : public dsLinkedList { // Stack is built of linked list
protected: 

public:
    // Remove the last entry on stack
    void popStack();
    
    // Add an entry to the stack
    void pushStack(int iPos, int jPos);
    
    // return the i,j position on top of stack with int* position = new int[2] 
    int* returnTop();
};


#endif