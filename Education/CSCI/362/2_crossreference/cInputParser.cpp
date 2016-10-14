
#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;
#include <fstream> // open files
#include <sstream>
#include "cInputParser.h" 

cInputParser::cInputParser(std::string pathToFile){
    std::ifstream input_stream(pathToFile.c_str());
    std::string line;
    int lineNumber = 1;
    while(std::getline(input_stream, line)){
        //std::cout << line << endl;
        parseThisLine(line, lineNumber);
        lineNumber+= 1;
    }
    theSearchTree.outputTable();
};

void cInputParser::collectThisWord(std::string thisWord, int lineNumber){
    //cout << "Collecting " << thisWord << endl;
    theSearchTree.addWordToTree(thisWord, lineNumber);
}
void cInputParser::parseThisLine(std::string thisLine, int lineNumber){
    /*
        For each line, run through each character. When this character is alpha and last character is not alpha numeric - start new word string. When this character is non alphanumeric and last character was, record the wordstring.
    */
    
    //cout << thisLine.length() << endl;
    
    std::string wordstring = "";
    char lastChar = ' ';
    int total = thisLine.length();
    for(int index = 0; index < total; index ++){
        char thisChar = thisLine[index];
        //cout << "parsing : " <<  thisLine[index] << endl;
        
        /*
        if(isalpha(thisChar)){
            cout << "this is an alpha char"  << endl;   
        }
        if(isalnum(thisChar)){
            cout << "this an alpha numeric char" << endl;   
        }
        if(isalnum(lastChar)){
            cout << "last was an alpha numeric char" << endl;    
        }
        */
        
        //////////////////
        /* 
        Start string if last char was not a alphanum and this char is a alpha char,
        add char to string if it is an alpha num
        */
        //////////////////
        if (isalpha(thisChar) && !isalnum(lastChar)){
            //cout << "New String Starting!" << endl;
            wordstring += thisChar;
        } else if (isalnum(thisChar) && wordstring != "" && wordstring.length() < 10){ // makes sure words that start with numbers arent included and that max word length is 10
            wordstring += thisChar;
        }
        
        // note - expresion below is not else if as the (wordstring != ...) will not run if char is last in line
        ///////////////////
        /* 
        collect word and clear string if wordstring is not empty and this char is not alpha num or is last in line
        */
        if (wordstring != "" && (!isalpha(thisChar) || index + 1 == total)){
            //cout << "String Ended!" << endl << " Here it is : " << wordstring << endl;
            
            //cout << wordstring << "#" << lineNumber << endl;
            collectThisWord(wordstring, lineNumber);
            
            wordstring = ""; // clear wordstring
        }
        
        /*  
        cout << index + 1 << "vs" << total << endl;
        cout << "----" <<  wordstring << endl;
        string result = (wordstring != "") ? "true" : "false";
        cout << result << endl;
        result = (index + 1 == total) ? "true" : "false";
        cout << result << endl;
        */
        
        lastChar = thisChar;
    }
    
    
}
