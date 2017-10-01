# ch 4, p 13
import numpy as np;
import matplotlib.pylab as plt;


emmisivity = 0.4;
T = (451 - 32) * 5 / float(9) + 273; ## kelvin from farenheight

wavelength = np.arange(0.002, 60, 0.1) * 10**(-6); ## microns

h = 4.1357 * 10**(-15); #eV s
c = 299792458; # m/s
kb = 8.62*10**(-5) #eV/K
excitance = emmisivity * 2 * np.pi * h * c**2 / wavelength**5 * (np.exp(h*c/(wavelength * kb * T)) - 1)**(-1)

plt.plot(wavelength*10**(6), excitance);
plt.xlabel('Wavelength (microns)')
plt.ylabel('Spectral Radiant Excitance')
plt.axis('tight')
#plt.show()
plt.draw();
plt.savefig("spectral_excitance_graybody.png");