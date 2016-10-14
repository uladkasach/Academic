//cppFormatted
//convert class to C++-style format

#include <iostream>
#include <string>

using namespace std;

//begin with class prototype

class Student {
    private:
        string name;
    public:
      Student();
      Student(string);
  void setName(string);
  string getName();
}; // end class def

//functions defined seperate from class definition!
//note use of scope operator

Student::Student(){
  Student::name = "Anonymous";
} // end constructor

Student::Student(string name){
  Student::setName(name);
} // end overloaded constructor
 
//scope operator removes need for tName
void Student::setName(string name){
  Student::name = name;
} // end setName

string Student::getName(){
  return name;
} // end getName

main(){
  //classes can be instantiated without parameters
  //in C++, you must always provide a null parameter constructor
  //or one will be created for you.  

  Student s1;
  cout << s1.getName() << endl;
  s1.setName("John");
  cout << "Name: " << s1.getName() << endl;
  Student s2 ("Hepzibah");
  cout << s2.getName() << endl;

} // end main