## note, must be tested against something with known value, like infinite square well
'''
    
    matrix
        M = matrix
        Psi = vector (eigenfunctions = eigenvectors)
        E = vector (eigenvalues) 
        M * Psi
    
    linear interpolation
        - spline interpolation integration
        
    normalization 
        int modsquared psi_found = int |A|^2 psi_normalized = A^2 -> psi_normalized = 1/sqrt(A) psi_found 

'''


#https://stackoverflow.com/questions/15896588/how-to-change-elements-in-sparse-matrix-in-pythons-scipy

import numpy as np;
import scipy.sparse as sp;
import scipy.sparse.linalg as sparce_linalg;
from scipy import linalg as linalg;
import matplotlib.pyplot as plt;
from scipy.interpolate import UnivariateSpline;
from scipy.integrate import simps;


## scipy.sparse.linalg.eigs - https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigs.html

def build_matrix(n, delta, v_list):
    H_matrix = sp.csr_matrix((n,n));
    for diagonal_index in range(n):
        # main diagonal element
        H_matrix[diagonal_index, diagonal_index] = (2/float(delta**2)) + v_list[diagonal_index];
        
        # lower off diagonal
        lower_off_diagonal = diagonal_index - 1;
        #print(lower_off_diagonal);
        if(lower_off_diagonal >= 0):
            H_matrix[diagonal_index, lower_off_diagonal] = (-1)*(1/float(delta**2));
        
        # higher off diagonal
        higher_off_diagonal = diagonal_index + 1;
        #print(higher_off_diagonal);
        if(higher_off_diagonal < n):
            H_matrix[diagonal_index, higher_off_diagonal] = (-1)*(1/float(delta**2));
        
    print(H_matrix.todense())
    return H_matrix;
    
def solve_matrix(matrix):
    #n = matrix.shape[0];
    
    if(False):
        e_vals, e_vecs = sparce_linalg.eigs(matrix);
    
    if(True):
        matrix = matrix.todense();
        e_vals, e_vecs = linalg.eig(matrix);
        
        ## sort eigvals in increasing and sort vecs by same index
        idx = e_vals.argsort()
        e_vals = e_vals[idx]
        e_vecs = e_vecs[:,idx]
        
        print(e_vecs.shape)
        vecs = [];
        for i in range(e_vecs.shape[0]):
            vecs.append(e_vecs[:, i]);
        e_vecs = vecs;
            
    #print(e_vals);
    #print(e_vecs);
    return [e_vals, e_vecs];
    
def plot_eigenvectors(vectors):
    fig = plt.figure()
    ax = plt.axes()
    for vector in vectors:
        ax.plot(range(len(vector)), np.absolute(vector)**2);
    plt.show()
    

def normalize_eigenvectors(vectors, x_list):    
    ## integrate over spline interpolation of each vector, return the normalization factor, divide each vector by the normalization constant
    
    ## note, for infinite well normalization coefficient = sqrt(2/a)
    print("should be : " + str(np.sqrt(2/float(10))))
    for eig_function in vectors:
        spl = UnivariateSpline(x_list, np.absolute(eig_function)**2);
        integral = spl.integral(x_min, x_max)
        coefficient = 1/np.sqrt(integral); ## since integral over psi*psi should be 1
        print("spline.integral : " + str(coefficient));
        
        integral_simps = simps(np.absolute(eig_function)**2, x_list);
        coefficient = 1/np.sqrt(integral); ## since integral over psi*psi should be 1
        print("simpso.integral : " + str(coefficient));
    
    
x_max = 10;
x_min = 0;
a = x_max - x_min;
n = 1000;
delta_x = (x_max - x_min)/float(n);
x_list = [delta_x*this_n for this_n in range(n)];
print(x_list);
print("N : " + str(n));
print("delta_x -> " + str(delta_x));
v_list = [0]*n; # 


## build matrix
print ("building matrix");
H_matrix = build_matrix(n, delta_x, v_list);
#print(H_matrix);

print ("solve matrix");
vals, vecs = solve_matrix(H_matrix);
## eigen values should be of form n^2*np.pi^2/a^2
print([n**2 * np.pi**2 / a**2 for n in [1,2,3]])
#print(vals);
print(vals);


#print ("plot vectors");
#plot_eigenvectors(vecs[:2]);

print("normalize");
print(x_list);
normalize_eigenvectors(vecs[:2], x_list);

