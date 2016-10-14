//cAddr.cpp
#include <string>
#include <iostream>
#include "cAddr.h"


void cAddr::setAddr(std::string line1, std::string line2, std::string city, std::string state, std::string zip){
  cAddr::line1 = line1;
  cAddr::line2 = line2;
  cAddr::city = city;
  cAddr::state = state;
  cAddr::zip = zip;
  //std::cout << "My Address : " << line1 + line2 + city + state + zip  << std::endl;
} //end

std::string cAddr::getAddr(int which){
    if(which == 0){
        return line1; 
    } else if (which == 1){
        return line2;
    } else if (which == 2){
        return city;
    } else if (which == 3){
        return state;
    } else if (which == 4){
        return zip;
    } else {
        return "You what? (cAddr.cpp - getAddr)";   
    }
} // end getName
