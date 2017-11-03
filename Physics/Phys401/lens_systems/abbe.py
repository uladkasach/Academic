import numpy as np;


object_position         = 880;
lens_positions          = [655.5, 632, 593, 568, 546, 484, 427, 420]
image_positions         = [
                            [184, 266.5, 311, 314.5, 310.5, 278, 237.5, 230.5],
                            [180, 267, 320, 319, 308, 281, 238, 234],
                            [188, 269, 314, 312, 305, 278, 235, 231],
                          ];



def find_focal_len(s_1, s_prime_1, s_2, s_prime_2):
    m_1 = -1 * s_prime_1/s_1;
    m_2 = -1 * s_prime_2/s_2;
    f = (s_2 - s_1)/(1/m_1 - 1/m_2);
    return f;


data_pairs = [];
focal_errors = [];
for index in range(len(lens_positions)):
    lens_pos = lens_positions[index];
    s = object_position - lens_pos;
    s_prime = [lens_pos - image_positions[0][index], lens_pos - image_positions[1][index], lens_pos - image_positions[2][index]];
    #print("s:",  s, " s':", s_prime[0], " s':", s_prime[1], " s':", s_prime[2]);

    print(s, "& ", s_prime[0], "& ", s_prime[1], "& ", s_prime[2], "\\\\");

    for this_s_prime in s_prime:
        data_pairs.append((s, this_s_prime));

delta_s = 0.5; ## .5mm imprecision
focal_lengths = [];
for index_one, pair_one in enumerate(data_pairs):
    for index_two, pair_two in enumerate(data_pairs):
        if(index_two <= index_one): continue; ## eliminates repeats
        if(pair_one == pair_two): continue; ## enforces distinct pairs -- only one duplicate measure existed
        if(pair_one[0] == pair_two[0]): continue;
        f = find_focal_len(pair_one[0], pair_one[1], pair_two[0], pair_two[1]);
        if(f == False): continue;
        focal_lengths.append(f);

        s_1 = pair_one[0];
        s_1_prime = pair_one[1];
        s_2 = pair_two[0];
        s_2_prime = pair_two[1];
        focal_error = f*(delta_s/float(s_1) + delta_s/float(s_2) - delta_s*(s_1 + s_2_prime - s_2 - s_1_prime)/float(s_1*s_2_prime - s_2 * s_1_prime));
        focal_errors.append(focal_error);




print("---------------");

n = len(focal_errors);
avg = np.mean(focal_errors);
stdev = np.std(focal_errors);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));

print("---------------");


print("n    : ", len(focal_lengths))
print("mean : ", np.mean(focal_lengths));
print("stdev: ", np.std(focal_lengths));
