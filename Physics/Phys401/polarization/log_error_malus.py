import numpy as np;
import matplotlib.pyplot as plt;

def log_error(intensity, theta_in_degrees, delta_theta):
    theta_in_radians = theta_in_degrees * np.pi / float(180);
    print("theta:" + str(theta_in_radians));
    print("tan:" + str(np.tan(theta_in_radians)));
    print("intensity:" + str(intensity));
    error = -2 * intensity * np.tan(theta_in_radians) * float(delta_theta);
    print("error : " + str(error));
    return error;

def malus_law(theta_in_degrees):
    theta_in_radians = theta_in_degrees * np.pi/float(180);
    return 1*np.cos(theta_in_radians)**2*0.98;



errors = [];
thetas = np.arange(0, 360, 15);
for theta in thetas:
    expected_intensity = malus_law(theta);
    print("pre theta" + str(theta))
    method = 2;
    if(method == 1):
        theta = theta % 180; ## from 0 to 90 transform theta
        if(theta > 90): theta = (-1)*(theta - 180) ## converts 110 degrees to 20
        if(theta == 90): theta = 0;
    elif(method == 2):
        theta = theta % 90;

    print("post theta" + str(theta))
    error = log_error(expected_intensity, theta, 1);
    print(error);
    errors.append(np.abs(error));


mean = np.mean(errors);
stdev = np.std(errors);
print(mean);
print(stdev);

fig, ax = plt.subplots()
ax.scatter(thetas, errors, alpha=0.2);

plt.show()
