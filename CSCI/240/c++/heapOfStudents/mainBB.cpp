///////////////////////////////////////
// Heap Of Students Project
// main.cpp
///////////////////////////////////////
// Uladzimir Kasacheuski
// 7/24/15
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
/////// Objectives :
///////////////////////////////////////
// Load Data From Data File data.dat
//     -  Store it In a Student Class stored on the heap
//             - Student class consists of 3 classes and 4 variables
// List Student Data in full report
// List Student Data in mini report
// Sort Data Alphabetically ( after which when you list the student data again, it will display in alphabetical order)
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//   cd /var/www/CSCi/c++/heapOfStudents


#include <iostream>
#include <fstream>
#include "cStudent.h"
#include "cDate.h"
#include "cAddr.h"
//using namespace std;
// opting in favor of less global variables. (Good for learning purposes too.)
// std::cin
// std::cout


// Break String Up By A Delimitor.
// Returns a pointer to the array. 
//Ends array with string "||thisIsTheEnd||".
std::string * explodeStr(std::string theString, std::string delimiter){
    //std::cout << "Starting - Splitting up string by \"" << delimiter << "\"" << std::endl;   
    int count = 0;
    int total = theString.size();
    int foundDelimiter = 0;
    while(count < total){
        //std::cout << " char [" << count << "] = {"<< theString[count] << "}" << std::endl;
        if(theString[count] == delimiter[0]){
            foundDelimiter++;   
            //std::cout << "Found " << foundDelimiter << " now" << std::endl;
        }
        count++;
    }
    std::string *theArray = new std::string[foundDelimiter+2];
    //std::cout << "Found a total of " << foundDelimiter << std::endl;
    //std::string theArray[foundDelimiter+2];
    count = 0;
    // total is already set.
    std::string newPart = "";
    int arrayCount = 0;
    while(count < total){
        if(theString[count] == delimiter[0]){
            //std::cout << "Just added " << newPart << std::endl;
            theArray[arrayCount] = newPart;
            arrayCount++;
            newPart = "";
        } else {
            newPart = newPart + theString[count];   
        }
        count++;   
    }
    //std::cout << "Just added " << newPart << std::endl;
    theArray[arrayCount] = newPart; 
    arrayCount++;
    newPart = "";
    theArray[arrayCount] = "||thisIsTheEnd||";
    //std::string *theArrayPts = new std::string[foundDelimiter+2];
    //theArrayPts = theArray;
    //std::cout << theArrayPts[0] << std::endl;
    //std::cout << theArray[0] << std::endl;
    return theArray;
}




cStudent * parseThisLine(std::string line){
    //std::cout << "\n\n -- " << line << std::endl;
    std::string *theArray = explodeStr(line, ",");
    //std::cout << theArray[2] << std::endl;
    
    cStudent *newStudent = new cStudent;
    newStudent->setVal(theArray[0],theArray[1]);
        //std::cout << newStudent->getName(1) << std::endl;
    
    cAddr newAddr;
    newAddr.setAddr(theArray[2], theArray[3], theArray[4], theArray[5], theArray[6]);
    newStudent->setAddr(newAddr);
        //std::cout << newStudent->getAddr().getAddr(0) << std::endl;
    
    cDate birthDate;    
    std::string *theDateArray = explodeStr(theArray[7], "/");
    // For all dates that are invalid. /////////////////////////////////////////////////////////
    if(theDateArray[1] == "||thisIsTheEnd||"){
        birthDate.setDate("N/A","N/A","N/A");
    } else {
        birthDate.setDate(theDateArray[0],theDateArray[1],theDateArray[2]);
    }
    newStudent->setBirthDate(birthDate);
        //std::cout << newStudent->getBirthDate().getDate(2) << std::endl;
    
    cDate compDate;    
    std::string *theDateArray2 = explodeStr(theArray[8], "/");
    // For all dates that are invalid. /////////////////////////////////////////////////////////
    if(theDateArray2[1] == "||thisIsTheEnd||"){
        compDate.setDate("N/A","N/A","N/A");
    } else {
        compDate.setDate(theDateArray2[0],theDateArray2[1],theDateArray2[2]);
    }
    newStudent->setCompDate(compDate);
        //std::cout << newStudent->getCompDate().getDate(2) << std::endl;
    
    newStudent->setExtra(theArray[9], theArray[10]);
        //std::cout << newStudent->getExtra(1) << std::endl;
    
    delete[] theArray;
    
    return newStudent;
}


cStudent * loadTheData(){
      //std::cout << "Boo Buddy" << std::endl; 
      std::string line;
      std::ifstream myfile ("./data.dat");

    int total = 0;
      if (myfile.is_open()){
            while ( getline(myfile,line) ){
                total++;
            }
           //std::cout << total << std::endl;
          

               myfile.clear();
               myfile.seekg(0);
              cStudent *allStudents = new cStudent[total];
              int count = 0;
               while ( getline(myfile,line) ){
                       if(count != 0){
                         cStudent *thisStudent = parseThisLine(line);
                         allStudents[count-1] = *thisStudent;  
                         //std::cout << thisStudent->getName(1) << std::endl;
                       }
                     count++;
                }
                myfile.close();

                //std::cout << allStudents[0].getName(0) << std::endl;
          
                //std::cout << &allStudents << std::endl;
          
                //cStudent * link = allStudents;
                //std::cout << link[0].getName(0) << std::endl;
                
          
                return allStudents;
              
      } else {
          std::cout << "Unable to open file"; 
      }
    
        
}



int countTheData(){
      std::string line;
      std::ifstream myfile ("./data.dat");
    int total = 0;
      if (myfile.is_open()){
            while ( getline(myfile,line) ){
                total++;
            }
            return total;
      } else {
          std::cout << "Unable to open file"; 
      }
}


void displayMiniReport(cStudent * allStudents, int total){
    int count = 0;
    while(count < total-1){
        std::cout << allStudents[count].getName(1) << ", " << allStudents[count].getName(0) << std::endl;
        count++;   
    }
}

void displayFullReport(cStudent * allStudents, int total){
    int count = 0;
    while(count < total-1){
        std::cout << "NAME        : " << allStudents[count].getName(1) << ", " << allStudents[count].getName(0) << std::endl;
        std::cout << "ADDRESS     : " << allStudents[count].getAddr().getAddr(0) << " " << allStudents[count].getAddr().getAddr(1) << std::endl;
        std::cout << "              " << allStudents[count].getAddr().getAddr(2) << ", " << allStudents[count].getAddr().getAddr(3) << " " << allStudents[count].getAddr().getAddr(4) << std::endl;
        std::cout << "BIRTHDAY    : " << allStudents[count].getBirthDate().getDate(0) << "/" << allStudents[count].getBirthDate().getDate(1) << "/" << allStudents[count].getBirthDate().getDate(2) << std::endl;
        std::cout << "A. C. DATE  : " << allStudents[count].getCompDate().getDate(0) << "/" << allStudents[count].getCompDate().getDate(1) << "/" << allStudents[count].getCompDate().getDate(2) << std::endl;
        std::cout << "GPA         : " << allStudents[count].getExtra(0)  << std::endl;
        std::cout << "C. H. COMP. : " << allStudents[count].getExtra(1)  << std::endl;
        
        
        std::cout  << std::endl;
        count++;   
    }
}


cStudent * alphabetize(cStudent * allStudents, int total){
    cStudent * newAllStudents = new cStudent[total];
    int count = 0;
    int count2;
    int lowestIndex;
    std::string lowestName;
    std::string thisName;
    while(count < total-1){
        count2 = 0;
        while(count2 < total-1){
            if(count2 == 0){
                lowestName = "ZZZZ";   
            }
            thisName = allStudents[count2].getName(1);
            //std::cout << "Is " << thisName << " lower than " << lowestName << "?" << std::endl;
            if(thisName < lowestName && thisName != "||DONE||"){
                   //std::cout << "Yes!" << std::endl;
                   lowestName = thisName;
                   lowestIndex = count2;
            } else {
                   //std::cout << "No!" << std::endl;
            }
            count2++;
        }
        newAllStudents[count] = allStudents[lowestIndex];
        allStudents[lowestIndex].setVal("||DONE||","||DONE||");
        count ++;   
    }
    return newAllStudents;
}

int main(){
    
// Load Data From Data File data.dat
//     -  Store it In a Student Class stored on the heap
//             - Student class consists of 3 classes and 4 variables
    cStudent * allStudents = loadTheData();
    int total = countTheData();
    // Exaple of calling the data.    
    //std::cout << "" << allStudents[0].getAddr().getAddr(0) << std::endl;
    std::cout  << std::endl;
    std::cout  << std::endl;
    std::cout  << std::endl;
    std::cout << "Hello!asdfasdfas" << std::endl << "Your student data has been loaded. What would you like to do with it?" << std::endl;
    int running = 1;
    int count = 0;
    while(running == 1){
        if(count > 0){
            std::cout  << std::endl;
            std::cout  << std::endl;
            std::cout << "Great!" << std::endl << "What else would you like to do?" << std::endl;
        }
        std::cout << "Enter 1 for a full report, enter 2 for a mini report, enter 3 to alphabetize the data, and 4 to exit." << std::endl;

        std::string response;
        std::cin >> response;


        if(response == "1"){
            std::cout << "You've requested a full report. Here it is : " << std::endl;
            std::cout  << std::endl;
            std::cout << "|||||||||||||||||||||||||||||||||||||||";
            std::cout  << std::endl;
            displayFullReport(allStudents, total);
            std::cout << "|||||||||||||||||||||||||||||||||||||||";
            std::cout  << std::endl;
            std::cout  << std::endl;
        } else if (response == "2"){
            std::cout << "You've requested a mini report. Here it is : " << std::endl; 
            std::cout  << std::endl;
            std::cout << "|||||||||||||||||||||||||||||||||||||||";
            std::cout  << std::endl;
            displayMiniReport(allStudents, total);
            std::cout << "|||||||||||||||||||||||||||||||||||||||";
            std::cout  << std::endl;
            std::cout  << std::endl;
        } else if (response == "3"){
            std::cout  << std::endl;
            std::cout  << std::endl;
            std::cout << "Okay! Alphabetizing the data by last name now..." << std::endl; 
            std::cout  << std::endl;
            allStudents = alphabetize(allStudents, total);
            std::cout << "All done. Next time you display a report the data will be sorted alphabetically by last name." << std::endl; 
        } else if (response == "4" || response == "exit"){
            running = 0;
        } else {
            std::cout << "Sorry, I dont understand that command. Please try again." << std::endl;   
        }
        std::cout << std::endl;
        
        count++;
        if(count > 500){
            std::cout << "Terminating the session because we've made 500 calls already. Start me again if you need to do more work." << std::endl;  
            running = 0;   
        }
    }
    return 0;
}