## note, must be tested against something with known value

#https://stackoverflow.com/questions/15896588/how-to-change-elements-in-sparse-matrix-in-pythons-scipy

import numpy as np;
import scipy.sparse as sp;

def build_matrix(n, delta, v_list):
    H_matrix = sp.csr_matrix((n,n));
    for diagonal_index in range(n):
        # main diagonal element
        H_matrix[diagonal_index, diagonal_index] = (2/float(delta**2)) + v_list[diagonal_index];
        
        # lower off diagonal
        lower_off_diagonal = diagonal_index - 1;
        #print(lower_off_diagonal);
        if(lower_off_diagonal >= 0):
            H_matrix[diagonal_index, lower_off_diagonal] = (1/float(delta));
        
        # higher off diagonal
        higher_off_diagonal = diagonal_index + 1;
        print(higher_off_diagonal);
        if(higher_off_diagonal < n):
            H_matrix[diagonal_index, higher_off_diagonal] = (1/float(delta));
        
    print(H_matrix.todense())

x_max = 10;
x_min = 0;
granularity = 2.5;
n = int((x_max - x_min)/(granularity));
v_list = [1]*n;
build_matrix(n, 3, v_list);


def solve_matrix(matrix):