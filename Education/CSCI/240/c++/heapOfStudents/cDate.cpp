//cDate.cpp
#include <string>
#include <iostream>
#include "cDate.h"


void cDate::setDate(std::string day, std::string month, std::string year){
  cDate::day = day;
  cDate::month = month;
  cDate::year = year;
  //std::cout << "My Address : " << line1 + line2 + city + state + zip  << std::endl;
} //end

std::string cDate::getDate(int which){
    if(which == 0){
        return day; 
    } else if (which == 1){
        return month;
    } else if (which == 2){
        return year;
    } else {
        return "You what? (2) (cDate.cpp - getDate)";   
    }
} // end getName
