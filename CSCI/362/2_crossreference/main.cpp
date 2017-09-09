///////////////////////////////////////
//main.cpp
///////////////////////////////////////
//Cross Reference Index Problem
/*
1) Reads Text File
2) Seperates out Words
3) Stores each word
4) Outputs index table
*/
///////////////////////////////////////
// Implementation 
/*
This program uses 1 data structure - dsBinarySearchTree, with a linked list inside of it.

The program starts by opening a text file, then iterating through each character keeping count of which line it is on and tracking words by building a string upon seeing a alpha character and terminating it when it sees a nonaphanumeric character, retaining the information after termination. Output of the index table is a combination of printing the binary search tree and linked lists found in each node.

*/
// Uladzimir Kasacheuski
// Started 3/27/16
// Completed 3/27/16
///////////////////////////////////////
//   
/*
cd /var/www/CSCi/362/2_crossreference
*/

#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;
#include <fstream> // open files
#include <sstream>



#include "dsBinarySearchTree.h" 
#include "cInputParser.h" 



int main() {
    
    //////////////////////
    // The constructor of input parser object takes the file from relative file path specified as an argument, parses the text, plugs it into a bst, and outputs the table all at once.
    //////////////////////
    cInputParser InputParserObject("0_thefile.txt");
    
    return 0;
}

