import numpy as np;
import matplotlib.pyplot as plt;

## find effective slit width and determine whether this improves plot matching
## fraunhoffer on side between slit and screen, focal length

## optical hole is 4 mm
slit = 2
if(slit == 1):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.04 * 10 **(-3); ## mm
    wavelength = 633 * 10**(-9); ## nm
    distance = (924-374) * 10**(-3) ## mm ----------------------- may be source of imprecision
    comparison_range = (-20, 20);
    minimum = 0;
    center = 66;

    measurements = np.array([
        (65, 8.65),
        (66, 8.55),
        (66.5, 8.3),
        (67.5, 7.5),
        (68.5, 7.2),
        (69.5, 4.6),
        (70.5, 2.85),
        (71.5, 1.05),
        (72.5, 0.25),
        (73, 0.1),
        (73.5, 0),
        (74.5, 0.1),
        (75.5, 0.35),
        (76.5, 0.4),
        (77.5, 0.35),
        (78.5, 0.3),
        (79.5, 0.055),
        (80, 0),
        (80.5, 0.05),
        (81.5, 0.05),
        (82.5, 0.1),
        (83.5, 0.15),
        (84.5, 0.15),
        (85.5, 0.1),
        (86.5, 0.05),
        (87, 0),

        (64, 7.5),
        (63, 5.5),
        (62, 4.1),
        (61, 2.3),
        (60, 0.85),
        (59, 0.3),
        (58, 0.05),
        (57, 0.2),
        (56, 0.35),
        (55.5, 0.4),
        (55, 0.4),
        (54.5, 0.35),
        (54, 0.3),
        (53.5, 0.2),
        (53, 0.15),
        (52.5, 0.1),
        (51.5, 0.05),
        (50.5, 0),
        (50, 0.05),
        (49.5, 0.15),
        (49, 0.19),
        (48, 0.19),
        (47, 0.15),
        (46, 0.1),
        (45, 0.0)

    ])

    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);

    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - minimum) / np.max(measurements[:,1]);

elif(slit == 2):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_width = 0.02 * 10 **(-3); ## mm
    wavelength = 632.8 * 10**(-9); ## nm
    distance = (775-376) * 10**(-3) ## mm ----------------------- may be source of imprecision
    comparison_range = (-20, 20);
    center = 61.5;

    measurements = np.array([
        (62, 8.4),
        (56.5, 0),
        (49, 0),
        (50, 0.05),
        (53, 0),
        (52.5, 0),
        (52, 0.05),
        (51, 0.1),
        (51.5, 0.05),
        (52, 0.01),
        (52.5, 0),
        (53, 0),
        (53.5, 0),
        (54, 0.05),
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

x = np.arange(-40, 40, 0.05)*10**(-3);
y = [scalar(this_x, distance, slit_width, wavelength) for this_x in x];

y_test2 = [scalar(this_x, distance+90*10**(-3), slit_width, wavelength) for this_x in x];

measured_x = measurements[:, 0];
measured_y = measurements[:, 1];


fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.2);
#ax.scatter(x, y_test2, color="blue", alpha=0.2);
ax.scatter(measured_x, measured_y, color="red");

plt.show()
