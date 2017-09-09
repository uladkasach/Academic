//basicClass.cpp

#include <iostream>
#include <string>

using namespace std;

class Student {
    private:
        string name;
    public:
      // constructor
 
      Student(){
	name = "Anonymous";
      } // end constructor

      Student(string tName){
        name = tName;
      } // end overloaded constructor

      void setName(string tName){
        name = tName;
      } // end setName

      string getName(){
        return name;
      } // end getName
}; // end class def
//don't forget semicolon at end of class def!


main(){
    Student s1;
    cout << s1.getName() << endl;
    s1.setName("John");
    cout << "Name: " << s1.getName() << endl;
    Student s2 ("Hepzibah");
    cout << s2.getName() << endl;

} // end main