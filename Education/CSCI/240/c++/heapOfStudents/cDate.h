//cDate.h
#ifndef CDATE_H_EXISTS
#define CDATE_H_EXISTS

#include <string>


class cDate {
  private:
    std::string day;
    std::string month;
    std::string year;
  public:
    void setDate(std::string, std::string, std::string);
    std::string getDate(int);
}; // end class def

#endif