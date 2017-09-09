#include <iostream>
#include "critter.h"
#include "car.h"

using namespace std;

int main(){
  Critter c;
  c.setName("Carlyle");
  cout << c.getName() << endl;

  Car theCar;
  theCar.setDriver(c);
  cout << "driver: " << theCar.getDriver() << endl;
} // end main
