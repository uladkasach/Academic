import numpy as np;
import matplotlib.pyplot as plt;
import math;

## find effective slit width and determine whether this improves plot matching
## fraunhoffer on side between slit and screen, focal length

data_index = 0;

wavelength = 632.8 * 10**(-9); ## mm

distances = [
    (418 + (1000 - 477)) * 10**(-3), ## mm
    (418 + (1000 - 477)) * 10**(-3) ## mm
];
minimas = [
    np.array([[-0.009, -2],
 [-0.0045, -1],
 [ 0.005, 1],
 [ 0.0095, 2],]),

    np.array([[-0.0095, -2],
 [-0.0045, -1],
 [ 0.005    , 1],
 [ 0.01      , 2],]
)

]


distance = distances[data_index];
minimas = minimas[data_index];

def slit_width_from_maxima(order, y_m, d, wavelength):
    gamma = np.sqrt(d**2 + y_m**2)**(-1);
    a = order * wavelength * (y_m * gamma)**(-1);
    a = np.abs(a);
    return a;


slit_widths = [];
for minima in minimas:
    this_width = slit_width_from_maxima(minima[1], minima[0], distance, wavelength);
    print(this_width);
    slit_widths.append(this_width*10**3);

print("mean width:");
print(np.mean(slit_widths));
