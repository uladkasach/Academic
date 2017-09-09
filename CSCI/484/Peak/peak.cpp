#include <fstream> 
#include <iostream>     // std::cout
#include <stdlib.h>     // exit()
#include <math.h>       /* floor */
using namespace std;


char get_type(int* list, int index){
    ////////////////////////////////////////////
    // Determine if rising, peak, or falling  ( r, p, or f )
    ////////////////////////////////////////////
    int previous_index = index - 1;
    int following_index = index + 1;
    int previous = list[previous_index];
    int following = list[following_index];
    int current = list[index];
    
    
    //////////////////////////////////////
    // Handle boundary cases
    //////////////////////////////////////
    // Mark boudary cases
    if(previous_index < 0){
        previous_index = -1;  // Means we are at the start of the list. If following is smaller, then this is peak. else, this is rising
    }
    if(following_index > 29){
        following_index = -1; // Means we are at the end of the list. If previous is smaller, then this is peak. else, this is falling
    }
    // test for boundary cases
    if(previous_index == -1){
        if(following < current){
            return 'p';   
        } else {
            return 'r';   
        }
    } 
    if(following_index == -1){
        if(current > previous){
            return 'p';
        } else {
            return 'f';   
        }
    }
    
    //cout << "Here we are!!!!: " << previous << " - " << current << " - " << following << endl;
    //////////////////////////////////////
    // Handle normal cases
    //////////////////////////////////////
    if(previous < current && current < following){
        return 'r';   
    } else if (previous < current && following < current){
        return 'p';
    } else if (previous > current && current > following){
        return 'f';   
    }
    
       
}

int search(int* list, int start_index, int end_index){
    int peak_index = 0;
    
    cout << "Index Inverval : [" << start_index << ", " << end_index << "]" << endl;
    
    
    ////////////////////////
    // Base Case
    ////////////////////////
    if(start_index == end_index){
        cout << "Only one element left to check, it must be the peak." << endl;
        return start_index;   
    }
    
    ///////////////////////
    // Find midpoint
    ///////////////////////
    int list_size = (end_index - start_index);
    int mid_index = floor(list_size/2) + start_index;
    cout << "Mid Point Index : " << mid_index << endl;
    
    
    ///////////////////////
    // Determine if rising, peak, or falling 
    ///////////////////////
    char type = get_type(list, mid_index);
    //cout << "----" << endl;
    cout << "Midpoint type : " << type << endl;
    
    ///////////////////////
    // React appropriately
    ///////////////////////
    if(type == 'p'){
        return mid_index;
    } else if (type == 'r'){
        //peak is infront of mid_point
        start_index = mid_index + 1;
        peak_index = search(list, start_index, end_index);
    } else if (type == 'f'){
        // peak is behind mid_point
        end_index = mid_index - 1;
        peak_index = search(list, start_index, end_index);
    }
    
    
    return peak_index;
}


int main() {
    
    //////////////////////////////
    // Open input file of increasing then decreasing integers, one integer per line
    //////////////////////////////
    std::ifstream in_stream;
    in_stream.open("input.txt");
    if(in_stream.fail()){
      cout << "Error: Could not read input file" << endl;
      exit(1);  //exit the program
    }
    
    //////////////////////////////
    // Load input into an array
    //////////////////////////////
    // Because max n = 30, array size can be simply 30.
    // Keep track of number of elements, to mark boudaries
    int start_index = 0;
    int end_index = 0;
    int *list = new int[30](); // initialize array to all zeros
    int number;
    while (in_stream >> number){
        if(end_index != 0){
            cout << ", ";
        }
        cout << number;
        list[end_index] = number;
        end_index++;
    }
    end_index--;
    cout << endl;
    
    //////////////////////////////
    // Start search
    //////////////////////////////
    int peak_index = search(list, start_index, end_index);
    cout << endl;
    cout << "Peak Index :" << peak_index << endl;
    cout << "Peak Value :" << list[peak_index] << endl;

    return 0;
}