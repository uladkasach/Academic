///////////////////////////////////////
//horseRace.cpp
///////////////////////////////////////
//Build a program that simulates a horse race. Each horse starts at position 0. On each turn, the horse 'flips a coin' (I don't know how horses flip coins, but just go with me for a moment.) Half the time, the horse will advance one step. The other primary entity in this game is the race (or the track, if you prefer.) This object will contain a series of horses. It will also have the ability to start the race. When the race is running, the race class will 'tell' each horse to advance, and will print out a track diagram showing the relative positions of the horses.
///////////////////////////////////////
// Uladzimir Kasacheuski
// 7/15/15
///////////////////////////////////////
//   cd /var/www/CSCi/c++

#include <string>
#include <iostream>     // std::cout
#include <cmath>        // std::abs
#include <time.h>
#include <cstdlib>
#include <sys/time.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;

class Horse {
    private: 
        int id;
        int position;
        int key;
    public:
      Horse(){
          id = 999;
          position = 0;
          key = time(0);
      } // end constructor
      Horse(int newId){
          id = newId;
          position = 0;
          key = time(0);
      } // end overloaded constructor
    
        void setId(int newId){
            id = newId;
        } // end setId
    
        int getId(){  
            return id;
        } // end getId
    
        int getPosition(){
            return position;   
        }
    
        void setPosition(int newPos){
            position = newPos;
        }
    
        void runRound(){
            //cout << "Running Round for horse " << id << endl;   
            srand(time(0));
            int ran = abs(time(0) + rand() * key * (id + 1) % ((id + 5) * 5) ) % 2;
            if(ran == 1){
                key = time(0);   
            }
            position = position + ran;
           // cout << "Num = " << ran << ", position now = " << position << endl;
        }
};// end Horse class def


class Race {
  private:
    Horse horses[5];
    Horse horse;
    int horseCount;
    int length;
    int raceDone;
  public:
    
    Race(){
        horseCount = 0;
        length = 25;
    } // end constructor
    
    void setHorse(Horse horse){
        if(horseCount < 5){
            horses[horseCount] = horse;
            horseCount++;
        }
    } // end setHorse

    
    // getHorse is used in the other functions to select each horse.
    Horse getHorse(int which){
      return horses[which];
    } // end getHorse
    
    
    // start race sets all the race defaults to 0;
    void resetRace(){
        int count = 0;
        raceDone = 0;
        while(count < horseCount){
            horses[count].setPosition(0);
            count ++;
        }
        if(horseCount == 0){
            cout << "No horses have been set yet" << endl;   
        }
    }
    
    // runRaceRound tells each horse to "run" and determine its new position.
    void runRaceRound(){
        int count = 0;
        while(count < horseCount){
            horses[count].runRound();
            count ++;
        }
        if(horseCount == 0){
            cout << "No horses have been set yet" << endl;   
        }
    }
    
    // display race displays the "graphics" of the race.
    void displayRace(){
        int count = 0;
        while(count < horseCount){
            //cout << "Horse " << count << " is at position " << horses[count].getPosition() << " out of " << length << endl;
            int count2 = 0;
            while (count2 < length){
                
                if(horses[count].getPosition() == 25){
                    raceDone = 1; 
                    cout << " Horse " << horses[count].getId() << " has won the race!";
                    count2 = 25;
                } else if(count2 == horses[count].getPosition()){
                    cout << horses[count].getId();   
                } else {
                    cout << "-";
                }
                count2++;
            }
            usleep(125000);
            cout << endl;
            count ++;
        }
        if(horseCount == 0){
            cout << "No horses have been set yet" << endl;   
        }
    }
    
    int checkRaceDone(){
        return raceDone;   
    }
}; // end Race class def

int main(){  
    
  Horse horse1 (0);
  Horse horse2 (1);
  Horse horse3 (2);
  Horse horse4 (3);
  Horse horse5 (4);
  
  Race theRace;

  theRace.setHorse(horse1);
  theRace.setHorse(horse2);
  theRace.setHorse(horse3);
  theRace.setHorse(horse4);
  theRace.setHorse(horse5);
    
  theRace.resetRace();
    
    string value;
    
    while( theRace.checkRaceDone() == 0){
        theRace.displayRace();
        theRace.runRaceRound();
        if(theRace.checkRaceDone() == 1){
            cout << "The race is finished!";
        } else {
            cout << "Press enter for another round";
            cin.ignore();
        }
    }
    
    
} // end main
