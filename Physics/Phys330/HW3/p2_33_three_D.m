%{

1/1 - 1/2 + 1/3 - 1/4 + 1/5 - ....
= sum (-1)^(i+1)/i

%}
clear;



threshold = 0.001;
error = 100;
iteration = 0;
while error > threshold && iteration < 10000000
    iteration = iteration + 1;
    
    max_iterations = iteration;
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = 0;
    for i = 0:max_iterations % odd numbers
        for j = 0:max_iterations
            
            for k = 0:max_iterations
                if(i == 0 && j == 0 && k == 0)
                    continue;
                end

                this_part_value = (-1)^(i+j+k)/sqrt(i^2 + j^2 + k^2);
                %size(this_part_value)
                %fprintf('at i (%i) this part contributes (%f)\n', i, this_part_value);
                %fprintf(' --- ');
                %this_part_value
                sum_value = sum_value + this_part_value;
                %(sum_value)
            end
            
        end
    end

    fprintf('done iterating, the final sum value found is : \n');
    this_value = sum_value
    
    if exist('last_value', 'var');
        difference = (this_value - last_value);
        average = (this_value + last_value) / 2;
        error = sum(abs(difference / average));
        fprintf('At iteration (n level) `%d` the error is `%f`\n\n', max_iterations, error);
    end
    last_value = this_value;
end