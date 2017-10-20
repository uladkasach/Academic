import numpy as np
from scipy.integrate import quad
'''
    Function : 2*pi**(-1/2) * integral from 0 to 1 of exp{-x**2}dx
'''


def integrand(x):
    return 2*np.pi**(-0.5) * np.exp(-x**2)

I = quad(integrand, 0, 1)
print(I);

print(1 - I[0]);
