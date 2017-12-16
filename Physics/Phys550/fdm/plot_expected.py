
import numpy as np;
import scipy.sparse as sp;
import scipy.sparse.linalg as sparce_linalg;
from scipy import linalg as linalg;
import matplotlib.pyplot as plt;
from scipy.interpolate import UnivariateSpline;
from scipy.integrate import simps;
import pickle;

## for infinite square well, we expect form of [2/a]^(1/2)*sin(n*pi*x/a)
def infinite_square_well_expected(x_list, n):
    print("calculating expected for energylevel " + str(n))
    a = 10;
    eigenvector = [];
    for this_x in x_list:
        psi = (2/float(a))**(1/2) * np.sin(n*np.pi*this_x/float(a))
        eigenvector.append(psi); # already complex conjugate
    return eigenvector;


def plot_eigenvectors(vectors, x_list):
    fig = plt.figure()
    ax = plt.axes()
    for vector in vectors:
        ax.plot(x_list, np.absolute(vector)**2);
    plt.show(block=False)


x_max = 10;
x_min = 0;
n = 1000;
delta_x = (x_max - x_min)/float(n);
a = (x_max - x_min);
x_list = [delta_x*this_n for this_n in range(n)];
print("N : " + str(n));
print("delta_x -> " + str(delta_x));

eigenvectors = [];
for this_n in range(3):
    eigenvector = infinite_square_well_expected(x_list, this_n);
    eigenvectors.append(eigenvector);


plot_eigenvectors(eigenvectors, x_list);
plt.show();
