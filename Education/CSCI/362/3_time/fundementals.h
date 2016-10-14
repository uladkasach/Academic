#ifndef FUNDEMENTALS_EXISTS
#define FUNDEMENTALS_EXISTS     


template <typename T> 
string intToString ( T Number ) {
    ostringstream ss;
    ss << Number;
    return ss.str();
}

//print array for debug
void printArray(int array[], int size);
void printArray(int array[], int from, int total);

#endif