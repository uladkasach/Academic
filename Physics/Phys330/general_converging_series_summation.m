clear;

threshold = 0.0001; %% 1 percent

a = 1;

x = 0.5*a;
y = [0:0.2:1]*a;
z = 1*a;

error = 100;
iteration = -1;
while error > threshold && iteration < 10000
    iteration = iteration + 1;
    %n = 11;
    max_iterations = iteration * 2 + 1; %% Dont forget to modify the for values
    for_interval_n = 1:2:max_iterations;
    for_interval_m = for_interval_n;
    
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = zeros(size(y));
    for n = for_interval_n % odd numbers
            %this_part_value = (1/n)*exp(-n*pi*x/a)*sin(n*pi*y/a); 
            %this_part_value = (1/n)*exp(-n*pi*x/a)*sin(n*pi*y/a); 3.13
        this_part_value = 0;
        for m = for_interval_m
            gamma = pi/a*sqrt(n^2 + m^2);
            this_part_value_part = (1/(n*m))*sinh(gamma * z) / sinh(gamma * a) * sin(n*pi*x/a) * sin(m*pi*y/a);
            this_part_value = this_part_value + this_part_value_part;
        end
        %size(this_part_value)
        %fprintf('at i (%i) this part contributes (%f)\n', i, this_part_value);
        %fprintf(' --- ');
        %this_part_value
        sum_value = sum_value + this_part_value;
        (sum_value)
    end

    fprintf('done iterating, the final sum value found is : \n');
    this_value = sum_value;
    %disp(this_value);
    if exist('last_value', 'var');
        difference = (this_value - last_value);
        average = (this_value + last_value) / 2;
        error = sum(abs(difference / average));
        fprintf('At n level `%d` (iteration %d) the error is `%f`\n\n', max_iterations, iteration, error);
    end
    last_value = this_value;
end

sum_value
