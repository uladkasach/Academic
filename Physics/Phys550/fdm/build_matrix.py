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


        NOTE: h_bar^2/2m is not defined

        conversion factor - x = x/a s.t. in real space potential is between 0 and a
        then eigenvalues are 1/a^2 -> but when transforming into actual energy, keep track that x_max represents a
        for potential to, when potential must be in units of energy

Note - with time evolution must choose correct order of magnitude of delta_t
'''


#https://stackoverflow.com/questions/15896588/how-to-change-elements-in-sparse-matrix-in-pythons-scipy

import numpy as np;
import scipy.sparse as sp;
import scipy.sparse.linalg as sparce_linalg;
from scipy import linalg as linalg;
import matplotlib.pyplot as plt;
from scipy.interpolate import UnivariateSpline;
from scipy.integrate import simps;
import pickle;  # for caching

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


def plot_eigenvectors(vectors, x_list):
    fig = plt.figure()
    ax = plt.axes()
    for vector in vectors:
        ax.plot(x_list, np.absolute(vector)**2);
    plt.show(block=False)


def plot_spline(spline, x_list):
    xs = x_list;
    #print(range(n))
    ys = spline(xs);
    fig = plt.figure()
    plt.plot(xs, ys)
    plt.show(block=False)

def normalize_eigenvectors(vectors, x_list):
    ## integrate over spline interpolation of each vector, return the normalization factor, divide each vector by the normalization constant

    print(a);
    normalized_vectors = [];
    ## note, for infinite well normalization coefficient = sqrt(2/a)
    for eig_function in vectors:
        spl = UnivariateSpline(x_list, np.absolute(eig_function)**2, s=0);
        integral = spl.integral(x_min, x_max)
        coefficient = 1/np.sqrt(integral); ## since integral over psi*psi should be 1
        print("spline.integral : " + str(coefficient));

        #plot_eigenvectors([eig_function], x_list);
        #plot_spline(spl, x_list);

        if(False):
            integral = simps(np.absolute(eig_function)**2, x_list);
            coefficient = 1/np.sqrt(integral); ## since integral over psi*psi should be 1
            print("simpso.integral : " + str(coefficient));

        normalized_vectors.append(eig_function*coefficient);



    return normalized_vectors;

x_max = 10; # angstrom
x_min = 0; # angstrom
n = 1000;
delta_x = (x_max - x_min)/float(n);
a = (x_max - x_min);
x_list = [delta_x*this_n for this_n in range(n)];
print("N : " + str(n));
print("delta_x -> " + str(delta_x));

if(False): ## infinite square well potential
    v_list = [0]*n;
else:
    E_n_inf_square_well = 50**2 * np.pi**2 / a**2;
    V_0 = E_n_inf_square_well;
    v_list = [0]*n;
    for index in np.arange(int(n/2), n, 1): # from n/2 to n in steps of 1
        v_list[index] = V_0; ## set the potential to be equal to V_0
    #print(v_list);
load_from_cache = dict({
    "eigen" : False,
});

## build matrix
print ("building matrix");
H_matrix = build_matrix(n, delta_x, v_list);
#print(H_matrix);

if(load_from_cache["eigen"] == False):
    print ("solve matrix");
    vals, vecs = solve_matrix(H_matrix);
    with open('.cache/vals.pk', 'wb+') as handle:
        pickle.dump(vals, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('.cache/vecs.pk', 'wb+') as handle:
        pickle.dump(vecs, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    with open('.cache/vals.pk', 'rb') as handle:
        vals = pickle.load(handle)
    with open('.cache/vecs.pk', 'rb') as handle:
        vecs = pickle.load(handle)

## eigen values should be of form n^2*np.pi^2/a^2
print("Eigenvalues should have these values: ");
print([n**2 * np.pi**2 / a**2 for n in [1,2,3]])
#print(vals);
print("Calculated eigenvalues:");
print(vals[:3]);

print(" ");
print("plot vectors");
#plot_eigenvectors(vecs[:2]);

print("normalize");
#print(x_list);
vecs = normalize_eigenvectors(vecs[:2], x_list);
vecs = normalize_eigenvectors(vecs[:2], x_list);

plot_eigenvectors(vecs, x_list);
plt.show();
