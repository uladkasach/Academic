#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>

#include "fundementals.h"



//print array for debug
void printArray(int array[], int size){
    for(int index = 0; index < size; index++){
        cout << array[index] << ", ";    
    }
    cout << endl;
}
//print array for debug
void printArray(int array[], int from, int total){
    for(int index = from; index < total+from; index++){
        cout << array[index] << ", ";    
    }
    cout << endl;
}



