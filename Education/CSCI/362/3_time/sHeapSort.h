#ifndef HEAP_SORT_EXISTS
#define HEAP_SORT_EXISTS     

#include "fundementals.h"


class cHeapSort{
protected:
    int* listArray;
    int listSize;
public:
    cHeapSort(int* thisList, int thisSize);
    
    void run();
    
    void buildHeap();
    void percolateUp(int index);
    
    void sortHeap();
    
    void percolateDown(int index, int lastHeapEleIndex);
    
    
};

#endif