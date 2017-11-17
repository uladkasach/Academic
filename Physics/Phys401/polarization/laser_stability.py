import numpy as np;
import matplotlib.pyplot as plt;

####### stability measurements
values = [
    (0, 7), #50:00
    (30, 7), #50:30
    (60, 7),
    (90, 7),
    (120, 7),
    (150, 7),
    (180, 7),
    (210, 7),
    (240, 7),
    (270, 7),
    (300, 7)
]


measurement_set = 1;
## difference for of 19 angles
if(measurement_set == 1):
    ## for two polarizers, theta is theta difference
    measurements = np.array([
        (0, 8),
        (15, 9.19),
        (30, 8.78),
        (45, 7.62),
        (60, 5.57),
        (75, 2.91),
        (90, 0.95),
        (105, 0),
        (120, 0.3),
        (135, 1.69),
        (150, 3.96),
        (165, 6.05),
        (180, 7.88),
        (195, 9.95),
        (210, 8.55),
        (225, 6.81),
        (240, 4.9),
        (255, 2.61),
        (270, 0.96),
        (285, 0.01),
        (300, 0.21),
        (315, 1.61),
        (330, 3.4),
        (345, 5.54),
        (0, 6.95),
        (15, 7.9),
        (30, 7.5),
        (15, 7.89),
        (30, 7.4),
    ]);
    measurements[:, 1] = measurements[:, 1]/np.max(measurements[:, 1]); ## normalize to zero
    measurements[:, 0] = measurements[:, 0] - measurements[np.argmax(measurements[:, 1]), 0] + 180;

elif(measurement_set == 2):
    ## polarizer 1
    measurements = np.array([
        (0, 5),
        (15, 6.4),
        (30, 7.25),
        (45, 7.55),
        (60, 7.1),
        (75, 6.5),
        (90, 5.19),
        (105, 3.75),
        (120, 2.85),
        (135, 2.45),
        (150, 2.9),
        (165, 3.95),
        (180, 5.25),
        (195, 6.8),
        (205, 7.3),
        (210, 7.4),
        (225, 7.45),
        (240, 7.4),
        (255, 6.7),
        (270, 4.85),
        (285, 3.75),
        (300, 2.85),
        (315, 2.5),
        (330, 2.79),
        (345, 3.85),
        (360, 5)

    ]);
    measurements[:, 1] = measurements[:, 1]/np.max(measurements[:, 1]);
    measurements[:, 0] = measurements[:, 0] - measurements[np.argmax(measurements[:, 1]), 0];
elif(measurement_set == 3):
    ## polarizer 2
    measurements = np.array([
        (0, 5),
        (15, 6),
        (30, 6.3),
        (45, 6.21),
        (60, 6.2),
        (75, 5.85),
        (95, 4.3),
        (90, 4.6),
        (105, 3.7),
        (120, 2.95),
        (135, 2.81),
        (150, 3.01),
        (165, 3.75),
        (180, 4.75),
        (195, 5.55),
        (210, 6.3),
        (225, 6.7),
        (240, 6.35),
        (255, 5.5),
        (270, 4.5),
        (285, 3.7),
        (300, 3.3),
        (315, 3),
        (330, 3.3),
        (345, 4),
        (0, 4.85),
    ]);
    measurements[:, 1] = measurements[:, 1]/np.max(measurements[:, 1]); ## normalize to zero
    measurements[:, 0] = measurements[:, 0] - measurements[np.argmax(measurements[:, 1]), 0] + 180;



#####
# through no polarizers, 9
# through first one, 3.75 (through angle zero)
# add second w/ 90 degree polarizer, get zero
# add 45 instead of 90 degree , 1.15,
# all 3, 0, 45, 90 = 0.4, 0.35 =/= 3.75/4 -> attenuation?

####### mauses law
def mauses_law(max_intensity, theta_in_degrees):
    theta_in_radians = theta_in_degrees * np.pi/180;
    return max_intensity*np.cos(theta_in_radians)**2;

###
range = np.arange(0, 360, 0.1);
intensity = [mauses_law(1, this_theta) for this_theta in range];

measured_range = measurements[:, 0];
measured_intensity = measurements[:, 1];

fig, ax = plt.subplots()
ax.scatter(range, intensity, alpha=0.2);
ax.scatter(measured_range, measured_intensity, color="red");

plt.show()
