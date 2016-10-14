//critterOneFile.cpp
//illustrate how critter example could be written in one file

#include <string>
#include <iostream>
using namespace std;

class Critter {
  private:
    string name;
  public:
    void setName(string name){
      Critter::name = name;
    } // end setName

    string getName(){
      return name;
    } // end getName
}; // end critter class def

class Car {
  private:
    Critter driver;
  public:
    void setDriver(Critter driver){
      Car::driver = driver;
    } // end setDriver

    string getDriver(){
      return driver.getName();
    } // end getDriver

}; // end car class def

int main(){
  Critter c;
  c.setName("George");
  cout << "critter: " << c.getName() << endl;

  Car theCar;
  theCar.setDriver(c);
  cout << "driver: " << theCar.getDriver() << endl;
} // end main
