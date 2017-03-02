
if( ~exist('y', 'var'))
    threshold = 0.001; %% 1 percent

    a = 1;
    b = 0.5;

    x = 0.9*b;
    y = 0.5*a;
end

error = 100;
iteration = -1;
times_crossed = 0;
last_value = 0;
while times_crossed < 1 && iteration < 1000
    iteration = iteration + 1;
    %n = 11;
    max_iterations = iteration * 2 + 1;
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = zeros(size(y));
    for n = 1:2:max_iterations % odd numbers
        %fn
        this_part_value = (1/n)*cosh(n*pi*x/a)/cosh(n*pi*b/a)*sin(n*pi*y/a);
        %size(this_part_value)
        %fprintf('at i (%i) this part contributes (%f)\n', n, this_part_value);
        %fprintf(' --- ');
        %this_part_value
        sum_value = sum_value + this_part_value;
        %sum(sum_value)
    end

    fprintf('done iterating, the final sum value found is : \n');
    this_value = sum_value;
    %disp(this_value);
    if exist('last_value', 'var');
        difference = (this_value - last_value);
        %difference(1:5)
        %this_value(1:5)
        %last_value(1:5)
        if(true)
            average = (this_value + last_value) / 2;
            error = sum(abs(difference / average));
        else
            error = sum(abs(difference / this_value));
        end
        
        if(error < threshold)
            times_crossed = times_crossed + 1;
        else
            times_crossed = 0;
        end;
        fprintf('At iteration (n level) `%d` the error is `%f` (-vs- %f)\n\n', max_iterations, error, threshold);
    end
    before_last = last_value;
    last_value = this_value;
end
