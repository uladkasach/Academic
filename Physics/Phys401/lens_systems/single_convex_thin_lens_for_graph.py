import numpy as np;
#import matplotlib.pyplot as plt


object_position         = 880;
lens_positions          = [550, 650, 692, 517, 439, 353, 307, 279, 262, 485]
image_positions         = [
                            [333, 345, 231, 315, 254, 180, 140, 113, 96, 289],
                            [338, 331, 202, 315, 253, 181, 141, 119, 98, 295],
                            [332, 326, 215, 314, 256, 180, 138, 116, 100, 285],
                          ];

delta_s = 0.5; #0.5 mm; - precision of distance measurement

object_distances = [];
image_distances = [];
focal_lengths = [];
focal_errors = [];
for index in range(len(lens_positions)):
    lens_pos = lens_positions[index];
    s = object_position - lens_pos;
    s_prime = [lens_pos - image_positions[0][index], lens_pos - image_positions[1][index], lens_pos - image_positions[2][index]];
    #print("s:",  s, " s':", s_prime[0], " s':", s_prime[1], " s':", s_prime[2]);

    #print(s, "& ", s_prime[0], "& ", s_prime[1], "& ", s_prime[2], "\\\\");


    object_distances.extend([s,s,s]);
    image_distances.extend(s_prime);

    object_distance = s;
    for image_distance in s_prime:
        f_converging = 1/float(1/float(object_distance) + 1/float(image_distance));
        focal_error = delta_s/float(s) + delta_s/float(image_distance) - (2*delta_s/float(s + image_distance));
        focal_lengths.append(f_converging);
        focal_errors.append(f_converging*focal_error);


print("---------------");

n = len(focal_errors);
avg = np.mean(focal_errors);
stdev = np.std(focal_errors);

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
