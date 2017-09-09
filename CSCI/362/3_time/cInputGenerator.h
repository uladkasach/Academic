#ifndef INPUT_GENERATOR_EXISTS
#define INPUT_GENERATOR_EXISTS     

#include "fundementals.h"


class cInputGenerator {

    // random generator function:
    int randomIntModI (int i);

    public:
    
        cInputGenerator();

        // random string of numbers generator, numbers from 1 - n
        std::string returnStringOfRandomNumbers(int n);
    
        void createInputFileForNArrays();

};

#endif