///////////////////////////////////////
//oopHorse.cpp
///////////////////////////////////////
//Build a program that simulates a horse race. Each horse starts at position 0. On each turn, the horse 'flips a coin' (I don't know how horses flip coins, but just go with me for a moment.) Half the time, the horse will advance one step. The other primary entity in this game is the race (or the track, if you prefer.) This object will contain a series of horses. It will also have the ability to start the race. When the race is running, the race class will 'tell' each horse to advance, and will print out a track diagram showing the relative positions of the horses.
///////////////////////////////////////
// Uladzimir Kasacheuski
// 7/15/15
///////////////////////////////////////
//   cd /var/www/CSCi/c++

#include <string>
#include <iostream>
using namespace std;

class Race {
  private:
    int horses[5];
    int horseCount = 0;
  public:
    void setHorse(int horse){
      horses[horseCount] = horse;
      horseCount++;
    } // end setDriver

    string getHorse(int which){
      return horses[which];
    } // end getDriver

}; // end car class def

int main(){
  horse = 5;
  Race theRace;
  theRace.setHorse(horse);
  cout << "Horse: " << theRace.getHorse(0) << endl;
} // end main
