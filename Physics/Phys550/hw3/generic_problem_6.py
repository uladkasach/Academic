## imports
import matplotlib.pylab as plt;
import numpy as np;

## define constants
V_o = 5; #Volts
m = 0.511 * 10**(6); ## mass of electron
h = 4.1357 * 10**(-15); #eV s
h_bar = h / (2 * np.pi);
b = 2*10**(-10); #meters

def return_coefficients_for_barrier(E, V_o):
    k = np.sqrt(2*m*E)/float(h_bar);
    alpha = np.sqrt(2*m*V_o)/float(h_bar);
    
    l_squared = k**2 - alpha**2;
    if(l_squared < 0):
        l = 1j * np.sqrt(-1 * l_squared);
    else:
        l = np.sqrt(l_squared);
    
    if(k == 0 or l == 0): 
        print(" k or l = zero, which is not calculable:");
        print("`-> k: " + str(k))
        print("`-> l: " + str(l))
    
    ## see pg 1.5 and 1.4
    #exponent_part = ((k - l) * 2 * 1j  * b );, note if this is too large it will return nan
    Mf_11 = (0.25) * (1 + l / k) * (1 + k / l) * np.exp(2 * 1j * b * (k - l)) + (0.25) * (1 - l / k) * (1 - k / l) * np.exp(2 * 1j * b * (k + l))
    Mf_21 = (0.25) * (1 - l / k) * (1 + k / l) * np.exp(2 * 1j * b * (k - l)) + (0.25) * (1 + l / k) * (1 - k / l) * np.exp(2 * 1j * b * (k + l))
    Mc_11 = 0.5 * (1 + k / l);
    Mc_12 = 0.5 * (1 - k / l);
    
    
    refl = Mf_21 / (Mf_11);
    tran = 1 / (Mf_11);
    
    return [refl, tran, np.conj(refl) * refl, np.conj(tran) * tran];


Rs = [];
Ts = [];
energies = np.arange(5, 10, 0.01);
for an_energy in energies:
    result = return_coefficients_for_barrier(an_energy, V_o);
    Ts.append(result[3]);
    Rs.append(result[2]);
    print("E = " + str(an_energy) + " => T = " +str(result[3]) + " and R = " + str(result[2]) + " and total = " + str(result[3] + result[2]));



plt.plot(energies, Rs);
plt.plot(energies, Ts);
plt.axis('tight')
plt.ylabel(" Probability ");
plt.xlabel(" Energy (Volts) ");
plt.title(" Probability vs Energy for Transmission and Reflection at " + str(V_o) + "V Barrier");
plt.draw()
plt.savefig("results_6/"+str(V_o)+"V_barrier_smallstep.png")