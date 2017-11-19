import numpy as np;
import matplotlib.pyplot as plt;




def normalize_measurements(measurements, max=None):
    if max is None: max = np.max(measurements[:, 1]);
    measurements[:, 1] = measurements[:, 1]/max; ## normalize to zero
    measurements[:, 0] = measurements[:, 0] - measurements[np.argmax(measurements[:, 1]), 0];
    for index, theta in enumerate(measurements[:, 0]):
        if(theta < 0): measurements[index, 0] = theta+360;
        if(theta >= 360): measurements[index, 0] = theta - 360;

    measurements = measurements[measurements[:,0].argsort()]
    return measurements;


measurement_set = 3;
measures = dict({});
if(measurement_set == 1 or measurement_set == "ALL"):
    ## polarizer one
    measurements = np.array([
        (0, 4),
        (15, 3.8),
        (30, 3.8),
        (45, 3.6),
        (60, 3.5),
        (75, 3.6),
        (90, 3.5),
        (105, 3.5),
        (120, 3.7),
        (135, 3.8),
        (150, 3.8),
        (165, 3.8),
        (180, 3.9),
        (195, 3.9),
        (210, 3.7),
        (225, 3.6),
        (240, 3.5),
        (255, 3.5),
        (270, 3.5),
        (285, 3.6),
        (300, 3.7),
        (315, 3.8),
        (330, 3.8),
        (345, 3.9),
        (360, 3.8),
    ]);
    measurements = normalize_measurements(measurements, max = 8);
    measures[1] = measurements;


if(measurement_set == 2 or measurement_set == "ALL"):
    ## polarizer two
    measurements = np.array([
        (0, 3.5),
        (15, 3.3),
        (30, 3.3),
        (45, 3.1),
        (60, 3),
        (75, 3.1),
        (90, 3.1),
        (105, 3.1),
        (120, 3.2),
        (135, 3.3),
        (150, 3.3),
        (165, 3.4),
        (180, 3.4),
        (195, 3.3),
        (210, 3.3),
        (225, 3.2),
        (240, 3),
        (255, 3),
        (270, 3),
        (285, 3),
        (300, 3),
        (315, 3.1),
        (330, 3.3),
        (345, 3.3),
        (360, 3.4),
    ]);
    measurements = normalize_measurements(measurements, max = 8);
    measures[2] = measurements;


if(measurement_set == 3 or measurement_set == "ALL"):
    ## two polarizers
    measurements = np.array([
        (0, 7.8),
        (15, 7.3),
        (30, 5.8),
        (45, 3.7),
        (60, 1.8),
        (75, 0.5),
        (90, 0),
        (105, 0.6),
        (120, 1.9),
        (135, 3.8),
        (150, 5.8),
        (165, 7.3),
        (180, 7.8),
        (195, 7),
        (210, 5.4),
        (225, 3.4),
        (240, 1.8),
        (255, 0.5),
        (270, 0.1),
        (285, 0.6),
        (300, 1.6),
        (315, 3.6),
        (330, 5.6),
        (345, 7.3),
        (360, 7.9),
    ]);
    measurements = normalize_measurements(measurements, max = 8);
    measures[3] = measurements;


####### mauses law
def mauses_law(max_intensity, theta_in_degrees):
    theta_in_radians = theta_in_degrees * np.pi/180;
    return max_intensity*np.cos(theta_in_radians)**2;

'''
all = (measures[1][:, 1].tolist());
all.extend(measures[2][:, 1].tolist());
all = np.array(all);
print(all);
average = np.mean(all);
stdev = np.std(all);
print(average);
print(stdev);
exit();
'''

## rmse
if(True):
    differences = [];
    for pair in measurements:
        differences.append((pair[1] - mauses_law(1, pair[0]))**2);
    mean = np.mean(differences);
    rmse = np.sqrt(mean);
    print("RMSE : ");
    print(rmse);
    exit();


###
if(True):
    for pair in measurements:
        malus_law_expected =  " & " + "{0:.3f}".format(mauses_law(1, pair[0])) ;
        data_string = "{0:.0f}".format(pair[0]) +  " & " + "{0:.3f}".format(pair[1])  + malus_law_expected + "\\\\";
        print(data_string);

print("--------");

if(measurement_set == "ALL"):
    for index, pair in enumerate(measures[1]):
        print("{0:.0f}".format(pair[0]) +  " & " + "{0:.3f}".format(pair[1])  +  " & " + "{0:.3f}".format(measures[2][index][1]) + "\\\\");
    exit();


range = np.arange(0, 360, 0.1);
intensity = [mauses_law(1, this_theta) for this_theta in range];

measured_range = measurements[:, 0];
measured_intensity = measurements[:, 1];

fig, ax = plt.subplots()
ax.scatter(range, intensity, alpha=0.2);
ax.scatter(measured_range, measured_intensity, color="red");

plt.show()
