/*********************************************************
PROJECT: FractionADT
FILE: testFractFile.cpp - a testing program for ADT Fraction
AUTHORS: Designed by R. Fecteau & W.W. Kirchherr for CS140
DATE: Spring, 2004
************************************************************/

#include <iostream>
#include <fstream>
#include "fraction.h"

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ios;

int main()
{
Fraction f, g, half(1,2), sum, diff, prod, quotient, neg, answer;
bool done = false;
int readResult, cmpResult;
ifstream infile;
char filename[100];

cout << "Enter the name of your data file > ";
cin >> filename;
infile.open(filename,ios::in);
if (infile.fail())
{
  cout << "No such file" << endl;
  exit(1);
}

while ( !done)
{
  readResult = Fraction::getFract( infile, f );
  if ( readResult == -1 ) 
    done = true;
  else
  {
    if (readResult == 0 )
    {
    cout << "Ill formed fraction in file " << filename << endl;
    exit (1); 
  }

  readResult = Fraction::getFract(infile, g);
  if ( readResult == 0 )
  {
    cout << "Ill formed fraction in file " << filename << endl;;
    exit (1); 
  }

  /* Now we have two properly formed fractions */
  neg = Fraction::negateFract(f);
  sum = Fraction::addFract(f,g);
  diff = Fraction::subFract(f,g);
  prod = Fraction::mulFract(f,g);
  quotient = Fraction::divFract(f,g);
	
  cout << "F1 = "; Fraction::putFract(cout, f); cout << endl;
  cout << "F2 = "; Fraction::putFract(cout, g); cout << endl;
  cout << "Neg = "; Fraction::putFract(cout,neg); cout << endl;
  cout << "Sum = "; Fraction::putFract(cout,sum);
  cout << "  Diff = "; Fraction::putFract(cout,diff);
  cout << "  Prod = "; Fraction::putFract(cout,prod);
  cout << "  Quot = "; Fraction::putFract(cout,quotient); cout << endl;
  cmpResult = Fraction::compareFract( f, g );
  if ( cmpResult == 0 ) 
    cout << "equal" << endl;
  else if (cmpResult < 0 ) 
    cout << "less" << endl;
  else 
    cout << "Greater" << endl;
    
  cout << "Try one nested: " << endl;
  answer = Fraction::subFract(
    Fraction::addFract( f,g ),
    Fraction::mulFract(f,Fraction::negateFract(half)));
  cout << "(f + g) - ( f * -(1/2) ) = ";
  Fraction::putFract(cout,answer); cout << endl;
  cout << "===============================================" << endl;			
  f.setNumerator(0);
  f.setDenominator(5);
  f.setSign('+');
  cout << "zero = "; Fraction::putFract(cout,f); cout << endl;
  g = Fraction::negateFract(f);
  cout << "Negative zero = "; Fraction::putFract(cout,g); cout << endl;

  }
}
return 0;
}
