####################################
## Task : Create dataset of logical functions for 3 variables, x1, x2, x3, and label y, all values are binary values
######  `and`:  y = x1 * x2
## Purpose : demonstrate how tensorflow can be used to teach a logical regression algorithm this function
#####################################

################
import pandas as pd
import numpy as np 
import sys
################

logicalFunction = 'XOR';


df = pd.DataFrame(columns =  ["x1", "x2", "x3", "y"]);

for i in range(10000):
    x1 = np.random.randint(0, 2);
    x2 = np.random.randint(0, 2);
    x3 = np.random.randint(0, 2);
    
    if(logicalFunction == 'AND'):
        y = x1 and x2;
    elif(logicalFunction == 'XOR'):
        y = (x1 or x2) and (x1 != x2);    
    
    y = int(y);
    df.loc[i] = [x1, x2, x3, y];
print(df);


print('Type `save` to save data as csv.') 
result = sys.stdin.readline().rstrip();
if (result == 'save'):
    print ('Please type filename, data will be saved as {}.csv');
    filename = sys.stdin.readline().rstrip();
    file_name = filename + '.csv';
    df.to_csv(file_name, index=False);
    print('done!');
    print('\n');
else:
    print('Ok. Data not saved.');
