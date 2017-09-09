#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */
#include <math.h>       /* floor */
#include <time.h> /* clock */

#include "sQuickSort.h"



    cQuickSort::cQuickSort(int* thisList, int thisSize){
        listArray = thisList;
        listSize = thisSize;
    }
    
    void cQuickSort::run(){
        int* array = listArray;
        int total = listSize;
        quickSortFromTill(0, total-1);
            
        //printArray(array,total);
    }
    
    void cQuickSort::quickSortFromTill(int from, int till){
        
        int* array = listArray;
        int total = till - from;
        
        
        if(from >= till){
            // then you're at the last element, and you're all done.
            //cout << "all done" << endl;
            return;   
        }
        
        int pivotIndex = till;
        int wallIndex = from; //wall index = index of first bigger element, untill it is replaced by pivot
        
       // cout << endl << "Sorting from " << from << " till " << till << " total " << total << endl;
       // printArray(array, from, total);
        //cout << "pivot:"<< array[pivotIndex] << endl;
        
        for(int index = from; index < total+from; index++){
            //cout << array[index] << "vs" << array[pivotIndex] << endl;
            if(array[index] < array[pivotIndex]){
                //cout << "^^^swap^^^" << endl;
                swap(array[index], array[wallIndex]);
                wallIndex += 1; // set new wall at element greater than pivot
            }
            // else, move on
        }
        
        // set pivot at wallIndex
        swap(array[pivotIndex], array[wallIndex]);
        
        //////
        // Quicksort all elements before wall, quicksort all elements after wall
        //////
       // printArray(listArray, listSize);
        //cout << "quicksort from " << from << ", till " << wallIndex -1 << endl; 
        quickSortFromTill(from, wallIndex - 1);
        //cout << "quicksort from " << wallIndex+1 << ", till " << till << endl; 
        quickSortFromTill(wallIndex + 1, till);
        
    }
