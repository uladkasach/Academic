
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(B_0, t):
    gamma = 1;
    omega = 1;
    mu = B_0 * gamma * 0.5 / omega;
    probability = np.cos(mu * np.sin(omega * t))**2;
    return probability;

t = np.linspace(0, 6.28, 100) # since omega is one, this is essentially the radians of sin. we want this to go full range, so from t = 0 to t = 2pi
B_0 = np.linspace(-6, 6, 100) # since np.cos is even (and especially np.cos**2) we dont need negative range, unless we want to verify

X, Y = np.meshgrid(t, B_0)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('t')
ax.set_ylabel('B_0')
ax.set_zlabel('Probability');

plt.show();
