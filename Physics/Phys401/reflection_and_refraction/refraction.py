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
        [10, 0.1],
        [15, 0.15],
        [20, 0.2],
        [25, 0.3],
        [30, 0.35],
        [35, 0.45],
    ]
    
]

thickness = [
    5.2,
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
    position = pair[1];
    seperation = origin_position - position;
    result = calculate_n_2(seperation, thickness, n_1, theta_in_radians);
    print("theta : " + str(theta) + ", seperation : " + str(seperation) + " -> n_2 : " + str(result));
    results.append(result);
    
    
print("Mean " + str(np.mean(results)));
print("Standard Deviation " + str(np.std(results)));