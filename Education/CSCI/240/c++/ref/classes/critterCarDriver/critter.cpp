//critter.cpp
#include <string>
#include <iostream>
#include "critter.h"

using namespace std;

void Critter::setName(string name){
  Critter::name = name;
  cout << "Hi Everybody" << endl;
} //end setName

string Critter::getName(){
  return name;
} // end getName
