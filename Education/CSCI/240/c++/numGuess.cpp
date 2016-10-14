#include <iostream>
#include <string>
#include <time.h>
#include <cstdlib>
#include <cstring>

using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Uladzimir Kasacheuski - Number Guesser
//////////////////
/// Program utilizes an array to make sure that no numbers are skipped or forgotten. Calculates optimal guessing mid point and guesses every number from 1 - 100 within 7 guesses. 
/// Passes "arrays" into and returns them from functions.
//////////////////////////////////////////////
/// I'm very sorry for the late submission. Work and technology both shot me in the legs and left me stranded before/durring my vacation turning it in.
/// I left for vacation friday and had set 6 hours up on thursday to finish the assignment before I left. Ended up getting surprised with urgent work I had to take care of so I bought mobile data tethering for my phone so i could work on the assignment as I was on the road trip to florida. Not only did i not get data the whole drive down, the inverter I had and the second inverter I had bought on the road down did not charge my laptop for whatever reason.
// Stopped in a small town in the middle of tenessee even to try and get it done before it was too late but the internet there was so bad i was not even able to send you a message explaining the situation.
// I had decided to finish the assignment before sending any messages - and spend a lot of time on it.
// I hope that you will allow me to at least get partial credit for the assignment. I will complete the next assignement in advance regardless.
// Thank you for your time and I hope you understand.



////////////////////////
// This function counts the number of elements in the array by looking for when the value turns to 0.
/////
int countRay(int ray[]){
        int daCount = 0;
        while(ray[daCount] != 0){
            daCount++;
            //cout << "ray" << "["  <<  daCount  <<  "]"  <<  "="  <<  ray[daCount]  << endl; 
        }
        //cout << daCount << endl;  
        return daCount;
}



////////////////////////
// Create an array using the values from the "origRay" (origional array) starting at index = start and ending at index end in origional array. Returns the pointer to the array.
/////
int * makeArray( int origRay[], int start, int end){
    int newRay[100];
    //int length = countRay(origRay);
    int count = 0;
    int total = end;
    while (start < end){
        newRay[count] = origRay[start];
        //cout << "At index " << count << " set equal to index " << start << " ( " << origRay[start] << endl;
        start++;
        count++;   
    }
    while(count < 100){
        newRay[count] = 0;    
        //cout << "At index " << count << " set equal to 0 " << endl;
        count++;   
    }
    //newRay[count] = 0;
    int length = countRay(newRay);
    //cout << "Length = " << length << endl;  
    return  newRay; 
}

 

main(){
    
    ////////////////////////
    // Initialize the array of possible numbers and end array on a 0 - so that count array function can look for the 0 as the stopping point.
    //////
    int ray[100];
    int count = 0;
    int total = 100;
    while(count < total){
        ray[count] = count+1;
        //cout << count+1 << endl;
        count++;
    }
    ray[count] = 0;
    
    int tries = 0;
    int run = 1;
    while( run == 1 ){

        ////////////////////////
        // Get the length of the array.
        /////
        tries++;
        int length = countRay(ray);
        //cout << "length = " << length << endl;
        
        if(length == 0){
            cout << "Hmmm... it appears that it is not a number from 1-100. Those are the only numbers I'm built to guess. Run me again if you want to play more. Next time, please pick a number from 1 - 100." << endl << endl;
            run = 0;
            return 0;
        }
        
        
        
        ////////////////////////
        // Set the "Key" variable. Key is the index number for the integer that will be chosen as a guess. Purpose is to select a number at the exact center and evenly off for each number to enable acuracy within 7 guesses. Use both devision and the remainder to evenly pass through the array with guesses. Without accounting for the remainder - the program will only guess 100 with 8 turns.
        /////
        int key = length/2;
        int remainder = length%2;    
        //cout << "remainder = " << remainder << endl;
        if(key != 0 && remainder == 0){
            key = key - 1;   
        }
        //cout << " Key == " << key << endl;
        

        
        ////////////////////////
        // Generate a "guess" by plugging in the key index variable into the array of eligible numbers.
        /////
        int guess = ray[key];        
        //cout << "guess = " << guess << endl;
        
        
        ////////////////////////
        // Get the users feed back
        /////
        cout << endl << "Is your number ";
        cout << guess;
        cout << "?" << endl;
        cout << "H = too high, L = too low, C = correct" << endl;
        string response;
        cin >> response;
        
        ////////////////////////
        //Parse the users feedback
        /////
    
        if(response == "L" || response == "l"){
            cout << "Too Low..." << endl;
            
            ////////////////////////
            // The next two lines are used for setting the array. For some reason setting them below the makeArray function results in an inacurate resulting array.
            /////
            int count = 0;
            //cout << "Count = " << count << endl;
            
            ////////////////////////
            // Make an array that removes all the integers below and including the guess number.
            /////
            int *newRay;
            newRay = makeArray(ray, key+1 , length);
            
            ////////////////////////
            // Set the main array equal to the new array created.  
            /////
            while(count < 100){
                ray[count] = newRay[count];
                count++;   
            }
            
            //out << ray << endl;
            //cout << countRay(ray) << endl;
            //cout << "done" << endl;
            
        } else if (response == "H" || response == "h"){
            
             cout << "Too High..." << endl;
            
            ////////////////////////
            // The next two lines are used for setting the array. For some reason setting them below the makeArray function results in an inacurate resulting array.
            /////
            int count = 0;
            //cout << "Count = " << count << endl;
            
            ////////////////////////
            // Make an array that removes all the integers above and including the guess number.
            /////
            int *newRay;
            newRay = makeArray(ray, 0 , key);
            
            ////////////////////////
            // Set the main array equal to the new array created.  
            /////
            while(count < 100){
                ray[count] = newRay[count];
                count++;   
            }
            
            //out << ray << endl;
            //cout << countRay(ray) << endl;
            //cout << "done" << endl;
            
            
            
        } else if (response == "C" || response == "c"){
            run = 0;
            cout << "Hooray!!!" << endl << "That only took " << tries << " tries!";
        } else {
            cout << "I'm sorry, I didn't understand that. Try again please." << endl;
        }
        
        cout << endl;
        
    }
    
    
} // end main

