import numpy as np;
import matplotlib.pyplot as plt;

tuples = [
    (54, 9),
    (54.5, 9),
    (55, 9),
    (55.5, 9),
    (56, 9),
    (56.5, 9),
    (57, 9),
    (57.5, 9),
    (58, 9),
    (58.5, 9),
    (59, 8.8),
    (59.5, 5.3),
    (60, 8.5),
    (60.5, 8.7),
    (61, 8.7),
    (61.5, 7.8),
    (62, 4.6),
    (62.5, 2.7),
    (63, 1.3),
    (63.5, 1),
    (64, 1.9),
    (64.5, 3),
    (65, 3.7),
    (65.5, 3.9),
    (66, 3.5),
    (66.5, 3),
    (67, 2.1),
    (67.5, 0.7),
    (68, 0.5),
    (68.5, 0.4),
    (69, 0.9),
    (69.5, 1.3),
    (70, 1.5),
    (70.5, 1.3),
    (71, 0.8),
    (71.5, 0.4),
    (53.5, 9),
    (52.5, 9),
    (51.5, 8.9),
    (51, 7.9),
    (50.5, 4.3),
    (50, 6.1),
    (49.5, 6.7),
    (49, 8.7),
    (48.5, 8.7),
    (48, 8.4),
    (47.5, 5.8),
    (47, 4.2),
    (46.5, 4.2),
    (46, 1),
    (45.5, 0.8),
    (45, 1.5),
    (44.5, 2.4),
    (44, 2.6),
    (43.5, 2.6),
    (43, 2),
    (42.5, 1),
    (42, 0.6),
    (41.5, 0.4),
    (40.5, 0.6),
    (40, 1),
    (39.5, 1),
    (39, 0.8),
]

tuples = np.array(tuples);
print(tuples);

print(tuples.shape);
print(len(tuples[:, 1]))

x = tuples[:, 0];
y = tuples[:, 1];


fig, ax = plt.subplots()
ax.scatter(x, y)

plt.show()