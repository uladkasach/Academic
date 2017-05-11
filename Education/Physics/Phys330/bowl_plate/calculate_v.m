function potential = calculate_v(q, r, d, theta)
   %% V = V_0 + f
   e_0 = 1;
   
   V_0 = q/(4*pi*e_0) * (r^2 + d^2 - 2*r*d*cos(theta))^(-1/2);
   
   f_1 = 0;
   max_l = 10;
   
    
   
   
    
end