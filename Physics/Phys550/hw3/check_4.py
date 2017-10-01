import numpy as np;

calculate_energy_coefficient = True;

total = 0.0;
scale = 2**(0.5) / np.pi;
for n in range(100000):
    if(n == 6):
        value = np.pi/float(2);
    elif (n % 2 == 0): 
        value = 0; # if even, add 0
    else:
        value = np.sin(np.pi/2 * (n-6))/float((n-6)) - np.sin(np.pi/2 * (n+6))/float((n+6));
    value = scale * value;
    value = value**2;
    
    if(calculate_energy_coefficient == True):
        ## E^2_n = E^1_1 * n^2/4 -> coefficient = n^2/4
        value = value * n**2/float(4);
    
    total += value;
    
print(total);