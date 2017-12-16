## h_n^(1) = j_n + i * y_n
## thus, d(h_n^(1))/dr = d(j_n)/(dr)*(dx/dr) + i * d(y_n)/dr * dx/dr
## where x = kr, h_n' = j_n' * k + i * l * y_n'


## Goal: for an arbitrary l find points where functions are equal (p - v and a dependency)

## plot the solutions as a function of lambda
from __future__ import division
import scipy
import scipy.optimize
import numpy as np
import matplotlib.pylab as plt;
from scipy.optimize import brentq




m = 1 #0.511 * 10**6 ## eV / s - mass of electron
a = 1 #0.529*10**-10; ## one a.u.
alpha = 1 #1*10**-5;
h = 1; #4.1357 * 10**(-15); #eV s
h_bar = h / (2 * np.pi);


def func(k, ratio, bool_full_value = True):
    gamma = alpha * ratio;
    #mu = 2*m*alpha/h_bar**2;
    mu = alpha;
    lam = gamma/alpha;
    #print("---");
    #print("k->" + str(k));
    fun = (4*k**2 - 4*k*mu + mu**2*(1 + lam**2))
    fun2 = np.exp(-4*k*a) * mu**2*(1 + lam**2)

    #print(fun);
    #print(fun2);
    #print("full : " + str(fun - fun2));
    if(bool_full_value == True):
        return fun - fun2;
    else:
        return [fun, fun2];



def find_all_roots(f, a, b, pars=(), min_window=0.001):
    try:
        one_root = brentq(f, a, b, pars)
        print "Root at %g in [%g,%g] interval" % (one_root, a, b)
    except ValueError:
        print "No root in [%g,%g] interval" % (a, b)
        return [] # No root in the interval

    if one_root-min_window>a:
        lesser_roots = find_all_roots(f, a, one_root-min_window, pars)
    else:
        lesser_roots = []

    if one_root+min_window<b:
        greater_roots = find_all_roots(f, one_root+min_window, b, pars)
    else:
        greater_roots = []

    return lesser_roots + [one_root] + greater_roots

########
## find roots
##########
if(True):
    full_roots = [];
    ratio_range = np.arange(0, 1, 0.001);
    for ratio in ratio_range:
        #ratio = 0.25
        min = -1
        max = 1 # set max to some sufficiently large value
        #root = scipy.optimize.brentq(func, min, max, args = (ratio)) # args just supplies any extra
                                                               # argument for the function that isn't the varied parameter
        roots = find_all_roots(func, min, max, pars=(ratio))

        full_roots.append(roots[0]);
        print(roots);
        if(len(roots) > 1):
            print("MORE THAN ONE ROOT FOUND!!!!");
            exit();

    plt.plot(ratio_range, full_roots);
    plt.axis('tight')
    plt.ylabel(" [2mE]^(1/2)/h_bar");
    plt.xlabel(" gamma / alpha ");
    plt.title("Ratio vs Energy of Solutions");
    plt.draw()
    plt.savefig("results_3/ratio_vs_energy.png")


if(False): ## plot function
    k_range = np.arange(0, 1, 0.001);
    left_vals = [];
    right_vals = [];
    for k in k_range:
        val, val2 = (func(k, ratio, bool_full_value = False))
        left_vals.append(val);
        right_vals.append(val2);


    plt.plot(k_range, left_vals);
    plt.plot(k_range, right_vals);
    plt.axis('tight')
    plt.title("gamma/alpha = " + str(ratio));
    plt.draw()
    plt.savefig("results_3/ratio_" + str(ratio)+".png")
