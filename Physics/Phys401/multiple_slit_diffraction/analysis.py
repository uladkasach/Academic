import numpy as np;
import matplotlib.pyplot as plt;

## find effective slit width and determine whether this improves plot matching
## fraunhoffer on side between slit and screen, focal length

## optical hole is 4 mm
slit = 2
if(slit == 1):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_count = 2;
    slit_width = 0.04 * 10 **(-3); ## mm
    slit_spacing = 0.125 * 10**(-3) ## mm
    distance = (418 + (1000 - 477)) * 10**(-3) ## mm

    wavelength = 632.8 * 10**(-9); ## nm
    comparison_range = (-30, 30);
    center = 103.5;
    minimum = 0;

    #20 & 1/4
    #### measurememt is extreemly inacurate below one
    measurements = np.array([
        (103.5, 9),
        (103, 7.7),
        (102.5, 5.9),
        (102, 3.35),
        (101.5, 0.6),
        (101, 0.5),
        (100.5, 1.9),
        (100, 4.4),
        (99.5, 5.7),
        (99, 6.1),
        (98.5, 5.5),
        (98, 2.6),
        (97.5, 1.25),
        (97, 0.6),
        (97, 0),
        (96.5, 0.2),
        (96, 0.5),
        (95.5, 1.4),
        (95, 1.95),
        (94.5, 2),
        (94, 1.8),
        (93.5, 1.1),
        (93, 0.5),
        (92.5, 0),
        (92, 0),
        (91.5, 0),
        (91, 0),
        (90.5, 0),
        ## more data could not be found ,intensity too low and data too far out, going to other half
        (103.5, 8.9),
        (104.5, 8.1),
        (105, 5),
        (105.5, 1.9),
        (106, 0.75),
        (106.5, 0.7),
        (107, 2.5),
        (107.5, 5),
        (108, 5.9),
        (108.5, 6.6),
        (109, 5.8),
        (109.5, 2.3),
        (110, 1.45),
        (110.5, 0.5),
        (111, 0.5), ## could be zero
        (111.5, 0.8),
        (112, 1.75),
        (112.5, 2.20),
        (113, 2.30),
        (113.5, 1.75),
        (114, 1.25),
        (114.5, 0.55),
        (115, 0.3),
        (115.5, 0.25),
        (116, 0),
        (117, 0),

    ]);

    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);

    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - minimum);
    measurements[:, 1] = (measurements[:, 1]) / np.max(measurements[:,1]);

elif(slit == 2):
    # apperature - 0.1 mm - results in accurate readings, so light is only incident from that point
    slit_count = 5;
    slit_width = 0.04 * 10 **(-3); ## mm
    slit_spacing = 0.125 * 10**(-3) ## mm
    distance = (418 + (1000 - 477)) * 10**(-3) ## mm

    wavelength = 632.8 * 10**(-9); ## nm
    comparison_range = (-30, 30);
    center = 91;
    minimum = 0;

    '''
        (91, 9.5),
        (91.5, 9.5),
        (92, 4.45),
        (92.5, 0.4),
        (93, 0.4),
        (93.5, 0.4),
        (94, 0.45),
        (94.5, 1.7),
        (95, 4.3),
        (95.5, 9.4),
        (96.5, 1.95),
        (97, 0.1),
        (97.5, 0.1),
        (98, 0.1),
        (98.5, 0.1),
        (99, 0.1),
        (99.5, 0.35),
        (100, 1.6),
        (100.5, 3),
        (101, 2.65),
        (101.5, 0.1),
        (102, 0),
        (102.5, 0),
        (87, 9.4),
        (82, 3.75),
    '''
    #20 & 1/4
    #### measurememt is extreemly inacurate below one
    ## previous measurements lead to 9.4 each time for each local max
    measurements = np.array([ ## snesor has become inxtreemly inaccurate,


        ## double data
        (91, 9),
        (87, 5.75),
        (81.5, 1.6),
        (81, 0.9),
        (80.5, 0.55),
        (80, 0.3),
        (79.5, 0.3),
        (79, 0.3),
        (78.5, 0.3),
        (79, 0.3),
        (81.5, 1.5),
        (82, 1.25),
        (82.5, 0.7),
        (83, 0.4),
        (83.5, 0.3),
        (84, 0.3),
        (84.5, 0.3),
        (85, 0.9),
        (85.5, 1.5),
        (86, 3.4),
        (86.5, 6),
        (87, 3.8),
        (87.5, 0.6),
        (88, 0.35),
        (88.5, 0.3),
        (89, 0.5),
        (89.5, 0.55),
        (90, 1.05),
        (90.5, 2.4),
        (91, 8.9), ## very finiky,went from 4.4 to 7.6 to 8.6 to here
        (91.5, 8.8),
        (92, 5),
        (92.5, 0.45),
        (93, 0.4),
        (93.5, 0.4),
        (94, 0.5),
        (94.5, 0.55),
        (95, 1.05),
        (95.5, 2),
        (96, 4.05),
        (96.5, 4.1), ## went up and down,
        (96, 6.1),
        (97, 1.1),
        (97.5, 0.4),
        (98, 0.35),
        (98.5, 0.35),
        (99, 0.35),
        (99.5, 0.35),
        (100, 0.6),
        (100.5, 1.2),
        (101, 1.25),
        (101.5, 0.65),
        (102, 0.35),
        (102.5, 0.3),
        (103.5, 0.3),
        (103, 0.3),
        (101, 1.45),
        (100.5, 1.25),

    ]);

    # center the data and normalize to meters
    measurements[:, 0] = measurements[:, 0] - center;
    measurements[:, 0] = measurements[:, 0] * 10 **(-3);


    # normalize intensity in terms of I_max
    measurements[:, 1] = (measurements[:, 1] - minimum);
    measurements[:, 1] = (measurements[:, 1]) / np.max(measurements[:,1]);




def scalar(y_value, distance, slit_width, split_spacing, slit_count, wavelength):
    sin_theta = y_value / (np.sqrt(distance**2 + y_value**2));
    beta = np.pi * slit_width / float(wavelength) * sin_theta;
    alpha = np.pi * slit_spacing / float(wavelength) * sin_theta;
    # pi / 10^-9
    slit_width_component = np.sin(beta) / beta;
    slit_spacing_component = np.sin(slit_count * alpha) / np.sin(alpha);
    scalar = slit_width_component * slit_spacing_component;
    #scalar = slit_spacing_component;
    scalar = scalar**2;
    return [scalar, alpha];

intens = scalar(0.05*10**(-3), distance, slit_width, slit_spacing, slit_count, wavelength)
print(intens);



x = np.arange(comparison_range[0], comparison_range[1], 0.05)*10**(-3);
y = [scalar(this_x, distance, slit_width, slit_spacing, slit_count, wavelength)[0] for this_x in x];
y = (y) / np.max(y);






measured_x = measurements[:, 0];
measured_y = measurements[:, 1];


fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.2);
#ax.scatter(x, y_test2, color="blue", alpha=0.2);
ax.scatter(measured_x, measured_y, color="red");
#ax.scatter(x, n_sin, alpha=0.2, color="blue");
#ax.scatter(x, sine, alpha=0.2, color="green");

plt.show()
