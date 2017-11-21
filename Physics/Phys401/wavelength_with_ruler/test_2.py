
x_0 = (428.6 - 9 + 1.4)*10**(-2); # cm -> m
d = 0.5*10**(-3); #mm -> m

measured = dict({ #mm
    "-0" : -345.9 - 0.5,
    "0" : -5.5,
    "1" : 59,
    "2" : 140,
    "3" : 205,
})
bar_width = 67*10**(-3); #mm -> m

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
    ## expects all in m
    lamb = (d / float(2 * n)) * (y_n**2 - y_0**2) / float(x_0**2)
    return lamb;


measurements = normalize_measurements(bar_width, measured);

len = wavelength(d, x_0, measurements["0"]*10**(-3), 1, measurements["1"]*10**(-3));
print(len);
