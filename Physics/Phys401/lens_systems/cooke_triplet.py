import numpy as np;
#import matplotlib.pyplot as plt

object_position         = 209;
lens_positions          = [354, 378, 362, 395, 439, 418, 400, 340, 348, 320]
image_positions         = [
                            [515, 527, 525, 535, 563, 547, 533, 518, 519, 523],
                            [521, 531, 525, 537, 564, 547, 539, 517, 520, 522],
                          ];


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

focal_diffs = [];
position_diffs = [];

focal_lengths = [];
object_distances = [];
image_distances = [];
focal_lengths = [];
for index in range(len(lens_positions)):
    lens_pos = lens_positions[index];
    lens_pos = [lens_pos, lens_pos + 38*2]; # 38
    this_obj_pos = object_position;
    s = this_obj_pos - lens_pos[0];
    s_prime = np.array([lens_pos[1] - image_positions[0][index], lens_pos[1] - image_positions[1][index]]);
    #print("s:",  s, " s':", s_prime[0], " s':", s_prime[1], " s':", s_prime[2]);

    s = s * -1;
    s_prime = s_prime * -1;

    print(s, "& ", s_prime[0], "& ", s_prime[1], "\\\\");

    object_distance = s;
    for image_distance in s_prime:
        part_focal = float(1/float(object_distance) + 1/float(image_distance));
        if part_focal == 0: continue;
        f_converging = 1/part_focal;
        focal_lengths.append(f_converging);

        expected_values = calculate_image_pos_with_numpy_matmul(s, 38, 38, 44, -22, 44)
        difference = (np.abs(expected_values[0] - image_distance), np.abs(expected_values[1] - f_converging));
        focal_diffs.append(difference[1]);
        position_diffs.append(difference[0]);

    object_distances.extend([s,s]);
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
