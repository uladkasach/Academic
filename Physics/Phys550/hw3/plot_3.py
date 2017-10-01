## plot the solutions as a function of lambda
from __future__ import division
import scipy
import scipy.optimize
import numpy as np
import matplotlib.pylab as plt;



m = 1 #0.511 * 10**6 ## eV / s - mass of electron
a = 1 #0.529*10**-10; ## one a.u.
alpha = 1 #1*10**-5;
h = 1; #4.1357 * 10**(-15); #eV s
h_bar = h / (2 * np.pi);


def func(k, ratio):
    gamma = alpha * ratio;
    print(gamma);
    mu = 2*m*alpha/h_bar**2;
    mu = alpha;
    lam = gamma/alpha;
    print("---");
    fun = (4*k**2 - 4*k*mu + mu**2*(1 + lam**2))
    fun2 = np.exp(4*k*a)
    fun3 = 0 - mu**2*(1 + lam**2);
    
    print("---");
    print(fun);
    print(fun2);
    return(fun);



########
## roots not working
##########
ratio = 5000000
min = 1
max = 10 # set max to some sufficiently large value
#root = scipy.optimize.brentq(func, min, max, args = (ratio)) # args just supplies any extra
                                                       # argument for the function that isn't the varied parameter

k_range = np.arange(0, 1, 0.001);
left_vals = [];
right_vals = [];
for k in k_range:    
    val = (func(k, ratio))
    print(val);
    print(ratio);
    left_vals.append(val);


plt.plot(k_range, left_vals);
plt.axis('tight')
plt.draw()
plt.show()