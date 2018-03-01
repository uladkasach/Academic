import numpy as np;
import matplotlib.pyplot as plt;

def multiplicity(z, N):
    return (4*z*(1-z))**N;

for N in [1, 10, 100, 1000, 10000]:
    z_list = np.arange(0, 1, 0.05);
    x = z_list;
    y = multiplicity(z_list, N);
    plt.plot(x, y) # plot the curve
    
plt.show()## show plot
