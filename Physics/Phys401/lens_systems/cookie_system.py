import numpy as np;
import json;

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


lens_1_pos = [354, 378, 362, 395, 439, 418, 400, 340, 348, 320];
object_distance = 354-209;
L_1 = 38;
L_2 = 38;
f_1 = 48;
f_2 = -22;
f_3 = 48;

for pos in lens_1_pos:
    object_distance = pos - 209;
    results = calculate_image_pos_with_numpy_matmul(object_distance, L_1, L_2, f_1, f_2, f_3);
    print(results);
    print(pos + 38*2 + results[0]);


'''
# 5.5mm delta
delta = 5.5;
lens_1_pos = 700 + delta; #L_1
lens_2_pos = 520 + delta; #L_d
lens_3_pos = 379 + delta ; #_2


object_position = [836, 756]

object_distance = 756 - lens_1_pos;
L_1 = lens_1_pos - lens_2_pos;
L_2 = lens_2_pos - lens_3_pos;
f_1 = 130.33 #mm
f_2 = -22 #mm
f_3 = 129.92 #mm
'''

'''
    midlle of lens not helping
'''


exit();

lens_1_pos = 650; #L_1
lens_2_pos = 594; #L_d
lens_3_pos = 320 ; #_2
L_1 = lens_1_pos - lens_2_pos;
L_2 = lens_2_pos - lens_3_pos;
print("distance of L_1 = " + str(L_1));
print("distance of L_2 = " + str(L_2));
object_positions = [836, 817, 806, 802];
s = np.array(object_positions) - lens_1_pos; #mm



f_1 = 130.33 #mm
f_2 = -18.69 #mm
f_3 = 129.92 #mm

f_1 = 136
f_2 = -22
f_3 = 136


object_distances = np.arange(5, 400, 20);
L_1_positions = np.arange(5, 500, 5);
L_2_positions = np.arange(5, 500, 5);
total_calcs = len(object_distances) * len(L_1_positions) * len(L_2_positions);

L_1_positions = [180];
L_2_positions = [125];

i = -1;
set_index = -1;
valid_combinations = [];
for L_1 in L_1_positions:
    for L_2 in L_2_positions:
        set_index += 1;
        combinations = [];
        image_positions = []
        invalid_count = 0;
        valid_object_distances = [];
        total_length = [];
        for object_distance in (object_distances):
            i+= 1;
            if i%10000 == 0: print("at " + str(i) + " out of " + str(total_calcs) + " : " + str(i/float(total_calcs)));
            s = object_distance;
            s_prime, focal_len = calculate_image_pos_with_numpy_matmul(s, L_1, L_2, f_1, f_2, f_3);
            #print(s_prime);
            if(s_prime < 0): continue;
            this_total_length = s + L_1 + L_2 + s_prime;
            if this_total_length <= 2000: invalid_count += 1;
            #if(this_total_length > 2000): continue;
            total_length.append(this_total_length);
            combinations.append((s, s_prime));
            image_positions.append(s_prime);
            valid_object_distances.append(object_distance);
            #print("initial -vs- final position : " + str(lens_1_pos + s) + "-vs-" + str(lens_3_pos - s_prime) + " -> focal length : " + str(focal_len));

        if (len(image_positions) == 0): continue;

        valid_combinations.append({
            "invalid_count" : invalid_count,
            "mean_total_length" :  np.mean(total_length),
            "L_1" :L_1,
            "L_2" :L_2,
            "range" : np.ptp(image_positions),
            "stdev" : np.std(image_positions),
            "mean" : np.mean(image_positions),
            "object_distances" : str(valid_object_distances),
            "image_positions" : str(image_positions),
        })

valid_combinations = sorted(valid_combinations, key=lambda k: k['range'])  ## sort by range
print(json.dumps(valid_combinations, sort_keys=True, indent=2));

#good_combination = [-1]

#print(o)
