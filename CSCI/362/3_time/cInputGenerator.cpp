
#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand

#include "cInputGenerator.h"
#include "fundementals.h"



cInputGenerator::cInputGenerator(){
    srand((unsigned)time(0));
    createInputFileForNArrays();
}

// random generator function:
int cInputGenerator::randomIntModI (int i) { return std::rand()%i;}

// random string of numbers generator, numbers from 0 - n-1
std::string cInputGenerator::returnStringOfRandomNumbers(int n){
    int maxSize = 20000;
    std::string result = "";
    int nArray[maxSize];

    // initialize array of predetermined size
    for(int index = 0; index < maxSize; index++){
        nArray[index] = index;
    }
    //cout << endl;


    // randomize the numbers by "shuffling"
    for(int index = 0; index < maxSize; index++){
        //cout << index << "vs" << nArray[randomIntModI(n)] << endl;
        std::swap(nArray[index], nArray[randomIntModI(maxSize)]);
    }
    //printArray(nArray, n);


    // put values to string to return it
    for(int index = 0; index < n; index++){
        result += intToString(nArray[index]);  
        if(index+1 != n){
            result+= " ";   
        }
    }

    return result;
}

void cInputGenerator::createInputFileForNArrays(){
    int arrayLengths[] = {5, 10, 25, 100, 500, 1000, 2000, 5000, 8000, 10000};
    int total = sizeof(arrayLengths) / sizeof(arrayLengths[0]);
    std::ofstream out("0_input.txt");
    for(int index = 0; index < total; index++){
        //cout << arrayLengths[index] << " ";
        out << returnStringOfRandomNumbers(arrayLengths[index]);
        out << "\n";
    }
    out << "#";
    out.close();
}
