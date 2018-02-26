import numpy as np;
from scipy.special import comb;
import matplotlib.pyplot as plt;
import matplotlib.mlab as mlab;
import math;

N = 50; # number of oscilators per solid
q = 1000; # number of energy per solid
q_a_options = range(2*q); ## list of numbers from 0 to 2q; e.g., [0, 1, 2, ...]

def multiplicity(this_N, this_q):
    return comb(this_q + this_N - 1, this_N - 1);
def probability_of_macrostate(N_total, q_total, N_a, q_a, N_b, q_b):
    mul_qa = multiplicity(N_a, q_a);
    mul_qb = multiplicity(N_b, q_b);
    mul_total = multiplicity(N_total, q_total);
    return mul_qa * mul_qb / float(mul_total);
def probability_of_qa(N, q, q_a):
    return multiplicity(N, q_a)*multiplicity(N, 2*q-q_a) / float(multiplicity(2*N, 2*q));

#############
## plot probability
#############
x = [];
y = [];
for q_a in q_a_options:
    x.append(q_a);
    #this_probability = probability_of_macrostate(2*N, 2*q, N, q_a, N, 2*q-q_a);
    this_probability = probability_of_qa(N, q, q_a);
    y.append(this_probability);
plt.plot(x, y) # plot the scatter matrix


#############
## plot gaussian
#############
mu = q
sigma = q/float(math.sqrt(2*N));
x = np.array(q_a_options);
y = mlab.normpdf(x, mu, sigma);
plt.plot(x, y) ## plot the gaussian


plt.show()## who plots
