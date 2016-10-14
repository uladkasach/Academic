#ifndef QUICK_SORT_EXISTS
#define QUICK_SORT_EXISTS     

#include "fundementals.h"

class cQuickSort{
protected:
    int* listArray;
    int listSize;
public:
    cQuickSort(int* thisList, int thisSize);
    
    void run();
    
    void quickSortFromTill(int from, int till);

};
#endif