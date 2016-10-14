#ifndef INPUT_LOADER_EXISTS
#define INPUT_LOADER_EXISTS     

#include "fundementals.h"



class cInputLoader{
    protected : 
        int returnLineIndexOfList(int size);

    public:
        int* returnListOfSize(int size);
};


#endif