import numpy as np;
import matplotlib.pyplot as plt


object_position         = 880;
lens_positions          = [550, 650, 692, 517, 439, 353, 307, 279, 262, 485]
image_positions         = [
                            [333, 345, 231, 315, 254, 180, 140, 113, 96, 289],
                            [338, 331, 202, 315, 253, 181, 141, 119, 98, 295],
                            [332, 326, 215, 314, 256, 180, 138, 116, 100, 285],
                          ];

focal_len = 128.8; # mm
newtonian_differences = [];
for index in range(len(lens_positions)):
    lens_pos = lens_positions[index];
    s = object_position - lens_pos;
    s_prime = np.array([lens_pos - image_positions[0][index], lens_pos - image_positions[1][index], lens_pos - image_positions[2][index]]);
    #print("s:",  s, " s':", s_prime[0], " s':", s_prime[1], " s':", s_prime[2]);
    x = s - focal_len;
    x_prime = s_prime - focal_len;
    #print(s, "& ", s_prime[0], "& ", s_prime[1], "& ", s_prime[2], "\\\\");

    for this_prime in x_prime:
        lhs = x*this_prime;
        rhs = focal_len**2;
        difference = lhs-rhs;
        print(lhs, "=", rhs);
        print("`-> ", (lhs - rhs));
        newtonian_differences.append(np.sqrt(np.abs(difference)));


n = len(newtonian_differences);
avg = np.mean(newtonian_differences);
stdev = np.std(newtonian_differences);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));
