## problem 3.6 of optics pedrotti ed. 3
import numpy as np;
import matplotlib.pylab as plt;

## inputs
apex_angle = 60;
n = 1;
n_prime = 1.52;
theta_1 = np.arange(1,89,1);


def deg_to_rad(deg):
    return deg * np.pi / float(180);
def rad_to_deg(rad):
    return rad * 180 / np.pi;
## calc
theta_1_prime = rad_to_deg(np.arcsin(n/float(n_prime) * np.sin(deg_to_rad(theta_1))));

theta_2_prime = apex_angle - theta_1_prime;
theta_2 = rad_to_deg(np.arcsin(n_prime/float(n) * np.sin(deg_to_rad(theta_2_prime))));

total_deviation = theta_1 - theta_1_prime + theta_2 - theta_2_prime;

plt.plot(theta_1, total_deviation);
plt.xlabel('Entrance Angle (degrees)')
plt.ylabel('Total Deviation')
plt.axis('tight')
#plt.show()
plt.draw();
plt.savefig("prism_incident_vs_deviation.png");