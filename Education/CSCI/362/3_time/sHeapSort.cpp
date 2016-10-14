#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */
#include <math.h>       /* floor */
#include <time.h> /* clock */

#include "sHeapSort.h"



    cHeapSort::cHeapSort(int* thisList, int thisSize){
        listArray = thisList;
        listSize = thisSize;
    }
    
    void cHeapSort::run(){
        buildHeap();   
        sortHeap();
    }
    
    void cHeapSort::buildHeap(){
        // For every element, percolate up. This will make sure every element satisfies this heaps conditions
        int* array = listArray;
        int total = listSize;
        int thisIndex;
        int parentIndex;
        for(int index = 0; index < total; index++){
            // "Inserted" a node at index, now must test to make sure that the parent is larger than this node
            percolateUp(index);
        }
    }
    void cHeapSort::percolateUp(int index){
        if(index == 0){
            // note, this function is not nessesary because it will compare itself to itself and be done either way.
            return; // it is the root node.    
        }
        // This heap is a biggest value root heap. If Parent is smaller than this element, swap the two and test new parent.
        int parentIndex = (int)floor(index/2);
        int thisVal = listArray[index];
        int parentVal = listArray[parentIndex];
        
        //cout << "indexes : " << index << " vs " << parentIndex << endl;
        //cout << "vals : " << thisVal << " vs " << parentVal << endl;
        
        if(parentVal < thisVal){
            swap(listArray[index], listArray[parentIndex]);
            percolateUp(parentIndex); // test this elements new parent
        }
        
    }
    
    void cHeapSort::sortHeap(){
        //printArray(listArray, listSize);
        /*
        1) swap root with last heap element
        2) percolate down
        */
        int lastHeapEleIndex = listSize-1; 
        int* array = listArray;
        
        while(lastHeapEleIndex > 0){
            swap(array[0], array[lastHeapEleIndex]);
            lastHeapEleIndex--; 

            //printArray(listArray, listSize);
            percolateDown(0, lastHeapEleIndex);
            //printArray(listArray, listSize);
            //cout << endl;
        }
        
    }
    
    void cHeapSort::percolateDown(int index, int lastHeapEleIndex){
        // if a child is bigger than this element,  then swap with the bigger child 
        
        int childIndex = (index + 1)*2 - 1; //must correct for 0*2 = 0;
        
        int thisVal = listArray[index];
        
        // Account for children going out of heap bounds.
        int child1Val;
        if(childIndex > lastHeapEleIndex){
            child1Val = -1;
        } else {
            child1Val = listArray[childIndex];
        }
        int child2Val;
        if(childIndex + 1 > lastHeapEleIndex){
            child2Val = -1;
        } else {
            child2Val = listArray[childIndex + 1];
        }
        
        //cout << thisVal << " ::vs:: " << child1Val << " vs " << child2Val << endl;
        
        if(thisVal < child1Val || thisVal < child2Val){
            //cout << "swapped! " << endl;
            int maxChildIndex = childIndex;
            if(child1Val < child2Val){
                maxChildIndex += 1;
            }
            swap(listArray[index], listArray[maxChildIndex]);
            percolateDown(maxChildIndex, lastHeapEleIndex);
        }
    }
    
    
