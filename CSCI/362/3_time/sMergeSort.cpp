#include <string>
#include <iostream>     // std::cout
using namespace std;
#include <fstream> // open files
#include <sstream>
#include <stdlib.h> /* atoi */
#include <math.h>       /* floor */
#include <time.h> /* clock */

#include "sMergeSort.h"



    cMergeSort::cMergeSort(int* thisList, int thisSize){
        listArray = thisList;
        listSize = thisSize;
    }
    
    void cMergeSort::run(){
        for(int startSize = 1; startSize < listSize; startSize = startSize * 2){
            mergeBlocksCurrentSize(startSize);   
        }
    }
    
    void cMergeSort::mergeBlocksCurrentSize(int size){
        //cout << "Merging blocks - current size = " << size << endl;
        //merge the currently size sized blocks into size*2 blocks.
        int lastListElementIndex = listSize - 1;
        int newSize = size*2; 
        for(int index = 0; index < listSize; index += newSize){
            int block1FirstIndex = index;
            // block1EndIndex = block2start - 1;
            int block2FirstIndex = block1FirstIndex + size;
            if(block2FirstIndex > lastListElementIndex){
                //cout << "skipping merging once, only one block left" << endl;
                continue; // skip merging the blocks: there is no second block
            }
            int block2LastIndex = min(block2FirstIndex + size - 1, listSize-1);
            mergeTheseTwoBlocks(block1FirstIndex, block2FirstIndex, block2LastIndex);
        }
    }
    
    void cMergeSort::mergeTheseTwoBlocks(int block1FirstIndex, int block2FirstIndex, int block2LastIndex){
        //cout << block1FirstIndex << " " << block2FirstIndex << " " << block2LastIndex << " " << endl;
        int* array = listArray; 
        
        ///////////////////////////////////
        // Generate tempArray with both blocks merged into one ordered block
        ///////////////////////////////////
        int sizeOfNewBlock = block2LastIndex - block1FirstIndex + 1;
        int tempArray[sizeOfNewBlock];
        int block1Index = block1FirstIndex;
        int block2Index = block2FirstIndex;
        for(int index = 0; index < sizeOfNewBlock; index++){
            int block1Value = array[block1Index];
            int block2Value = array[block2Index];
            //cout << block1Value << " vs " << block2Value << endl;
            
            //cout << "b1i" << block1Index << " b2i" << block2Index << endl;
            if(block1Index >= block2FirstIndex){
                // if we've ran through block 1 completely, just add block2
                tempArray[index] = block2Value;
                block2Index++;
            } else if (block2Index > block2LastIndex){
                // if we've run through block 2, just add block 1
                tempArray[index] = block1Value;
                block1Index++;
            } else if(block1Value < block2Value){
                //cout << "here i am " << endl;
                tempArray[index] = block1Value;
                block1Index++;
            } else {
                tempArray[index] = block2Value;
                block2Index++;
            }
        }
        ///////////////////////////////////
        ///////////////////////////////////
        
        //printArray(tempArray, sizeOfNewBlock);
        
        ///////////////////////////////////
        // Replace elements of the two merged blocks in listArray with the tempArray
        ///////////////////////////////////
        for(int index = 0; index < sizeOfNewBlock; index++){
            array[block1FirstIndex + index] = tempArray[index];
        }
        ///////////////////////////////////
        ///////////////////////////////////
        
    }
    
