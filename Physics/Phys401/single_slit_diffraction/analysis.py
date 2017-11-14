import numpy as np;
import matplotlib.pyplot as plt;

## find effective slit width and determine whether this improves plot matching
## fraunhoffer on side between slit and screen, focal length

## optical hole is 4 mm
slit = 1;
if(slit == 1):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.04 * 10 **(-3); ## mm
    wavelength = 633 * 10**(-9); ## nm
    distance = (929-422) * 10**(-3) ## mm
    comparison_range = (-20, 20);
    minimum = 0;
    center = 75.5;
    '''
        (63, 0.1),
        (63.5, 0.1),
        (64, 0.1),
        (64.5, 0.05),
        (65, 0),
        (65.5, 0),
        (66, 0),
        (66.5, 0),
        (67, 0),
        (67.5, 0.3),
        (68, 0.65),
        (68.5, 1.55),
        (69, 2.55),
        (69.5, 3.75),
        (70, 4.75),
        (70.5, 5.65),
        (71, 6.6),
        (71.5, 8.4),
        (72, 9.2),
        (72.5, 9.45),
        (73, 9.4),
        (73.5, 8.45),
        (74, 7.4),
        (74.5, 5.95),
        (75, 4.65),
        (75.5, 3.9),
        (76, 3.2),
        (76.5, 1.7),
        (77, 1.25),
        (77.5, 0.8),
        (78, 0.5),
        (78.5, 0.1),
        (79, 0),
        (79.5, 0),
        (80, 0),
        (80.5, 0),
        (81, 0.05),
        (81.5, 0.1),
        (82, 0.1),
        (82.5, 0.1),
        (83, 0.1),
        (83.5, 0.1),
        (84, 0.05),
        (84.5, 0.05),
        (85, 0),
        (85.5, 0),
        (86, 0),
    '''
    measurements = np.array([
        ## changing apperature, increasing apperature size
        (62, 0),
        (63, 0.05),
        (62.5, 0.1),
        (62, 0.05),
        (61.5, 0.05),
        (61, 0.05),
        (60.5, 0.05),
        (60, 0),
        (59.5, 0.075),
        (59, 0.1),
        (58.5, 0.1),
        (58, 0.1),
        (57.5, 0.1),
        (57, 0.1),
        (56.5, 0.075),
        (56, 0.05),
        (55.5, 0.025),
        (55, 0),
        (54.5, 0),
        (54, 0),
        (57, 0.025),
        (58, 0.05),
        (59, 0.05),
        (60, 0.05),
        (61, 0.025),
        (61.5, 0),
        (62, 0),
        (63, 0.1),
        (62.5, 0.1),
        (62, 0.05),
        (61.5, 0.025),
        (61, 0),
        (60.5, 0),
        (62, 0.025),
        (62.5, 0.025),
        (63, 0.1),
        (63.5, 0.25),
        (64, 0.55),
        (64.5, 0.75),
        (65, 0.9),
        (65.5, 0.9),
        (66, 0.8),
        (67, 0.55),
        (67, 0.4),
        (68, 0.025),
        (69, 0.05),
        (70, 1.35),
        (71, 6.67),
        (72, 10),
        (73, 10),
        (74, 10.1),
        (75, 10.05),
        (76, 10.05),
        (77, 10.05),
        (78, 10),
        (79, 6.67),
        (78, 9.9)

    ]);

    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);

    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - np.min(measurements[:, 1])) / np.max(measurements[:,1]);
elif(slit == 2):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.02 * 10 **(-3); ## mm
    wavelength = 632.8 * 10**(-9); ## nm
    distance = (768.5 - 451.5) * 10**(-3) ## mm
    comparison_range = (-20, 20);
    center = 61.5;

    measurements = np.array([
        (77, 0),
        (76, 0),
        (75, 0.1),
        (74, 0.1),
        (73, 0.25),
        (72, 0.25),
        (71, 0.25),
        (70, 0.05),
        (69, 0),
        (68, 0.25),
        (67, 0.75),
        (66, 2.1),
        (65, 4.6),
        (64, 6.4),
        (63, 8),
        (63.5, 6.4),
        (63, 8.3),
        (62, 10),
        (61, 10),
        (60, 7.6),
        (59, 6.5),
        (58, 3.8),
        (57, 1.8),
        (56, 0.5),
        (55, 0),
        (54, 0),
        (53, 0.1),
        (52, 0.1),
        (51, 0.1),
        (50, 0.1),
        (53, 0.1)
        (49, 0),
        (48, 0),
        (47, 0),
        (72, 0.1),
        (73, 0.1)
    ]);


    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);

    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - np.min(measurements[:, 1])) / np.max(measurements[:,1]);


elif(slit == 3):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.08 * 10 **(-3); ## mm
    wavelength = 632.8 * 10**(-9); ## nm
    distance = (929-420) * 10**(-3) ## mm
    comparison_range = (-20, 20);
    center = 72.5;

    measurements = np.array([
        (84, 0),
        (83, 0),
        (82, 0),
        (81, 0.1),
        (80, 0.05),
        (79, 0.1),
        (78, 0.6),
        (77, 0.6),
        (76, 0),
        (75, 1.9),
        (74, 10),
        (74.5, 6.3),
        (75.5, 0.5),
        (76.5, 0),
        (73, 10),
        (73.5, 10),
        (72, 10),
        (71, 10),
        (70, 4.1),
        (70.5, 7.9),
        (69.5, 1.4),
        (69, 0.1),
        (68.5, 0),
        (68, 0.35),
        (67.5, 0.5),
        (67, 0.55),
        (66.5, 0.4),
        (66, 0.1),
        (65, 0),
        (65.5, 0),
        (64, 0),
        (63, 0),
        (73, 10),
        (73.5, 10),
        (74, 10),
        (74.5, 8.9),
        (75, 6.4),
        (75.25, 1),
        (75.5, 0.55),
        (75, 2.85),
        (74.5, 7.75),
        (75, 2.6),
        (75.5, 1.55),
        (76, 0.1),
        (76.5, 0.05),
        (77, 0.1),
        (77, 0.2),
        (77.25, 0.3),
        (77.5, 0.6),
        (77, 0.4),
        (77.5, 0.55),
        (78, 0.65),
        (78.5, 0.65),
        (79, 0.4),
        (79.5, 0.1),
        (80, 0),
        (80.5, 0.05),
        (81, 0.05),
        (81.5, 0.1),
        (82, 0.1),
        (82.5, 0.1),
        (83, 0),
        (83.5, 0),
        (84, 0),
    ]);


    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);

    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - np.min(measurements[:, 1])) / np.max(measurements[:,1]);


elif(slit == 4):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.16 * 10 **(-3); ## mm
    wavelength = 632.8 * 10**(-9); ## nm
    distance = 2000 * 10**(-3) ## mm
    comparison_range = (-20, 20);
    center = 61.5;

    measurements = np.array([(0, 1)]);

def scalar(y_value, distance, slit_width, wavelength):
    beta = np.pi * slit_width / float(wavelength) * y_value / (np.sqrt(distance**2 + y_value**2));
    # pi / 10^-9
    scalar = np.sin(beta) / beta;
    scalar = scalar**2;
    return scalar;

x = np.arange(-20, 20, 0.05)*10**(-3);
y = [scalar(this_x, distance, slit_width, wavelength) for this_x in x];

measured_x = measurements[:, 0];
measured_y = measurements[:, 1];


fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.2);
ax.scatter(measured_x, measured_y, color="red");

plt.show()
