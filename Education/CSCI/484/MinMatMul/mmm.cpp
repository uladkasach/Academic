#include <fstream> 
#include <iostream>     // std::cout
#include <iomanip>      // std::setw()
#include <stdlib.h>     // exit()
#include <math.h>       /* floor */
#include <string> 
#include <sstream>

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

using namespace std;


struct AMatrix {
    int rowCount;
    int colCount;
};
    

int** instantiateTheMatrix(int dim){
    int sizeY;
    int sizeX;
    sizeY = sizeX = dim;
    
    int** matrix = new int*[sizeY];
    for(int i = 0; i < sizeY; ++i) {
        matrix[i] = new int[sizeX];
    }
    
    for(int i = 0; i < sizeY; ++i){
        for(int j = 0; j < sizeX; ++j){
            if(i == j){
                matrix[i][j] = 0;
            } else if (i < j){
                matrix[i][j] = -2; //Unchanged
            } else if (i > j){
                matrix[i][j] = -1; //X  
            }
        }
    }
    return matrix;
}

void printTheMatrix(int** matrix, int dim){
    int sizeY;
    int sizeX;
    sizeY = sizeX = dim;
    int thisValue;
    //cout << "The Matrix : "<< endl;
    for(int i = 0; i < sizeY; ++i){
        for(int j = 0; j < sizeX; ++j){
            thisValue = matrix[i][j];
            cout << " " << std::setw(10) << thisValue << " ";
        }
        cout << endl;
    }
}

int findWorkForMultiplying(int i, int k, int j, int** minWorkMatrix, AMatrix* inputMatricies){
    //cout << " { " << i << " , " << k << " , " << j << " } " << endl;
    int previousWork1 = minWorkMatrix[i][k];
    int previousWork2 = minWorkMatrix[k+1][j];
    if(previousWork1 < 0){
        cout << "There has been some error - previous work 1 resulted < 0: " << previousWork1 << endl;   
    }
    if(previousWork2 < 0){
        cout << "There has been some error - previous work 2 resulted < 0: " << previousWork2 << endl;  
    }
    int thisWork = inputMatricies[i].rowCount * inputMatricies[k].colCount * inputMatricies[j].colCount;
    return previousWork1 + previousWork2 + thisWork;
}

void fillMinimumForElement(int** minWorkMatrix, int** minKMatrix, int thisI, int thisJ, int dim, AMatrix* inputMatricies){
    ////////////////////////
    // Find minimum work for multiplying matricies (A_i through A_k) and (A_k+1 through A_j),
    //      for i <= k < j
    ////////////////////////
    int thisK = thisI;
    int minWorkValue = 99999999;
    int minK = -2;
    int thisWork;
    for(int thisK = thisI; thisK < thisJ; ++thisK){
        thisWork = findWorkForMultiplying(thisI, thisK, thisJ, minWorkMatrix, inputMatricies);
        if(thisWork < minWorkValue){
            minWorkValue = thisWork;
            minK = thisK;
        }
    }
    minWorkMatrix[thisI][thisJ] = minWorkValue;
    minKMatrix[thisI][thisJ] = minK;
}

void fillTheMatricies(int** minWorkMatrix, int** minKMatrix, int dim, AMatrix* inputMatricies){
    
    /////////////////////
    // Traverse each element by the diagonals
    /////////////////////
    int thisI;
    int thisJ;
    for(int diagonal = 1; diagonal < dim; ++diagonal){
        //cout << "Diagonal " << diagonal << endl;
        for(int thisIndex = 0; thisIndex < dim - diagonal; ++thisIndex){
            thisI = thisIndex;
            thisJ = thisIndex+diagonal;
            //cout << "This : { " << thisI << " , " << thisJ << " } " << endl;
            fillMinimumForElement(minWorkMatrix, minKMatrix, thisI, thisJ, dim, inputMatricies);
        }
        //printTheMatrix(minWorkMatrix, dim);
    }
}

string returnTheParentheticalOrdering(int** minKMatrix, int start, int end){
    if(start == end){
        return patch::to_string(start);   
    }
    if(start == end - 1){
        return patch::to_string(start) + "*" + patch::to_string(end); 
    }
    int kVal = minKMatrix[start][end];
    string result = "(" + returnTheParentheticalOrdering(minKMatrix, start, kVal) + ")(" + returnTheParentheticalOrdering(minKMatrix, kVal+1, end) + ")"; 
    return result;
}

int main() {
    /*///////////////////////////////
    Given N matricies, (row x column = n x m) , find the smallest grouping.
    
    1) Construct 2 matricies, one for the minimum multiplication value of a grouping, one for at which k the minimum value for that grouping was found.
    
    2) Build the matricies, iterate by going through each element by diagonals
    
    3) Output table 1
    4) Output table 2
    5) Output the grouping to get the min
    *////////////////////////////////
    
    /////////////////////////////////////////////
    // Get input
    /////////////////////////////////////////////
    int inputMatriciesCount = 6;
    int dim = inputMatriciesCount;
    AMatrix* inputMatricies = new AMatrix[dim];
    inputMatricies[0].rowCount = 10;
    inputMatricies[0].colCount = 17;
    
    inputMatricies[1].rowCount = 17;
    inputMatricies[1].colCount = 12;
    
    inputMatricies[2].rowCount = 12;
    inputMatricies[2].colCount = 25;
    
    inputMatricies[3].rowCount = 25;
    inputMatricies[3].colCount = 14;
    
    inputMatricies[4].rowCount = 14;
    inputMatricies[4].colCount = 30;
    
    inputMatricies[5].rowCount = 30;
    inputMatricies[5].colCount = 15;
    
    inputMatricies[5].rowCount = 15;
    inputMatricies[5].colCount = 9;
    
    
    /////////////////////////////////////////////
    // Setup Matrixes
    /////////////////////////////////////////////
    int** minWorkMatrix = instantiateTheMatrix(dim);
    int** minKMatrix = instantiateTheMatrix(dim);
    //printTheMatrix(minWorkMatrix, dim);
    
    
    /////////////////////////////////////////////
    // Find the values
    /////////////////////////////////////////////
    fillTheMatricies(minWorkMatrix, minKMatrix, dim, inputMatricies);
    cout << "----" << endl;
    cout << "Minimal Work Table : " << endl;
    printTheMatrix(minWorkMatrix, dim);
    cout << "----" << endl;
    //printTheMatrix(minKMatrix, dim);
    cout << "Minimum Work Required : " << endl << minWorkMatrix[0][dim-1] << endl; 
    
    /////////////////////////////////////////////
    // Display the parenthetical ordering
    /////////////////////////////////////////////
    cout << "----" << endl;
    cout << "Minimal Work Parenthetical Ordering : " << endl;
    cout << returnTheParentheticalOrdering(minKMatrix, 0, dim-1) << endl;
    cout << "----" << endl;
    
    //cout << "hello!" << endl;
    return 0;
}