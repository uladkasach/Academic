#ifndef INSERTION_SORT_EXISTS
#define INSERTION_SORT_EXISTS     

#include "fundementals.h"

class cInsertionSort{
protected:
    int* listArray;
    int listSize;

public:
    cInsertionSort(int* thisList, int thisSize);

    void run();
    
    void sortElement(int indexOfElement);
    
};

#endif