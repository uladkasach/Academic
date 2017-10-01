

'''
1. define dPsi(x,t)/dk = <equations from notes>

2. define numerical integration procedure for a given (x,t)
    1. retreive N points from dPsi(x,t,k)/dk, for N k values, 1 x value and 1 t value
    2. integrate over a spline interpolation of the points
    3. calculate modulus squared, record
    
3. create a movie of the probability density over time
    - for each t in a range(min, max, step_size):
        for each x in a range(min', max', stepsize'):
            value = integral_at_(x,t)
            mod_squared = (comp_conj(value) * value)
            result[x,t] = mod_squared
    - foreach t in result[x,t]:
        plot all x -vs- result[x,t]
    - combine all plots into gif
    
4. calculate time it takes for a particle to tunnel through barrier
    - since this state is not well defined on its own, lets define "tunelling through barrier" as time where more than 75% of density is past barrier 
    - analyze data created in process of making movie and find where this occures
'''

## imports
from scipy.interpolate import UnivariateSpline;
import matplotlib.pylab as plt;
import numpy as np;

## define constants
V_o = 5;
k_o = 5;
x_o = 40; ## puts particle far away from barrier at time 0
m = 5;
h = 5 #4.1357 * 10**(-15); #eV s
h_bar = h / (2 * np.pi);
a = 1;
b = 2;

#######################################################################
## functionality required to analytically solve for Psi at an (x,t);
#######################################################################
## function generates the integrand requried to calculate Psi
def dPsi_over_dk(x, t, k):
    #k = np.sqrt(2*m*E)/h_bar; --- given, integrated over to create full wave packet
    ##print("--");
    
    alpha = np.sqrt(2*m*V_o) / float(h_bar);
    l_squared = k**2 - alpha**2;
    if(l_squared < 0):
        l = 1j * np.sqrt(-1 * l_squared);
    else:
        l = np.sqrt(l_squared);
    
    if(k == 0 or l == 0): 
        print(" k or l = zero, which is not calculable:");
        print("`-> k: " + str(k))
        print("`-> l: " + str(l))
        return 0; 
    
    lam = (1/float(2*np.pi))*(2*np.pi*h_bar / float(a * m))**(1/float(4)) * np.exp(-k_o**2 * h_bar/float(a*m))
    phi = h_bar / float(4 * a * m) + 1j * h_bar * t / float(2*m);
    theta = k_o * h_bar / (float(2 * a * m)) + 1j * x_o + 1j * x;
    theta_prime = k_o * h_bar / (float(2 * a * m)) + 1j * x_o; ## theta - 1j*x
    
    ## see pg 1.5 and 1.4
    #exponent_part = ((k - l) * 2 * 1j  * b );, note if this is too large it will return nan
    Mf_11 = (0.25) * (1 + l / k) * (1 + k / l) * np.exp(2 * 1j * b * (k - l)) + (0.25) * (1 - l / k) * (1 - k / l) * np.exp(2 * 1j * b * (k + l))
    Mf_21 = (0.25) * (1 - l / k) * (1 + k / l) * np.exp(2 * 1j * b * (k - l)) + (0.25) * (1 + l / k) * (1 - k / l) * np.exp(2 * 1j * b * (k + l))
    Mc_11 = 0.5 * (1 + k / l);
    Mc_12 = 0.5 * (1 - k / l);
    Mc_21 = Mc_12;
    Mc_22 = Mc_11;
    
    
    refl = Mf_21 / (Mf_11);
    tran = Mc_11 + Mc_12 * Mf_21 / (Mf_11);
    refl_prime = Mc_21 + Mc_22 * Mf_21 / (Mf_11);
    tran_prime = 1 / (Mf_11);
    
    ## page 1.8
    mu_1 = lam * np.exp(-k**2 * phi + k*theta); 
    mu_2 = lam * np.exp(-k**2 * phi + k*theta_prime + l*x); 
    mu_3 = mu_1;
    
    if(False):
        print(k);
        print("l = " + str(l))
        print(phi);
        print(theta_prime);
        print(lam);
        print(l);
        print("x = " + str(x));
        print(mu_2);
        print(tran);
        print(refl_prime);

    
    ## page 1.8, equation 1
    if(x < 0):
        if(k < 0):
            value = mu_1 * (1 + refl);
        else: 
            value = mu_1;
            
    ## page 1.8, equation 2
    elif(0 <= x < 2*b): #################################### NOTE - defining this range as 0 <= x < 2b may have unforseen consequences
        if(k < 0):
            value = mu_2 * tran;
        else: 
            value = mu_2 * refl_prime;
            
    ## page 1.8, equation 3
    else: # --> (x > 2*b):
        if(k < 0):
            value = 0;
        else: 
            value = mu_3 * tran_prime;
            
    ## return result
    return value;
            
    
        
## function which calculates modulus squared Psi at a particular x and t
def modulus_squared_Psi_at(x,t, N=False, orders_of_magnitude=False):
    ## for k going from negative infinity to infinity, integrate dPsi_over_dk
    ## that is: integral from -infinity to infinity dPsi/dk * dk = Psi
    ## see page 1.6 and 1.8 for where this is explicitly defined.
    

    ## infinity should be defined relative to the values K is working on
    ## | k = inf | >>> h_bar/(am), h_bar*t, k_o 
    orders_of_magnitude = orders_of_magnitude; ## defines how much greater infinity is related to maximum comparable value. Trade of "infinitness" of infinity w/ number of computations required for granulatiry
    max_of_comparables = np.abs(np.max([h_bar / float(a*m), h_bar * t, k_o, x_o]));
    inf_mag = (max_of_comparables)*10**orders_of_magnitude; ## 6 orders of magnitude greater than max of the list k should be much greater than
    step_size = 2*inf_mag/float(N);
    #print(inf_mag);
    #print(N);
    #print("step size = " + str(step_size));
    #print("max of comparables = " + str(max_of_comparables));
    
    if(step_size > max_of_comparables):
        comparable_N = 2*inf_mag/float(max_of_comparables);
        print("(!) -- warning - stepsize is greater than max val of comparables. N would need to be " + str(comparable_N) + " to be comparable");
        
    k_values = np.arange(-1 * inf_mag, inf_mag + 1, step_size); ## + 1 to max so that max val is generated and not cutoff
    integrand = [dPsi_over_dk(x, t, k) for k in k_values];
    
    #print(k_values[0:25]);
    #print(integrand[0:25]);
    #print(len(k_values))
    
    ## note, since we can not spline complex values - we can only numerically compute the modulus_squared_Psi = integral of Psi* Psi at every dk
    mod_squared_integrand = (np.conj(integrand) * integrand).real; ## note, imag is zero but grab real explicitly to remove concerning errors in future
    
    s = UnivariateSpline(k_values, mod_squared_integrand)
    result = s.integral(0, np.inf);
    print(result);
    return result;
    
## NOTE - you must tune orders_of_magnitude -vs- N to a converging value, when both increase
#######################################################################


def plot_density_now(x_range, densities):
    print(x_range);
    print(densities);
    plt.plot(x_range, densities);
    plt.xlabel('x position')
    plt.ylabel('Psi Modulus Squared')
    plt.axis('tight')
    plt.draw()
    plt.show()

#######################################################################
## create a movie of the probability density over time
#######################################################################
min_t = 5;
max_t = 6;
t_step_size = 1;
min_x = -5;
max_x = 8;
x_step_size = 0.3;

N = 10000;
orders_of_magnitude = 3;

t_range = np.arange(min_t, max_t, t_step_size)
x_range = np.arange(min_x, max_x, x_step_size)

densities_by_time = [];
for t in t_range:
    this_density_by_pos = [];
    for x in x_range:
        print("plotting for (x,t) = (" + str(x) + "," + str(t) + ")")
        this_density_by_pos.append(modulus_squared_Psi_at(x,t, N=N, orders_of_magnitude=orders_of_magnitude));
    plot_density_now(x_range, this_density_by_pos);
        

modulus_squared_Psi_at(0, 0, N=10000, orders_of_magnitude = 3);    
    