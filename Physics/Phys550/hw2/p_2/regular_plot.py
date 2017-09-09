import numpy as np  
import matplotlib.pyplot as plt  

def regular_f(t):
    if(t < 2):
        return 0;
    elif(2 < t and t < 7):
        value = (4/float(5))*((t**2)/float(2) - t);
        return value;
    elif(3 < t and t < 6):
        return (4/float(5))*(t-3/float(2));
    elif(6 < t and t < 7):
        return (4/float(5))*(-(t**2)/float(2) + 2*t + 21/float(2));
    else:
        return 0;

x = np.arange(0.0, 10.0, 0.01);
regular_values = [];
transformed_values = [];
for this_x in x:
    regular_result = regular_f(this_x);
    #print(regular_result);
    regular_values.append(regular_result);
    #fourier_values.append(fourier(this_x, n, period));

    
plt.plot(x, regular_values);  
#plt.plot(x, fourier_values);  
plt.show()