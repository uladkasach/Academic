import numpy as np;
import matplotlib.pyplot as plt;

## plot hyperbolic tangent between -4 and 4

x = np.arange(-4, 4, 0.1);
y = np.tanh(x);

plt.scatter(x, y)
plt.show()
