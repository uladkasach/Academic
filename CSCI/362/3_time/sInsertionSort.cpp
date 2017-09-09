#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */
#include <math.h>       /* floor */
#include <time.h> /* clock */

#include "sInsertionSort.h"



    cInsertionSort::cInsertionSort(int* thisList, int thisSize){
        listArray = thisList;
        listSize = thisSize;
    }

    void cInsertionSort::run(){
        int* array = listArray;
        int total = listSize;
        
        for(int index = 0; index < total; index++){
            sortElement(index);
        }
            
    }
    
    void cInsertionSort::sortElement(int indexOfElement){
        // implied that all indexes before index of element are already sorted.
        // How to sort, compare this element with the element before. If the element before is smaller, done. If its bigger, swap values and run sortElement on the element before.
        // Note - this is a recursive function
        if(indexOfElement == 0){
            return; // Its done, theres nothing before it.   
        }
        
        int* array = listArray;
        
        int thisElement = array[indexOfElement];
        int prevElement = array[indexOfElement - 1];
        if(prevElement < thisElement){
            return;   
        } else {
            swap(array[indexOfElement], array[indexOfElement - 1]);
            sortElement(indexOfElement - 1);
            //cout << "swapping" << thisElement << " and " << prevElement << endl;
        }
        
        //printArray(array, listSize);
    }
    
