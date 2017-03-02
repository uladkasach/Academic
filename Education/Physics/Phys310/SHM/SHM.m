clear;


%%%%%%%%%%%%
%% Initialize Values and Load Functions
%%%%%%%%%%%%
addpath('/');
A = 1;
g = 0.2;
k = 1;
m = 1;
phi = pi/2;
w = sqrt(k/m);
t_count = 100;
t = [1:t_count]*pi/16;


%%%%%%%%%%%%
%% Generate Data
%%%%%%%%%%%%
x = [1:t_count]*0;
x_dot = [1:t_count]*0;
KE = [1:t_count]*0;
PE = [1:t_count]*0;
E = [1:t_count]*0;
for index = [1:t_count]
    thisT = t(index);
    
    thisX = x_of_t(thisT, A, g, w, phi);
    x(index) = thisX;
    
    thisX_dot = x_dot_of_t(thisT, A, g, w, phi);
    %%disp (thisX_dot);
    x_dot(index) = thisX_dot;
    
    thisKE = 1/2 * m * thisX_dot^2;
    KE(index) = thisKE;
    
    thisPE = 1/2 * k * thisX^2;
    PE(index) = thisPE;
    
    E(index) = thisKE + thisPE;
end;


figure 
subplot(3,1,1)
plot(t,x)
title ('X vs T')


subplot(3,1,2)
plot(t,x_dot)
title ('X Dot vs T')



subplot(3,1,3)
plot(t,E)
title ('Total Energy vs T')

