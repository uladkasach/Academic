// Uladzimir Kasacheuski
//bubble.c
//famous bubble sort
//implement the swap algorithm with pointers

// Black Belt Edition
// Using combination of srand(time(NULL));, rand()%total;, and shuffling to create random numbers

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX 9



// Create Random Integers




//function prototypes
void printValues();
void sort();
void swap(int*, int*);
void generateValues();






int values[] = {7, 3, 9, 4, 6, 1, 2, 8, 5};

int main(){

  generateValues();
    
  printf("Before: \n");
  printValues();
  sort();
  printf("After: \n");
  printValues();

  return(0);
} // end main





void generateValues(){
    
    srand(time(NULL));
    
    int count = 0;
    int total = 100;
    while(count < total){
        values[count] = count;
        count += 1;   
    }
    
    while(0 < total){
      // generate random index
      int w = rand()%total;
      // swap items
      int t = values[total];
      values[total] = values[w];
      values[w] = t;
        
      total -= 1;
    }
    
    
}

void printValues(){
    int count = 0;
    int max = MAX;
    //printf("count = %d ---- max = %d", count, max);
    printf(" [ ");
    while(count < max){
        //printf("count = %d",count);
        printf("%d ", values[count]);
        count += 1;   
    }
    printf("]\n");
}

void sort(){
    int count1 = 0;
    int count2;
    int max = MAX-1;
    while(count1 < max){
        count2 = 0;
        while(count2 < max){
            if(values[count2] > values[count2+1]){
                int* v1 =  &values[count2];
                int* v2 =  &values[count2+1];
                swap (v1, v2);
                printValues();
            }
            //printf("%d ", values[count2]);
            count2 += 1;
           // printf(" %d\n",count2);
        }
        count1 += 1;   
       // printf("count1 = %d\n",count1);
    }
}

void swap(int* v1, int* v2){
    int hold = *v2;
    *v2 = *v1;
    *v1 = hold;
}