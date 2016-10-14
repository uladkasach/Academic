
#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */

#include "cInputLoader.h"

int cInputLoader::returnLineIndexOfList(int size){
    // Determine if its a valid size, and which line it would be located on.
    int arrayLengths[] = {5, 10, 25, 100, 500, 1000, 2000, 5000, 8000, 10000};
    int total = sizeof(arrayLengths) / sizeof(arrayLengths[0]);
    bool valid = false;
    int whichLine = 0;
    for(int index = 0; index < total; index++){
        if(arrayLengths[index] == size){
            valid = true;
            whichLine = index;
            index = total;
        }
    }


    if(valid == false){
        cout << "Thats not a valid n size" << endl;
        return 9999999;
    }

    return whichLine;
}

int* cInputLoader::returnListOfSize(int size){
        int returnIndex = returnLineIndexOfList(size);

        std::ifstream input_stream("0_input.txt");
        std::string line;
        int lineIndex = 0;
        while(lineIndex <= returnIndex && std::getline(input_stream, line)){ // Note, getLine must be second
            lineIndex += 1;
        }
        //cout << line << endl;
        // line = line

        int* newArray = new int[size]; // NOTE: CREATING ON HEAP - MUST MANUALLY FREE WHEN DONE
        int newArrayIndex = 0;
        int total = line.length();
        std::string numberHold = ""; 
        char thisChar;
        for(int index = 0; index < total; index++){
            thisChar = line[index];
            //cout<<thisChar<<endl;
            if(thisChar == ' '){
                //cout << "Adding " << numberHold << endl;
                newArray[newArrayIndex] = atoi( numberHold.c_str() );
                newArrayIndex++;
                numberHold = "";
            } else {
                //cout << " holding " << intToString(thisChar); 
                numberHold += intToString(thisChar); 
            }
        }
        if(numberHold != ""){
            newArray[newArrayIndex] = atoi( numberHold.c_str() );
            newArrayIndex++;
            numberHold = "";
        }

        //printArray(newArray, size);

        return newArray;
}
