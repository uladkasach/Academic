import numpy as np;
from scipy.special import comb;
import matplotlib.pyplot as plt;

N = 50; # number of coins
n = range(N); # list of numbers 0-N. e.g., [0, 1, 2, ...]


x = n;
y = comb(N, n) / float(2**N)

print x;
print y;
plt.scatter(x, y)
plt.show()
