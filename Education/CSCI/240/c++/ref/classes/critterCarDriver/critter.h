//critter.h
#ifndef CRITTER_H_EXISTS
#define CRITTER_H_EXISTS

#include <string>
using namespace std;

class Critter {
  private:
    string name;
  public:
    void setName(string name);
    string getName();
}; // end class def

#endif