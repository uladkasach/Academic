import numpy as np  
import matplotlib.pyplot as plt  

def amplitude_of_transform(w):
    if(w == 0): return 0;
    return (16/float((w**2))) * (np.cos(w*6) - np.cos(w*7)) * (np.sin(w*7) - np.sin(w*6));

x = np.arange(0.0, 10.0, 0.01);
regular_values = [];
transformed_values = [];
for this_x in x:
    regular_result = amplitude_of_transform(this_x);
    #print(regular_result);
    regular_values.append(regular_result);
    #fourier_values.append(fourier(this_x, n, period));

    
plt.plot(x, regular_values);  
#plt.plot(x, fourier_values);  
plt.show()