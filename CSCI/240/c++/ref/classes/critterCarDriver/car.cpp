//car.cpp

#include <string>
#include "critter.h"
#include "car.h"

void Car::setDriver(Critter driver){
  Car::driver = driver;
  // this is a change
} // end setDriver

string Car::getDriver(){
  return driver.getName();
} // end getDriver

