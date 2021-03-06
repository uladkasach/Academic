import numpy as np;
import matplotlib.pyplot as plt;


## note, we can not approximate and get an exact angle,
## or can show that error increases w/ failure of approximation of tangent to sin at larger angle


x_0 = (428.6 - 9 + 1.4)*10; # cm -> mm
d = 0.5; #mm
measured = dict({ #mm
    "-0" : -345.9 - 0.5,
    #"0" : -5.5,
    "0" : 59,
    "1" : 140,
    "2" : 205,
    "3" : 261.2,
    "4" : 310.1,
    "5" : 355.9,
    "6" : 397.1,
    "7" : 436.5,
    "8" : 473.2,
    "9" : 508.5,
    "10" : 541.9,
    "11" : 574.2,
    "12" : 605.5,
    "13" : 635.5,
    "14" : 663.2,
    "15" : 691.8,
    "16" : 719.2,
    "17" : 751,
    "18" : 772,
})

bar_width = 67; #mm

## normalize_measurements
def normalize_measurements(bar_width, measurements):
    ## negative values are seperated from positive values by bar width
    ## zero is actually to be defined as half way between 0 and -0

    ## 1 - convert all to scale where 0 is at "-0"
    zero = measurements["-0"];
    new_measure = dict();
    for key, val in measurements.iteritems():
        if(val >= 0): val = val + bar_width;
        val = val - zero;
        new_measure[key] = val;

    ## find new zero, being center between "-0" and "0"
    shift = (new_measure["-0"] + new_measure["0"])/float(2);

    ## shift all measurements to final value
    final_measure = dict();
    for key, val in new_measure.iteritems():
        final_measure[key] = val - shift;
    return final_measure;

## calc wavelength
def wavelength(d, x_0, y_0, n, y_n):
    ## convert all to m
    millimeter = 10**(-3);
    d = d*millimeter;
    x_0 = x_0*millimeter;
    y_0 = y_0*millimeter;
    y_n = y_n*millimeter;

    lamb = (d / float(2 * n)) * (y_n**2 - y_0**2) / float(x_0**2)
    return lamb;

def log_error(y_n, y_0, wavelength, x_0):
    wavelength = wavelength*10**(-9) # convert to m's
    millimeter = 10**(-3); # cnvert rest to m
    x_0 = x_0*millimeter;
    y_0 = y_0*millimeter;
    y_n = y_n*millimeter;

    delta_y = 1*millimeter;
    delta_x = 5*millimeter;
    part_1 = (delta_y * y_n - delta_y * y_0)/float(y_n**2 - y_0**2)
    part_2 = -2 * delta_x / float(x_0);
    print("part 1 error:" + str(part_1));
    print("part 2 error:" + str(part_2));
    print("total error :" + str(part_1 + part_2));
    error = wavelength * 2 * (part_1 + part_2) ;
    return error* 10**(9) ; #convert to nm

measurements = normalize_measurements(bar_width, measured);
print(measurements);
print("---");
print( measurements["0"]);
ns = np.arange(1, 14, 1);
lens = [];
errors = [];
for n in ns:
    len = wavelength(d, x_0, measurements["0"], n, measurements[str(n)])*10**9;
    print(str(n) + "&" + str(measurements[str(n)]) + "&" + str(round(len*100)/float(100)) + "\\\\");
    lens.append(len);
    this_error = log_error(measurements[str(n)], measurements["0"], len, x_0);
    errors.append(this_error);

print("log errrors mean:");
print(np.mean(errors));
exit();
print("mean:");
print(np.mean(lens))

exp = [];
for n in ns:
    exp.append(632.8);

fig, ax = plt.subplots()
ax.scatter(ns, lens, color = "green");
ax.scatter(ns, exp, color="blue", alpha=0.2);

plt.show()
