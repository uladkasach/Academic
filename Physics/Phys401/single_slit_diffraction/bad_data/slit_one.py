import numpy as np;
import matplotlib.pyplot as plt;


measurements_scale_1 = [
    (68.5, 9),
    (65.5, 9),
    (65,   8),
    (64.5, 6),
    (64,   4.5),
    (63.5, 3.4),
    (63,   1.75),
    (62.5, 0.8),
    (62,   0.25),
    (61.5, 0.4),
    (61,   0.0),
    (60,   0.3),
    (59,   0.4),
    (69.5, 8.5),
    (70,   7.5),
    (70.5, 5.6),
    (71,   3.6),
    (71.5, 2),
    (72,   1.1),
    (72.5, 0.5),
    (73,   0.2),
    (73.5, 0.0),
    (74,   0.0),
    (74.5, 0.0),
    (75,   0.2),
    (76.5, 0.4),
]
relation = (76.5, 0.4, 6.9) ## position 76.5, ratio scale1:scale2 -> 0.4:6.9
measurements_scale_2 = [
    (76.5, 6.9),
    (77, 6.6),
    (77.5, 5.1),
    (78,   4.5),
    (78.5, 3.6),
    (79, 3.5),
    (79.5, 2.6),
    (80, 2.25),
    (80.5, 2.1),
    (81, 2.4),
    (81.5, 3),
    (82, 3.1),
    (82.5, 3.4),
    (88.5, 2.4),
    (88, 2.4),
    (87.5, 2.24),
    (87, 2),
    (86.5, 2),
    (86, 2),
    (85.5, 2.4),
    (85, 2.6),
    (84.5, 3),
    (84, 3.5),
    (83.5, 3.5),
    (83, 3.5),
    (59, 7.5),
    (58.5, 6.5),
    (58, 5.1),
    (57.5, 5.0),
    (57, 4.4),
    (56.5, 3.0),
    (56, 2.5),
    (55.5, 2.4),
    (55.0, 2.4),
    (54.5, 3.3),
    (54, 3.6),
    (53.5, 3.7),
    (53, 3.8),
    (52.5, 3.8),
    (52.0, 3.6),
    (51.5, 3.3),
    (51, 2.4),
    (50.5, 2.4),
    (50, 2.5),
    (49.5, 2.6),
    (49, 2.6),
    (48.5, 2.9),
    (48.0, 2.9), 
]

def normalize_intensities(list_one, list_two, relation):
    ## I1/I2 = relation[1]/relation[2] -> I2 = I1 * r_2/r_1
    one_to_two_ratio = relation[2]/float(relation[1]);

    master_list = [];
    for tupe in list_one:
        new_tupe = (tupe[0], tupe[1] * one_to_two_ratio);
        master_list.append(tupe);

    master_list.extend(list_two);
    return master_list;

tuples = normalize_intensities(measurements_scale_1, measurements_scale_2, relation);

tuples = np.array(tuples);
print(tuples);

print(tuples.shape);
print(len(tuples[:, 1]))

x = tuples[:, 0];
y = tuples[:, 1];




fig, ax = plt.subplots()
ax.scatter(x, y)

plt.show()
