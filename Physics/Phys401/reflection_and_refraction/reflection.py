#############################
## We measure seperation distance and know thickness. We know that s = tsin(theta_1 - theta_2)/cos(theta_2) -> theta_2 = arctan([sin(theta_1) - s/t]/cos(theta_1))
## We can determine the index of refraction by snells law: n_2 = sin(theta_1)/sin(theta_2);
## We'd like to, first, evaluate errors of the measurements we had. We'll use log-errors in addition to average and stdev:
#############################
import numpy as np;


def calculate_n_2(s, t, n_1, theta_1):
    theta_2 = np.arctan((s/(2*t*np.sin(np.pi/2 - theta_1))));
    print(theta_2 * 180 / np.pi);
    print("ideal theta2 = " + str(np.arcsin((1/1.5)*np.sin(theta_1))));
    n_2 = n_1*np.sin(theta_1)/np.sin(theta_2);
    return n_2;

def calculate_imprecision(seperation, thickness, theta_in_radians, n2):

    theta1 = theta_in_radians;
    delta_theta1 = delta_theta1_in_radians;
    s = float(seperation);
    t = float(thickness);
    n2 = float(n2);
    print("s : " + str(s) + ", t : " + str(t) + ", theta1 : " + str(theta1 * 180 / np.pi) + ", n2 : " + str(n2))


    part1 = np.cos(theta1) / np.sin(theta1) * delta_theta1;
    print(np.cos(theta1));
    print(np.sin(theta1));
    print("p1: " + str(part1));

    part2_divisor = ((s)**2 + 4 * t**2 * (np.cos(theta1))**2);
    print("part2_divisor :"  + str(part2_divisor));
    part2 = (s*delta_s + 4*(delta_t * np.cos(theta1) - delta_theta1 * t * np.sin(theta1))) / part2_divisor;
    print("p2: " + str(part2));

    part3 = (2 * delta_s / s)
    print("p3: " + str(part3));

    delta_n2 = n2 * (part1 + part2 + part3);


    print("delta_n2 " + str(delta_n2));
    return delta_n2;


measured_pairs = [
    [
        [4, 6.5],
        [4, 6.5],
        [4, 6.5],
        [8, 11.5],
        [8, 11.0],
        [8, 11.5],
        [12, 16.5],
        [12, 16.0],
        [12, 15.5],
        [16, 20.5],
        [16, 20.5],
        [16, 20.5],
        [20, 25.0],
        [20, 24.5],
        [20, 25.0],
        [24, 28.5],
        [24, 28.5],
        [24, 28.5],
        [28, 32.0],
        [28, 31.5],
        [28, 32.0],
        [32, 35.0],
        [32, 35.5],
        [32, 35.0],
        [36, 38.0],
        [36, 37.5],
    ],
    [
        [4, 0.2],
        [4, 0.2],
        [4, 0.2],
        [8, 0.4],
        [8, 0.35],
        [8, 0.4],
        [12, 0.55],
        [12, 0.5],
        [12, 0.5],
        [16, 0.75],
        [16, 0.7],
        [16, 0.7],
        [20, 0.9],
        [20, 0.85],
        [20, 0.85],
        [24, 1.05],
        [24, 1.00],
        [24, 1.05],
        [28, 1.2],
        [28, 1.15],
        [28, 1.1],
        [32, 1.30],
        [32, 1.25],
        [32, 1.25],
        [36, 1.40],
        [36, 1.40],
        [36, 1.3],
    ],
]

'''

       28 & 32.0 & 31.5 & 32.0 \\
       32 & 35.0 & 35.0 & 35.5 \\
       36 & 38.0 & 37.5 &  \\

'''

thickness = [
    52,
    2.0
]

measurements_index = 1;
n_1 = 1;
measured_pairs = measured_pairs[measurements_index];
thickness = thickness[measurements_index];
origin_position = 2;

## precision units
delta_theta1 = 1; ## resolution of 1 degree in units of radians
delta_theta1_in_radians =  delta_theta1 * np.pi/180
delta_t = 0.05; ## resolution of 0.5mm - thickness
delta_s = 0.05; ## resolution of 0.5 mm - distance

results = [];
column_titles = ["n2", "delta_n2"];
for pair in measured_pairs:
    theta = pair[0];
    theta_in_radians = theta * np.pi / 180;
    seperation = pair[1];
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
