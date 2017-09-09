//cStudent.cpp
#include <string>
#include <iostream>
#include "cAddr.h"
#include "cStudent.h"


void cStudent::setVal(std::string firstName, std::string lastName){
  cStudent::firstName = firstName;
  cStudent::lastName = lastName;
  //std::cout << "Hi Everybody I'm " << firstName << " " << lastName << std::endl;
} //end setName

std::string cStudent::getName(int which){
    if(which == 0){
        return firstName;   
    } else if(which == 1) {
        return lastName;   
    } else {
        return "You What?";   
    }
} // end getName


void cStudent::setAddr(cAddr theAddr){
    //std::cout << theAddr.getAddr(1) << std::endl;
    cStudent::address = theAddr;
}


cAddr cStudent::getAddr(){
    return address;
} // end getName



void cStudent::setBirthDate(cDate theDate){
    //std::cout << theDate.getDate(1) << std::endl;
    cStudent::birthDate = theDate;
}


cDate cStudent::getBirthDate(){
    return birthDate;
} // end getName



void cStudent::setCompDate(cDate theDate){
    //std::cout << theDate.getDate(1) << std::endl;
    cStudent::compDate = theDate;
}


cDate cStudent::getCompDate(){
    return compDate;
} // end getName



void cStudent::setExtra(std::string gpa, std::string chc){
  cStudent::gpa = gpa;
  cStudent::chc = chc;
  //std::cout << "Hi Everybody I'm " << firstName << " " << lastName << std::endl;
} //end setName

std::string cStudent::getExtra(int which){
    if(which == 0){
        return gpa;   
    } else if(which == 1) {
        return chc;   
    } else {
        return "You What?";   
    }
} // end getName
