g = 9.8;
v_0 = 800;
a = 37*pi/180;
l = -50;
w = 2*pi/(24*60*60); %% 2pi every 24 hours in seconds

t_final = (2*v_0*sin(a))/(g - 2*v_0*w*cos(l)*sin(a));
t = 0:0.01:t_final;

x = 1/3*w*g*t.^3*cos(l) - w*t.^2*v_0*sin(a)*cos(l) + v_0*cos(a)*t;
y = -w*v_0*cos(a)*t.^2*sin(l);
z = -1/2*g*t.^2 + v_0*sin(a)*t + w*(v_0*sin(a))*t.^2*cos(l)


plot3(x,y,z);