import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    R = 8.31;
    constant = R*x;
    return b - a / constant;

xdata = np.array([100, 200, 300, 400, 500, 600])
ydata = np.array([-160, -35, -4.2, 9.0, 16.9, 21.3])
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
popt

plt.plot(xdata, func(xdata, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
