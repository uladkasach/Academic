import numpy as np;

N = 10**6; # one million
a = 2;
b = 5;
x = np.random.uniform(a,b, N)


print("calculated:")
print(np.mean(x));
print(np.var(x));

print("expected:");
mean = (b + a )/float(2);
var = (b**3 - a**3)/float(3*(b-a)) - mean**2;
print(mean);
print(var);
