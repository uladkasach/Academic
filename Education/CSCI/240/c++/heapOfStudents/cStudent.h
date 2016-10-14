//cStudent.h
#ifndef CSTUDENT_H_EXISTS
#define CSTUDENT_H_EXISTS

#include <string>
#include "cDate.h"
#include "cAddr.h"


class cStudent {
  private:
    std::string firstName;
    std::string lastName;
    cAddr address;
    cDate birthDate;
    cDate compDate;
    std::string gpa;
    std::string chc;
  public:
    void setVal(std::string, std::string);
    std::string getName(int);
    void setAddr(cAddr);
    cAddr getAddr();
    void setBirthDate(cDate);
    cDate getBirthDate();
    void setCompDate(cDate);
    cDate getCompDate();
    void setExtra(std::string, std::string);
    std::string getExtra(int);
}; // end class def

#endif