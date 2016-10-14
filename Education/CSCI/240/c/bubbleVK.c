//bubble.c
//famous bubble sort
//implement the swap algorithm with pointers

#include <stdio.h>
#define MAX 9

//function prototypes
void printValues();
void sort();
void swap(int*, int*);

int values[] = {7, 3, 9, 4, 6, 1, 2, 8, 5};

int main(){
  printf("Before: \n");
  printValues();
  sort();
  printf("After: \n");
  printValues();

  return(0);
} // end main

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