#include <fstream> 
#include <iostream>     // std::cout
#include <stdlib.h>     // exit()
#include <math.h>       /* floor */
#include <sstream>
namespace patch 
{
    // patch::to_string()
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}
using namespace std;





int maxNewSubLength(int i, int* list, int* lengths){
    int iVal = list[i];
    int maxSubLength = 0;
    int thisVal;
    for(int j = 0; j < i; j++){
        thisVal = list[j];
        if(thisVal < iVal && maxSubLength < lengths[j]){
            maxSubLength = lengths[j];   
        }
    }
    return maxSubLength + 1;
}


int maxNewSubIndex(int i, int* list, int* lengths){
    int iVal = list[i];
    int maxSubLength = 0;
    int maxSubIndex = -1;
    int thisVal;
    for(int j = 0; j < i; j++){
        thisVal = list[j];
        if(thisVal < iVal && maxSubLength < lengths[j]){
            //cout << "Found one" << endl;
            maxSubLength = lengths[j];   
            maxSubIndex = j;
        }
    }
    return maxSubIndex;
}


int main() {
    //////////////////////////////
    // Open input file of increasing then decreasing integers, one integer per line
    //////////////////////////////
    std::ifstream in_stream;
    in_stream.open("incseq.txt");
    if(in_stream.fail()){
      cout << "Error: Could not read input file" << endl;
      exit(1);  //exit the program
    }
    
    //////////////////////////////
    // Load input into an array
    //////////////////////////////
    int inputLength = 0;
    int number;
    int index = 0;
    int *list;
    bool first_read = true;
    while (in_stream >> number){
        if(first_read == true){
            inputLength = number;
            list = new int[inputLength](); // initialize the list with size defined in input file
            first_read = false;
            continue;
        }
        if(index != 0){
            cout << ", ";
        }
        cout << number;
        list[index] = number;
        index++;
    }
    cout << endl;
    
    //////////////////////////////
    // Find max sub sequence
    //////////////////////////////
    int *lengths = new int[inputLength]();
    string *subsequences = new string[inputLength];
    int maxLength = 0;
    string maxSubSequence = "";
    int lengthForSubIndex;
    string subForSubIndex;
    for(int i = 0; i < inputLength; i++){
        //lengths[i] = maxNewSubLength(i, list, lengths);
        int thisSubIndex = maxNewSubIndex(i, list, lengths);

        //cout << thisSubIndex << endl;
        if(thisSubIndex == -1){
            lengthForSubIndex = 0;
            subForSubIndex = "";
        } else {
            lengthForSubIndex = lengths[thisSubIndex];
            subForSubIndex = subsequences[thisSubIndex];
        }
        
        //cout << lengthForSubIndex + 1 << endl;
        lengths[i] = lengthForSubIndex + 1;
        subsequences[i] = subForSubIndex + " " + patch::to_string(list[i]);
        if(lengths[i] > maxLength){
            maxLength = lengths[i];   
            maxSubSequence = subsequences[i];
        }
    }
    
    //////////////////////////////
    // Output results
    //////////////////////////////
    cout << maxLength << endl;
    cout << maxSubSequence << endl;
    return 0;
}