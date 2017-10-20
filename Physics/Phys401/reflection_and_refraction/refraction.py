#############################
## We measure seperation distance and know thickness. We know that s = tsin(theta_1 - theta_2)/cos(theta_2) -> theta_2 = arctan([sin(theta_1) - s/t]/cos(theta_1))
## We can determine the index of refraction by snells law: n_2 = sin(theta_1)/sin(theta_2);
## We'd like to, first, evaluate errors of the measurements we had. We'll use log-errors in addition to average and stdev:
#############################
import numpy as np;


def calculate_n_2(s, t, n_1, theta_1):
    theta_2 = np.arctan((np.sin(theta_1) - s/t)/np.cos(theta_1));
    print(theta_2 * 180 / np.pi);
    n_2 = n_1*np.sin(theta_1)/np.sin(theta_2);
    return n_2;



def calculate_imprecision(s, t, theta1, n2):

    delta_theta1 = delta_theta1_in_radians;
    s = float(s);
    t = float(t);
    n2 = float(n2);
    print("s : " + str(s) + ", t : " + str(t) + ", theta1 : " + str(theta1 * 180 / np.pi) + ", n2 : " + str(n2))

    delta_s_over_t = delta_s / t - s / t**2 * delta_t;
    print("d(s/t) : " + str(delta_s_over_t));

    part1 = np.cos(theta1) / np.sin(theta1) * delta_theta1;
    print(np.cos(theta1));
    print(np.sin(theta1));
    print("p1: " + str(part1));

    print("(s/t)**2 : " + str((s/t)**2))
    part2_divisor = ((s/t)**2 - 2 * s / t * np.sin(theta1));
    print("part2_divisor :"  + str(part2_divisor));
    part2 = (delta_s_over_t * (1 - np.sin(theta1)) - s/t*np.cos(theta1) * delta_theta1) / part2_divisor;
    print("p2: " + str(part2));

    part3 = (np.cos(theta1) * delta_theta1 - delta_s_over_t) / (np.sin(theta1) - s/t)
    print("p3: " + str(part3));

    delta_n2 = n2 * (part1 + part2 + part3);



    print("delta_n2 " + str(delta_n2));
    return delta_n2;


measured_pairs = [
    [
        ##[0, 2],
        [10, 1.7],
        [20, 1.35],
        [30, 0.9],
        [35, 0.5],
        [30, 0.9],
        [25, 1.05],
        [20, 1.25],
        [15, 1.55],
        [10, 1.65],
        [5, 1.85],
        ##[0, 1],
        [10, 1.85],
        [20, 1.35],
        [30, 0.9],
        [35, 0.7],
        [25, 1.1],
        [15, 1.55]
    ],
    [
        [5, 0.05],
        [5, 0.05],
        [5, 0.05],
        [5, 0.05],
        [10, 0.1],
        [10, 0.1],
        [10, 0.1],
        [10, 0.1],
        [15, 0.15],
        [15, 0.15],
        [15, 0.15],
        [15, 0.15],
        [20, 0.2],
        [20, 0.2],
        [20, 0.2],
        [20, 0.25],
        [25, 0.3],
        [25, 0.3],
        [25, 0.3],
        [25, 0.3],
        [30, 0.35],
        [30, 0.35],
        [30, 0.35],
        [30, 0.35],
        [35, 0.45],
        [35, 0.45],
        [35, 0.45],
        [35, 0.45],
    ]

]

'''

       5  & 0.5 & 0.5 & 0.5 & 0.5 \\
       10 & 1.0 & 1.0 & 1.0 & 1.0  \\
       15 & 1.5 & 1.5 & 1.5 & 1.5 \\
       20 & 2.0 & 2.0 & 2.0 & 2.5 \\
       25 & 3.0 & 3.0 & 3.0 & 3.0 \\
       30 & 3.5 & 3.5 & 3.5 & 3.5 \\
       35 & 4.5 & 4.5 & 4.5 & 4.5 \\

'''

thickness = [
    5.2,
    2.0
]
origin_position = [
    2,
    0
]

measurements_index = 1;
n_1 = 1;
measured_pairs = measured_pairs[measurements_index];
thickness = thickness[measurements_index];
origin_position = origin_position[measurements_index];



## precision units
delta_theta1 = 1; ## resolution of 1 degree in units of radians
delta_theta1_in_radians =  delta_theta1 * np.pi/180
delta_t = 0.05; ## resolution of 0.5mm - thickness ------------------------------------------------------------ KEEP TRACK OF UNITS
delta_s = 0.05; ## resolution of 0.5 mm - distance

results = [];
column_titles = ["n2", "delta_n2"];
for pair in measured_pairs:
    theta = pair[0];
    theta_in_radians = theta * np.pi / 180;
    position = pair[1];
    seperation = np.abs(origin_position - position);
    n2 = calculate_n_2(seperation, thickness, n_1, theta_in_radians);
    delta_n2 = calculate_imprecision(seperation, thickness, theta_in_radians, n2)
    print("theta : " + str(theta) + ", seperation : " + str(seperation) + " -> n2 : " + str(n2) + " -> delta_n2 : " + str(delta_n2));
    results.append([n2, delta_n2]);


results = np.array(results);
for index, column in enumerate(results.T):
    print("for " + column_titles[index]);
    print("Mean " + str(np.mean(column)));
    print("Standard Deviation " + str(np.std(column)));
    print("pairs " + str(len(measured_pairs)));
