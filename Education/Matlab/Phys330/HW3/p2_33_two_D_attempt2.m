%{

1/1 - 1/2 + 1/3 - 1/4 + 1/5 - ....
= sum (-1)^(i+1)/i

%}
clear;




    
    
%{
Neutral Box Sumation



box = 2;
i = 0;
j = 0;
[i, j] = return_box_itteration(i, j, box);
i
j
[i, j] = return_box_itteration(i, j, box);
i
j
[i, j] = return_box_itteration(i, j, box);
i
j
[i, j] = return_box_itteration(i, j, box);
i
j
[i, j] = return_box_itteration(i, j, box);
i
j
[i, j] = return_box_itteration(i, j, box);
i
j
%}

threshold = 0.00005;
error = 100;
iteration = 0;


while error > threshold && iteration < 1000
    iteration = iteration + 1;
    
    max_iterations = iteration;
    
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = 0;
    for i = 1:max_iterations % odd numbers
        


        box_peak_radius = i;
        x = 0;
        y = 0;
        [x, y, neutrality_ratio] = return_box_itteration(x, y, box_peak_radius);
        while( x ~= -1 && y ~= -1)
            %fprintf('ratio = %f', neutrality_ratio);
            %neutrality_ratio = 1;
            %fprintf('running x, y as (%d, %d) \n', x, y);
            this_part_value = (-1)^(x+y) * neutrality_ratio/sqrt(x^2 + y^2);
            %size(this_part_value)
            %fprintf('at i (%i) this part contributes (%f)\n', i, this_part_value);
            %fprintf(' --- ');
            %this_part_value
            sum_value = sum_value + this_part_value;
            %(sum_value)
            [x, y, neutrality_ratio] = return_box_itteration(x, y, box_peak_radius);
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
