//cAddr.h
#ifndef CADDR_H_EXISTS
#define CADDR_H_EXISTS

#include <string>


class cAddr {
  private:
    std::string line1;
    std::string line2;
    std::string city;
    std::string state;
    std::string zip;
  public:
    void setAddr(std::string, std::string, std::string, std::string, std::string);
    std::string getAddr(int);
}; // end class def

#endif