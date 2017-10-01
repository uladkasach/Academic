import numpy as np  
import matplotlib.pyplot as plt  

def actual(x):
    y = x;
    while(y > 1):
        y = y - 2;
    return y;
    
def fourier(x, n):
    sum_list = [];
    for this_n in range(n):
        if(this_n == 0): continue;
        period = 2;
        this_value = (2*((-1)**(this_n+1))/(np.pi*this_n))*np.sin(2*np.pi*this_n*x/period)
        sum_list.append(this_value);
    final_value = np.sum(sum_list); 
    return final_value;
    

def calculate_difference_at_n_and_save_plot(n, x):
    #x = [0, 0.01];
    actual_values = [];
    fourier_values = [];
    for this_x in x:
        a_val = actual(this_x);
        f_val = fourier(this_x, n);
        actual_values.append(a_val);
        fourier_values.append(f_val);

    if(n % 25 == 0):
        plt.cla()
        plt.plot(x, actual_values);  
        plt.plot(x, fourier_values);  
        plt.savefig("results/figure_for_"+str(n)+".png");
        #plt.show()
        
    actual_values = np.array(actual_values);
    fourier_values = np.array(fourier_values);
    return np.sum(np.abs(actual_values - fourier_values));


## calculate differences
x = np.arange(0, 10.0, 0.01);
list_n = [];
list_difference = [];
for n in np.arange(5, 255, 5):
    list_n.append(n);
    list_difference.append(calculate_difference_at_n_and_save_plot(n, x));
    
## plot differences
plt.cla()
plt.title("Fourier Series vs Actual Function")
plt.ylabel("Sum of Absolute Difference")
plt.xlabel("n")
plt.plot(list_n, list_difference);  
plt.savefig("results/_differences.png");