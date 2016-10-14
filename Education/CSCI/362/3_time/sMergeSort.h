#ifndef MERGE_SORT_EXISTS
#define MERGE_SORT_EXISTS     

#include "fundementals.h"


class cMergeSort{
protected:
    int* listArray;
    int listSize;
public:
    cMergeSort(int* thisList, int thisSize);
    
    void run();
    
    void mergeBlocksCurrentSize(int size);
    
    void mergeTheseTwoBlocks(int block1FirstIndex, int block2FirstIndex, int block2LastIndex);
    
};
#endif