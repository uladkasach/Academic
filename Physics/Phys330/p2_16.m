

r = 0:0.1:3;
a = 1;
b = 2*a;

E0 = r * 0;

E1 = r./a;
E1(r >= a) = 0;

E2 = a./r;
E2(r < a) = 0;
E2(r >= b) = 0;

E = E0 + E1 + E2;

plot(r/a, E);
