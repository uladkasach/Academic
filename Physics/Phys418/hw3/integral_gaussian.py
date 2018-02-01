import numpy as np;
from scipy.integrate import quad

def integrand(x, sigma, mu):
    sigma = 0.8;
    mu = -2.0;
    scale = 1 / float(sigma * np.sqrt(2 * np.pi))
    raised_to = -0.5 * ((x - mu) / float(sigma))**2;
    return scale * np.exp(raised_to);

sigma = 0.8;
mu = -2.0;

I = quad(integrand, -0.5, 0.5, args=(sigma, mu))

print I;
