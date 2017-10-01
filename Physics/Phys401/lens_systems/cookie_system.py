import numpy as np;

'''
    M = R_3 * T_2 * R_2 * T_1 * R_1
'''


def calculate_image_pos(s, L_1, L_2, f_1, f_2, f_3):
    return False;
    s = float(s);
    L_1 = float(L_1);
    L_2 = float(L_2);
    f_1 = float(f_1);
    f_2 = float(f_2);
    f_3 = float(f_3);
    
    
    
    part_1 = (1 - L_1/f_1);
    part_2 = (-1)*part_1*(1/f_2) - 1/f_1;  
    
    res = np.array([[part_1, L_1], [-1/f_1, 1]])
    print("--");
    print(res);
    return;
    

    M1 =  part_1 + L_2 * part_2;
    M2 = L_1 + L_2 * part_1;
    M3 = (-1/f_3)*(part_1 + L_2*part_2) + part_2;
    M4 = (-1/f_3)*(L_1 + L_2*part_1 + part_1);

    print(1/M3);
    
    s_prime = (s*M1 + M2) / (s*M3 + M4);
    
    return s_prime;
    
    
def calculate_image_pos_with_numpy_matmul(s, L_1, L_2, f_1, f_2, f_3):
    s = float(s);
    L_1 = float(L_1);
    L_2 = float(L_2);
    f_1 = float(f_1);
    f_2 = float(f_2);
    f_3 = float(f_3);
    
    R_1 = [[1, 0], [-1/f_1, 1]]
    T_1 = [[1, L_1], [0, 1]]
    R_2 = [[1, 0], [-1/f_2, 1]]
    T_2 = [[1, L_2], [0, 1]]
    R_3 = [[1, 0], [-1/f_3, 1]]
    
    M = np.matmul(T_1, R_1);
    M = np.matmul(R_2, M);
    M = np.matmul(T_2, M);
    M = np.matmul(R_3, M);
    # print(M);
    
    
    focal_len = -1/M[1,0];
    #print("focal  : " + str(focal_len));

    s_prime = (-1)*(s*M[0,0] + M[0,1])/(s*M[1,0] + M[1,1]);
    #print("s prime : " + str(s_prime));
    return [s_prime, focal_len];
    
    
lens_1_pos = 650;
lens_2_pos = 594;
lens_3_pos = 320 ;
L_1 = lens_1_pos - lens_2_pos;
L_2 = lens_2_pos - lens_3_pos;
print("distance of L_1 = " + str(L_1));
print("distance of L_2 = " + str(L_2));

f_1 = 18 #mm
f_2 = -22 #mm
f_3 = 136 #mm

object_position = 696; 


for object_position in np.arange(690, 860, 5):
    s = object_position - lens_1_pos; #mm
    s_prime, focal_len = calculate_image_pos_with_numpy_matmul(s, L_1, L_2, f_1, f_2, f_3);
    #print("focal_len = " + str(focal_len));
    #print("distance of s = " + str(s));
    #print("initiial position : " + )
    #print("distance of s' = " + str(s_prime));
    print("initial -vs- final position : " + str(lens_1_pos + s) + "-vs-" + str(lens_3_pos - s_prime));

