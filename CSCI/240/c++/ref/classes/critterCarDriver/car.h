//car.h
#ifndef CAR_H_EXISTS
#define CAR_H_EXISTS

//a critter car
#include <string>
#include "critter.h"

class Car {
  private:
    Critter driver;
  public:
    void setDriver(Critter driver);
    string getDriver();
}; // end class def

#endif