//pointers.c

#include <stdio.h>

int main(){
    // you can extract address of ordinary variable
    // with & operator
    int a = 5;
    printf("value of a: %d \n", a);
    printf("address of a: %d \n", &a);

    // * in definition is 'pointer'
    // * in code is 'value at'
    int* pA = &a;
    printf("value OF pA: %d \n", pA);
    printf("value AT pA: %d \n", *pA);

    // You can have a pointer to a pointer!
    int ** ppA = &pA;
    printf("value OF ppA: %d \n", ppA);
    printf("value AT ppA: %d \n", *ppA);
    printf("value AT value AT ppA: %d \n", **ppA);
} // end main