#include <fstream> 
#include <iostream>     // std::cout
#include <iomanip>      // std::setw()
#include <stdlib.h>     // exit()
#include <math.h>       /* floor */
#include <string> 
#include <sstream>
namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}
using namespace std;


struct aValue {
    int ASCIICode;
    string character;
    int frequency;
};
    

struct treeNode {
    treeNode* leftNode;
    treeNode* rightNode;
    aValue* nodeValue;
};

struct encodedValue {
    string character;
    int ASCIICode;
    string encoding;
};

struct listElement {
    // list element has either node or value data, also holds size of the element
    int sumFreq; // sorting key
    treeNode* node;
    encodedValue* encodedVal;
};

void displayFreqList(listElement* inputList, int inputLength){
    for(int i = 0; i < inputLength; i++){
        cout << inputList[i].sumFreq << ",";   
    }
    cout << endl;
}

void displayFreqList_spec(listElement* inputList, int inputLength){
    // display the freqSum -vs- ASCII encoding
    
    for(int i = 0; i < inputLength; i++){
        encodedValue thisVal = *inputList[i].encodedVal;
        cout << inputList[i].sumFreq << " (-vs- " << thisVal.ASCIICode << "), ";   
    }
    cout << endl;
}

/////////////////////
// Sort List Elements by SumFreq
/////////////////////
void merge(listElement* inputList, int low, int mid, int high, int inputLength){
    //cout << "prev list status: ";
    //displayFreqList(inputList, inputLength);
    
    int sortedSegmentLength = high-low + 1;//last index - first index + 1 is size of new list
    //cout << "Sorted Segment Length = " << high - low << endl;
    listElement sortedSegmentList[sortedSegmentLength];
    //cout << "Sorted List : ";
    //cout << endl;

    int sortedSegmentIndex = 0;
    int highSegmentIndex = high;
    int lowSegmentIndex = mid;
    int lowFreq;
    int highFreq;
    for(int sortedSegmentIndex = sortedSegmentLength - 1; sortedSegmentIndex > -1; sortedSegmentIndex--){
        // Sort from big to small, enables using -1 as out of bounds condition
        
        if(lowSegmentIndex > low-1){
            lowFreq = inputList[lowSegmentIndex].sumFreq;
        } else {
            lowFreq = -1;
        }    
        if(highSegmentIndex > mid){
            highFreq = inputList[highSegmentIndex].sumFreq;
        } else {
            highFreq = -1;   
        }
        //cout << "SortedList["<<sortedSegmentIndex << "] = ... " << " (( L[li]=L["<<lowSegmentIndex<<"]="<< lowFreq << " -vs- L[hi]=L["<<highSegmentIndex<<"]="<<highFreq<<")) ";
        
        if(lowFreq > highFreq){
            sortedSegmentList[sortedSegmentIndex] = inputList[lowSegmentIndex];
            //cout << "(l)" << lowFreq << ", ";
            lowSegmentIndex--;
        } else {
            sortedSegmentList[sortedSegmentIndex] = inputList[highSegmentIndex];
            //cout << "(h)" << highFreq << ", ";
            highSegmentIndex--;
        }
        
        //cout << endl;
    }
    //cout << endl;
    //cout << "Now updating old array" << endl;
    //cout << " Sorted List Segment : ";
    //int difference = 0 - low; // sortedIndex = k - low
    for(int k=low;k<=high;k++){
        //cout << "k : " << k << " -vs- " << k-low << endl;
        //cout << sortedSegmentList[k-low].sumFreq << ",";
        inputList[k] = sortedSegmentList[k - low];  
    }
    
    //cout << endl;
    
    //cout << "now list status: ";
    //displayFreqList(inputList, inputLength);
}
void merge_sort(listElement* inputList, int low, int high, int inputLength){
     if(low<high){
        int mid = low + (high-low)/2;
        //cout << low << " - vs - " << high << "m = " << mid << endl;
        merge_sort(inputList, low, mid, inputLength);
        merge_sort(inputList, mid+1, high, inputLength);
        merge(inputList, low, mid, high, inputLength);
     }
}


////////////////////
// Build binary tree recursivly
////////////////////
void sortList(listElement* inputList, int inputLength){
    merge_sort(inputList, 0, inputLength-1, inputLength);
}
listElement* createBinaryTree(listElement* inputList, int inputLength){
    if(inputLength == 1){
        return inputList;   
    }
    
    sortList(inputList, inputLength); // ensure list is ordered in inc sumFreq size; 
    
    //cout << "lstS: " ;
    displayFreqList(inputList, inputLength);
    
    ////////////////////
    // Take bottom two elements, create a node out of them
    ////////////////////
    treeNode* newNode = new treeNode;
    newNode->leftNode = inputList[0].node;
    newNode->rightNode = inputList[1].node;
    newNode->nodeValue = NULL;

    ////////////////////
    // Create new list size inputLength - 1; First element = newElement, then append elements 2:inputLength-1
    ////////////////////
    listElement* newList = new listElement[inputLength - 1];
    newList[0].sumFreq = inputList[0].sumFreq + inputList[1].sumFreq;
    newList[0].node = newNode;
    //cout << "SumFreq = " << newList[0].sumFreq << endl;
    for(int i = 2; i < inputLength; i++){
        newList[i-1] = inputList[i];   
    }
    delete inputList; // clear old input list from memory
    
    
    //cout << "lstA: " ;
    displayFreqList(newList, inputLength-1);
    cout << endl;
    // create new list and delete old list
    return createBinaryTree(newList, inputLength - 1);
}


////////////////////
// build encoding list
////////////////////
void recordEncodingFor(treeNode* thisNode, encodedValue* encodedList, int* encodedIndex, string growingEncoding){
    
    if(thisNode->nodeValue != NULL){
        aValue thisValue = *thisNode->nodeValue;
        encodedValue* newEncoding = new encodedValue;
        newEncoding->character = thisValue.character;
        newEncoding->ASCIICode = thisValue.ASCIICode;
        newEncoding->encoding = growingEncoding;
        encodedList[*encodedIndex] = *newEncoding;
        //cout << encodedIndex << " -vs- " << *encodedIndex << endl;
        *encodedIndex = *encodedIndex + 1;
        //cout << "and now " << encodedIndex << " -vs- " << *encodedIndex << endl;
        //cout << "Node value == null!" << endl;
        cout << "encodedList[" << *encodedIndex << "]={character:'" << thisValue.character << "', ASCIICode:'"<< thisValue.ASCIICode << "', encoding:'" << growingEncoding << "' }"<< endl;
        return;
    } 
    
    recordEncodingFor(thisNode->leftNode, encodedList, encodedIndex, growingEncoding+"0");
    recordEncodingFor(thisNode->rightNode, encodedList, encodedIndex, growingEncoding+"1");
    
}
encodedValue* fillEncodedList(treeNode* rootNode, int inputLength){
    encodedValue* encodedList = new encodedValue[inputLength];
    int* encodedIndex = new int;
    *encodedIndex = 0;
    recordEncodingFor(rootNode, encodedList, encodedIndex, "");
    return encodedList;
}


////////////////////////////
// Output sorted (by ASCIICode) encoding table
////////////////////////////
void sortEncodedValueList(encodedValue* encodedList, int inputLength){
    ///////////
    //use listElement sorting to sort, and then update the encodedValue list;
    ///////////
    
    int dim = inputLength;
    listElement* inputList = new listElement[dim];
    // Create a list holding the values
    for(int i = 0; i < dim; i++){
        inputList[i].sumFreq = encodedList[i].ASCIICode;
        inputList[i].encodedVal = &encodedList[i]; 
    }
    
    //cout << "before_sort: " ;
    //displayFreqList_spec(inputList, dim);
    
    merge_sort(inputList, 0, inputLength-1, inputLength);
    
    //cout << "after_sort : " ;
    //displayFreqList_spec(inputList, dim);

    encodedValue sortedEncodingList[dim]; // create a new one because values are refereced from encodedList, can not overwrite without data loss
    for(int i = 0; i < dim; i++){
        //cout << " i " << i << " -> " << inputList[i].sumFreq; //<< " - vs - " (*inputList[i].encodedVal).ASCIICode << endl;
        encodedValue thisVal = *inputList[i].encodedVal;
        //cout << " -vs - " << thisVal.ASCIICode;
        sortedEncodingList[i] = thisVal;   
        //cout << "-vs-" << sortedEncodingList[i].ASCIICode << endl;
    }
    
    for(int i = 0; i < dim; i++){
        encodedList[i] = sortedEncodingList[i];   
    }
    
}
void outputSortedEncodingTable(encodedValue* encodedList, int inputLength){
    ////////////////////////
    // Sort encodedValue
    ////////////////////////
    sortEncodedValueList(encodedList, inputLength);
    
    ////////////////////////
    // Output the table, line by line
    ////////////////////////
    encodedValue thisValue;
    std::stringstream buffer;
    buffer << std::setw(10) << "Character" << " | " << std::setw(13) << "ASCII Value" << " | " << std::setw(10) << "Encoding" << endl;
    for(int i = 0; i < 10*3 + 3*3+1; i++){
        buffer << "-";   
    }
    buffer << endl;
    for(int i = 0; i < inputLength; i++){
        thisValue = encodedList[i];
        buffer << std::setw(10) << thisValue.character << " | " << std::setw(13) << thisValue.ASCIICode << " | " << std::setw(10) << thisValue.encoding << endl;
    }
    
    string fullText = buffer.str();
    cout << fullText; 
    
    
    ofstream myfile;
    myfile.open ("codetable.txt");
    myfile << fullText;
    myfile.close();
    
}


int main() {
    //////////////////////////////
    // Initialize charsAndFreqsHolder
    ///////
    int maxASCIIChars = 128;
    int dim = maxASCIIChars;
    aValue* staticValueList = new aValue[dim];
    
  
    //////////////////////////////
    // Open input file of increasing then decreasing integers, one integer per line
    //////////////////////////////
    std::ifstream in_stream;
    in_stream.open("freq.txt");
    if(in_stream.fail()){
        cout << "Error: Could not read input file" << endl;
        string x;
        cin >> x;
        exit(1);  //exit the program
    }
    
    //////////////////////////////
    // Load input values
    //////////////////////////////
    string thisVal;
    aValue thisInputData;
    int thisASCIICode;
    string thisChar;
    int thisFreq;
    int index = 0;
    while (in_stream >> thisVal){
        if(index % 2 == 0 && index != 0){
            thisInputData.ASCIICode = thisASCIICode;
            thisInputData.character = thisChar;
            thisInputData.frequency = thisFreq;
            staticValueList[index/2 - 1] = thisInputData;
            //inputList[index/2 - 1].value = thisInputData;
            //inputList[index/2 - 1].sumFreq = thisFreq;
        }
        if(index % 2 == 0){
            cout << thisVal << " "; 
            thisChar = thisVal;
            if(thisChar == "LF"){
                thisASCIICode = 10;   
            } else {
                thisASCIICode = (int) thisChar[0];   
            }
            cout << "(" << thisASCIICode << ")"  << " ";
        }
        if(index % 2 == 1){
            thisFreq = atoi(thisVal.c_str());
            cout << thisVal << endl;   
        }
        index++;
    }
    index + 1;
    thisInputData.ASCIICode = thisASCIICode;
    thisInputData.character = thisChar;
    thisInputData.frequency = thisFreq;
    staticValueList[index/2 - 1] = thisInputData;
    //inputList[index/2 - 1].value = thisInputData;
    //inputList[index/2 - 1].sumFreq = thisFreq;
    cout << endl;
    int inputLength = (index)/2;
    //cout << "input length = " << inputLength << endl;
    
    
    dim = inputLength;
    listElement* inputList = new listElement[dim];
    // Create a list holding the values
    for(int i = 0; i < dim; i++){
        treeNode* thisNode = new treeNode;
        thisNode->nodeValue = &staticValueList[i];
        inputList[i].sumFreq = staticValueList[i].frequency;
        inputList[i].node = thisNode; 
    }
    
    //cout << "LIST: " ;
    //displayFreqList(inputList, dim);
    //cout << endl;
    
    ////////////////////////////
    // Create binary tree
    ////////////////////////////
    listElement* singleElementList = createBinaryTree(inputList, inputLength);
    
    ////////////////////////////
    // Create table enumerating the encoding for each element, sorted by ASCII index;
    ////////////////////////////
    //treeNode* thisNode = new treeNode;
    //thisNode->nodeValue = &staticValueList[0];
    //encodedValue* encodedList = fillEncodedList(thisNode, inputLength); 
    encodedValue* encodedList = fillEncodedList(singleElementList[0].node, inputLength); 
    cout << endl;
    
    ////////////////////////////
    // Output sorted encoding table
    ////////////////////////////
    outputSortedEncodingTable(encodedList, inputLength);
    cout << endl;
    
    //cout << "hello!" << endl;
    return 0;
}