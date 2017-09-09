/***********************************************************
PROJECT: FractionADT
FILE: fraction.h
AUTHORS: Designed by R. Fecteau & W.W. Kirchherr
         IMPLEMENTED BY your name here
DATE: Spring, 2002
************************************************************/
#ifndef FRACTION_H
#define FRACTION_H

#include <iostream>

using std::istream;
using std::ostream;
using std::cin;
using std::cout;

/************ Type definitions for ADT Fraction ************/

typedef enum{ POS, NEG } SignType;

class Fraction
{

  private:
    int numerator;    /* numerator and denominator are declared as */
    int denominator;  /* int to simplify the algorithms, but they  */
    SignType sign;    /* will always be stored >= 0                */

  public:

    /********** Constructors, Destructors, and Clone ************/
    Fraction();  /* returns 0/1 */
    Fraction(int n, int d); /* returns n/d */

    /*********************** Accessors **************************/
    int getNumerator();
    int getDenominator();
    char getSign();

    /******************* Modifiers *****************************/
    void setNumerator(int);
    void setDenominator(int);
    void setSign(char);

    /*************** Fraction Operations ***********************/
    void reduceFract();
    static Fraction negateFract( const Fraction &f1);
    static Fraction addFract( const Fraction &f1, const Fraction &f2 );
    static Fraction subFract( const Fraction &f1, const Fraction &f2 );
    static Fraction mulFract( const Fraction &f1, const Fraction &f2 );
    static Fraction divFract( const Fraction &f1, const Fraction &f2 );
    static int compareFract( const Fraction &f1,  const Fraction &f2 );
    /* returns -1 if f1 <  f2
                0 if f1 == f2  
               +1 if f1 >  f2  
    */

    /******************* I/O *********************************/
    static int getFract(istream &infile, Fraction &f);
    /* returns 1 if a valid fraction is read
               0 if an invalid fraction is read 
             EOF if end of file is detected
    */
    static void putFract(ostream &outfile, const Fraction &f );

  // utility functions:
  private:
    static int gcd(int, int);
    void arithmeticSign();
    void standardSign();

};
#endif

Close
Page Saved
Open PocketRemove Page

Save