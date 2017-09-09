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

measured_pairs = [
    [
        ##[0, 2],
        [36, 0.038],
        [32, 0.035],
        [28, 0.032],
        [24, 0.0285],
        [20, 0.025],
        [4, 0.0065],
        [8, 0.0115],
        [12, 0.016],
    ],
    [
        [4, 0.2], 
        [4, 0.2], 
        [4, 0.2], 
        [4, 0.2], 
        [8, 0.4],
        [8, 0.35],
        [8, 0.4],
        [8, 0.35],
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
        [36, 1.35]
    ],
]


thickness = [
    0.052,
    2.0
]

measurements_index = 0;
n_1 = 1;
measured_pairs = measured_pairs[measurements_index];
thickness = thickness[measurements_index];
origin_position = 2;

results = [];
for pair in measured_pairs:
    theta = pair[0];
    theta_in_radians = theta * np.pi / 180;
    seperation = pair[1];
    result = calculate_n_2(seperation, thickness, n_1, theta_in_radians);
    print("theta : " + str(theta) + ", seperation : " + str(seperation) + " -> n_2 : " + str(result));
    results.append(result);
    
    
print("Mean " + str(np.mean(results)));
print("Standard Deviation " + str(np.std(results)));