import numpy as np;
#import matplotlib.pyplot as plt

lens = 2;
if(lens==1):
    object_position         = [815, 790, 760, 740, 720, 700, 670, 620];
    lens_positions          = (500, 440)
    image_positions         = [
                                [371, 367, 364, 359, 353, 345, 330, 282],
                                [369, 365, 362, 361, 353, 347, 332, 283],
                                [370, 364, 362, 359, 352, 343, 335, 280],
                              ];
elif(lens == 2):
    object_position         = [621, 636, 646, 656, 665, 676, 616, 606];
    lens_positions          = (500, 350)
    image_positions         = [
                                [204, 221, 229, 238, 247, 253, 119, 182],
                                [202, 222, 228, 240, 243, 254, 198, 183],
                                [205, 219, 233, 241, 246, 251, 126, 179]
                              ];
elif(lens == 3):
    object_position         = [621, 636, 646, 656, 665, 676, 616, 606];
    lens_positions          = (500, 400)
    image_positions         = [
                                [246, 256, 259, 264, 266, 269, 245, 237],
                                [249, 261, 257, 264, 266, 269, 243, 230],
                                [252, 257, 257, 265, 265, 270, 245, 240]
                              ];

def calculate_image_pos_with_numpy_matmul(s, L_1, f_1, f_2):
    s = float(s);
    L_1 = float(L_1);
    f_1 = float(f_1);
    f_2 = float(f_2);

    R_1 = [[1, 0], [-1/f_1, 1]]
    T_1 = [[1, L_1], [0, 1]]
    R_2 = [[1, 0], [-1/f_2, 1]]

    M = np.matmul(T_1, R_1);
    M = np.matmul(R_2, M);
    # print(M);

    focal_len = -1/M[1,0];
    #print("focal  : " + str(focal_len));

    s_prime = (-1)*(s*M[0,0] + M[0,1])/(s*M[1,0] + M[1,1]);
    #print("s prime : " + str(s_prime));
    return [s_prime, focal_len];

focal_lengths = [];
object_distances = [];
image_distances = [];
focal_lengths = [];

focal_diffs = [];
position_diffs = [];

for index in range(len(object_position)):
    lens_pos = lens_positions;
    this_obj_pos = object_position[index];
    s = this_obj_pos - lens_pos[0];
    s_prime = [lens_pos[1] - image_positions[0][index], lens_pos[1] - image_positions[1][index], lens_pos[1] - image_positions[2][index]];
    #print("s:",  s, " s':", s_prime[0], " s':", s_prime[1], " s':", s_prime[2]);

    #print(s, "& ", s_prime[0], "& ", s_prime[1], "& ", s_prime[2], "\\\\");

    object_distance = s;
    for image_distance in s_prime:
        part_focal = float(1/float(object_distance) + 1/float(image_distance));
        if part_focal == 0: continue;
        f_converging = 1/part_focal;
        focal_lengths.append(f_converging);

        expected_values = calculate_image_pos_with_numpy_matmul(s, lens_pos[0]-lens_pos[1], 136, 136)
        difference = (np.abs(expected_values[0] - image_distance), np.abs(expected_values[1] - f_converging));
        focal_diffs.append(difference[1]);
        position_diffs.append(difference[0]);

    object_distances.extend([s,s,s]);
    image_distances.extend(s_prime);



print("---------------");

n = len(position_diffs);
avg = np.mean(position_diffs);
stdev = np.std(position_diffs);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));

print("---------------");


print("---------------");

n = len(focal_diffs);
avg = np.mean(focal_diffs);
stdev = np.std(focal_diffs);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));

print("---------------");

n = len(lens_positions);
avg = np.mean(focal_lengths);
stdev = np.std(focal_lengths);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));



x = np.array([1/float(object_distance) for object_distance in object_distances]) ;
y = np.array([1/float(image_distance) for image_distance in image_distances] );


print(x);
print(y);


# fit with np.polyfit
m, b = np.polyfit(x, y, 1)
print(m);
print(b);
print(1/b);


print(m*x + b)
plt.plot(x, y, '.')

print([0].extend(x));
x = np.insert(x, 0, 0);

print(x);
plt.plot(x, m*x + b, '-')
plt.show();
