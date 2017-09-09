///////////////////////////////////////
//main.cpp
///////////////////////////////////////
//Time Complexity Problem
/*
1) Create lists of random, non repeating, numbers for n = 100, 500, 1000, 2000, 5000, 8000, 10000. Store lists as seperate lines in file 0_input.txt. input will be loaded from this file for analyzing time complexity.

2) Implement insertion sort, quick sort, heap sort, and merge sort

3) Analyze time complexity of each function using unsorted input and sorted input
*/
///////////////////////////////////////
/*
Implementation:

First was created a class that generates random values from 1-20000 and saves them to a file for n sized lists of different sizes
Then was created a class that loads the specified size list

Then implemented were the sorting algorithems

Last was created a function that analyzed the times of each function, and then later that result is saved to an output file

The generation of an input file, and the generation of the output file are by default off but can be toggled on.
*/
///////////////////////////////////////
// Uladzimir Kasacheuski
// Started 4/13/16
// Completed 4/13/16
///////////////////////////////////////
//   
/*
cd /var/www/CSCi/362/3_time
*/

#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */
#include <math.h>       /* floor */
#include <time.h> /* clock */


#include "fundementals.h"
#include "cInputGenerator.h"
#include "cInputLoader.h"

#include "sInsertionSort.h"
#include "sQuickSort.h"
#include "sHeapSort.h"
#include "sMergeSort.h"




string analyzeSortIndexType(string type);

int main () {
    
    /////////////////////////
    //////// READ ME ////////
    /////////////////////////
    /* 
        IMPORTANT 
        - Only test one sorting method at a time, else the following algorithems will be sorting a sorted list 
        
        Currently the set up loads a n100 sized list, and prints it out. 
        To sort the list, specify the algo type you wish to test below.
        
        See Optional parts below to regenerate input file or create output file.
        
    */
    /////////////////////////
    
    ///////////////
    // Algo Types
    ///////////////
    // 1 = Insertion Sort
    // 2 = Quick Sort
    // 3 = Heap Sort
    // 4 = Merge Sort
    ///////////////
    int algoIndex = 4;
    ///////////////
    ///////////////
    
    
    ///////////////////////////////////////
    // OPTIONAL - REGENERATE INPUT FILE
    ///////////////////////////////////////
    if(false){ 
        //if (true) regenerates input file, optional. Writes to 0_input.txt
        cInputGenerator regenerateInputFile;
    }
    ///////////////////////////////////////
    ///////////////////////////////////////
    
    cInputLoader inputLoader;
    int* n100 =  inputLoader.returnListOfSize(100);
    
    printArray(n100, 100);

    string algoType = "No";
    if(algoIndex == 1){// Run Insertion Sort
        cInsertionSort insertionSort(n100,100);
        insertionSort.run();
        algoType = "Insertion";
    } else 
    if(algoIndex == 2){// Run Quick Sort
        cQuickSort quickSort(n100, 100);
        quickSort.run();
        algoType = "Quick";
    } else 
    if(algoIndex == 3){// Run Heap Sort
        cHeapSort heapSort(n100, 100);
        heapSort.run();
        algoType = "Heap";
    } else
    if(algoIndex == 4){ // Run Merge Sort
        cMergeSort mergeSort(n100,100);
        mergeSort.run();
        algoType = "Merge";
    }
    
    cout <<  " ===!!! " << algoType << " Sort Has Been Completed !!!===" << endl; 
    
    printArray(n100, 100);
    
    
    ///////////////////////////////////////
    // OPTIONAL - WRITE OUTPUT TO 0_output.txt FILE
    ///////////////////////////////////////
    if(false){ // Function used to generate output that will be used for graphs, writes to 0_output.txt
        string result1 = "";
        string result2 = "";
        string result3 = "";
        string result4 = "";

        result1 = analyzeSortIndexType("insertion");
        result2 = analyzeSortIndexType("quick");
        result3 = analyzeSortIndexType("heap");
        result4 = analyzeSortIndexType("merge");

        /*
        cout << result1 << endl;
        cout << result2 << endl;
        cout << result3 << endl;
        cout << result4 << endl;
        */
        std::ofstream out("0_output.txt");
        out << result1 << "\n";
        out << result2 << "\n";
        out << result3 << "\n";
        out << result4 << "\n" << "\n";;
    }
    ///////////////////////////////////////
    ///////////////////////////////////////
  return 0;
}




string analyzeSortIndexType(string type){
    cInputLoader inputLoader;
    //int arrayLengths[] = {5, 10, 100, 500, 1000, 2000, 5000, 8000, 10000};
    
    string analysis = ""; 
    int arrayLengths[] = {100, 500, 1000, 2000, 5000, 8000, 10000};
    int total = 7;
    int thisSize;
    int* thisList;
    for(int index = 0; index < total; index++){
        thisSize = arrayLengths[index];
        thisList = inputLoader.returnListOfSize(thisSize);
        //printArray(thisList, thisSize);

        clock_t tStart = clock();
        ////////////////////////////////////////
        if(type == "insertion"){
            cInsertionSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "quick"){
            cQuickSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "heap"){
            cHeapSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "merge"){
            cMergeSort sorter(thisList, thisSize);
            sorter.run();
        }
        ////////////////////////////////////////
        int unsortedTime = clock() - tStart;

        tStart = clock();
        ////////////////////////////////////////
        if(type == "insertion"){
            cInsertionSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "quick"){
            cQuickSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "heap"){
            cHeapSort sorter(thisList, thisSize);
            sorter.run();
        } else if(type == "merge"){
            cMergeSort sorter(thisList, thisSize);
            sorter.run();
        }
        ////////////////////////////////////////
        int sortedTime = clock() - tStart;
        
        analysis += intToString(unsortedTime) + ":" + intToString(sortedTime) + " ";
        //printArray(thisList, thisSize);
    }
    
    return analysis;
}
