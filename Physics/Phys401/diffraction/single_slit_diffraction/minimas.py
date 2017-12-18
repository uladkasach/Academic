import numpy as np;
import matplotlib.pyplot as plt;
import math;

## find effective slit width and determine whether this improves plot matching
## fraunhoffer on side between slit and screen, focal length

data_index = 1;

wavelength = 632.8 * 10**(-9); ## mm

distances = [
    (929-420) * 10**(-3), ## mm
    (924-374) * 10**(-3),
];
minimas = [
    np.array([
        [-0.004, 1    ],
        [ 0.0035, 1    ],
        [ 0.004, 1    ]
    ]),
    np.array([[-0.0155, -2        ],
 [-0.008, -1],
 [ 0.0075, 1],
 [ 0.014, 2]])

]


distance = distances[data_index];
minimas = minimas[data_index];

def slit_width_from_minima(order, y_m, d, wavelength):
    gamma = np.sqrt(d**2 + y_m**2)**(-1);
    b = order * wavelength * (y_m * gamma)**(-1);
    b = np.abs(b);
    return b;


slit_widths = [];
for minima in minimas:
    this_width = slit_width_from_minima(minima[1], minima[0], distance, wavelength);
    print(this_width);
    slit_widths.append(this_width*10**3);

print("mean width:");
print(np.mean(slit_widths));
