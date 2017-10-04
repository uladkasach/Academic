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
    return [theta_2, n_2];

def calculate_imprecision_of_both(s, t, n_1, theta_1, delta_theta_1, delta_n1, delta_t, delta_distance):
    distance = s;
    
    theta_2 = np.arctan((s/(2*t*np.sin(np.pi/2 - theta_1))));
    n_2 = n_1*np.sin(theta_1)/np.sin(theta_2);
    
    delta_theta_2 = (-1)*(delta_theta_1 * np.tan(theta_1) + delta_t * t**(-1) + delta_distance*distance**(-1))/ float((1/float(np.cos(theta_2)))*(1/float(np.sin(theta_2))));
    
    print(delta_n1 * np.sin(theta_1))
    print(delta_theta_1 * n_1 * np.cos(theta_1))
    print(delta_theta_2 * n_2 * np.cos(theta_2))
    print(float(np.sin(theta_2)))
    delta_index = (delta_n1 * np.sin(theta_1) +  delta_theta_1 * n_1 * np.cos(theta_1) - delta_theta_2 * n_2 * np.cos(theta_2) ) / float(np.sin(theta_2))

    return [delta_theta_2, delta_index]
    
    

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

measurements_index = 0;
n_1 = 1;
measured_pairs = measured_pairs[measurements_index];
thickness = thickness[measurements_index];
origin_position = 2;

## precision units
delta_theta_1 = 1; ## resolution of 1 degree 
delta_t = 0.5; ## resolution of 0.5mm
delta_distance = 0.5; ## resolution of 0.5 mm
delta_n1 = 0;

if(False):
    results = [];
    column_titles = ["theta_2", "n2"];
    for pair in measured_pairs:
        theta = pair[0];
        theta_in_radians = theta * np.pi / 180;
        seperation = pair[1];
        result = calculate_n_2(seperation, thickness, n_1, theta_in_radians);
        print("theta : " + str(theta) + ", seperation : " + str(seperation) + " -> n_2 : " + str(result[1]));
        results.append(result);
else:
    column_titles = ["delta_theta_2", "delta_n2"];
    # calculate precision
    results = [];
    for pair in measured_pairs:
        theta = pair[0];
        theta_in_radians = theta * np.pi / 180;
        seperation = pair[1];
        result = calculate_imprecision_of_both(seperation, thickness, n_1, theta_in_radians, delta_theta_1, delta_n1, delta_t, delta_distance);
        print("theta : " + str(theta) + ", seperation : " + str(seperation) + " ->  delta_n2 : " + str(result[1]));
        results.append(result);
    
results = np.array(results);
for index, column in enumerate(results.T):
    print("for " + column_titles[index]);
    print("Mean " + str(np.mean(column)));
    print("Standard Deviation " + str(np.std(column)));
    print("pairs " + str(len(measured_pairs)));