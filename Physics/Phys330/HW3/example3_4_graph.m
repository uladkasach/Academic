

threshold = 0.000005; %% 1 percent

a = 1;
b = 0.5;

full_x = [-1:0.02:1]*b;
full_y = [0:0.02:1]*a;
global_max_n = 0;

full_data = zeros(length(full_x), length(full_y));

for i = 1:length(full_x)
    x = full_x(i);
    y = full_y;
    run('example3_4.m');
    
    full_data(i, :) = last_value; 
end

full_data = full_data / (full_data(1,25)); % v = v/v_0

if(length(full_x) == 1)
    plot(full_y, full_data, '-s')
else
    surf(full_y/a, full_x/b, full_data);
end    
    


    

