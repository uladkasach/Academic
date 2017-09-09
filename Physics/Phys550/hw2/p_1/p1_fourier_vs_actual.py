import numpy as np  
import matplotlib.pyplot as plt  

def actual(x):
    y = x;
    while(y > 1):
        y = y - 2;
    #print(str(x) + " -> " + str(y) );
    return y;
    
def fourier(x, n, period):
    
    x = x - 1;
    
    sum_list = [];
    for this_n in range(n):
        if(this_n == 0): continue;
        this_value = (-2/(np.pi*this_n))*np.sin(2*np.pi*this_n*x/period)
        sum_list.append(this_value);
    final_value = np.sum(sum_list); 
    return final_value;
    
    
n = 20;    
period = 2;
x = np.arange(-1.0, 10.0, 0.01);
actual_values = [];
fourier_values = [];
for this_x in x:
    actual_values.append(actual(this_x));
    fourier_values.append(fourier(this_x, n, period));

    

plt.plot(x, actual_values);  
plt.plot(x, fourier_values);  
plt.show()
    