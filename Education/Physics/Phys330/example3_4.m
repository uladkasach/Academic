threshold = 0.01; %% 1 percent

a = 1;

x = 0*a;
y = [0:0.00001:1]*a;

error = 100;
iteration = -1;
while error > threshold && iteration < 10
    iteration = iteration + 1;
    %n = 11;
    max_iterations = iteration * 2 + 1;
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = zeros(size(y));
    for n = 1:2:max_iterations % odd numbers
        this_part_value = (1/n)*exp(-n*pi*x/a)*sin(n*pi*y/a);
        %size(this_part_value)
        %fprintf('at i (%i) this part contributes (%f)\n', i, this_part_value);
        %fprintf(' --- ');
        %this_part_value
        sum_value = sum_value + this_part_value;
        %(sum_value)
    end

    fprintf('done iterating, the final sum value found is : \n');
    this_value = sum_value;
    %disp(this_value);
    if exist('last_value', 'var');
        difference = (this_value - last_value);
        average = this_value + last_value / 2;
        error = sum(abs(difference / average));
        fprintf('At iteration (n level) `%d` the error is `%f`\n\n', max_iterations, error);
    end
    last_value = this_value;
end
