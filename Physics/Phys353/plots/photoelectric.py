import numpy as np
import matplotlib.pyplot as plt


blue = [1137, 1014, 1064, 961, 1047, 949]
green = [381.5, 389,364.4, 344, 407, 394.4]



########################
## Stopping potential vs distances
########################
tung273 = [[470, 490, 430, 690, 510, 630, 470, 630], [710, 630, 550, 450, 430, 450, 470, 450], [570, 510, 550, 490,510, 410, 450, 510]];
distances = [10, 15, 20];
tung273_full = []
[tung273_full.extend(el) for el in tung273] 
print(tung273_full);


tungRed = [[430, 530, 530, 450, 450, 430, 430, 390, 450, 450], [610, 530, 490, 570, 630, 590, 530, 790, 510, 490], [370, 610, 630, 550, 610, 510, 490, 590, 650, 530]];
distances = [5, 10, 7];
tungRed_full = []
[tungRed_full.extend(el) for el in tungRed] 
print(tungRed_full);


Hgblue15=([1.21,1.31,1.39,1.37,1.03,1.07])
Hgblue10=([1.19,1.27,1.11,1.13,1.21,1.23])
Hgblue5=([1.27,1.29,2.26,1.39,1.17,1.23])
Hgblue20=([.970,1.05,.850,.830,.870,.870])
Hgblue7=([1.21,1.13,1.19,1.25,1.27,1.26])
HgBlueDist=[Hgblue5,Hgblue7,Hgblue10,Hgblue15,Hgblue20]

hg_blue_full = [];
[hg_blue_full.extend(el) for el in HgBlueDist] 
#print(hg_blue_full);


def mean_var_and_size(data_list):
    mean = np.mean(data_list);
    var = np.var(data_list)**(1/2);
    size = len(data_list);
    return mean, var, size;

'''
print("\nHgblue5: ", mean_var_and_size(Hgblue5));
print("\nHgblue7: ", mean_var_and_size(Hgblue7));
print("\nHgblue10: ", mean_var_and_size(Hgblue10));
print("\nHgblue15: ", mean_var_and_size(Hgblue15));
print("\nHgblue20: ", mean_var_and_size(Hgblue20));
'''
'''
print("\ntung273 10: ", mean_var_and_size(tung273[0]));
print("\ntung273 15 : ", mean_var_and_size(tung273[1]));
print("\ntung273 20 : ", mean_var_and_size(tung273[2]));
'''
print("\ntung273: ", mean_var_and_size(tung273_full));

'''
print("\ntungRed 5: ", mean_var_and_size(tungRed[0]));
print("\ntungRed 7 : ", mean_var_and_size(tungRed[1]));
print("\ntungRed 10 : ", mean_var_and_size(tungRed[2]));
print("\ntungRed: ", mean_var_and_size(tungRed_full));
'''


print("\nhg_blue: ", mean_var_and_size(hg_blue_full));
