clear;

threshold = 0.01; %% 1 percent

a = 1;
b = a;

x = [-1:0.02:1]*b;
y = [0:0.02:1]*a;


error = 100;
iteration = -1;
times_crossed = 0;
while times_crossed < 10 && iteration < 1000
    iteration = iteration + 1;
    %n = 11;
    max_iterations = iteration * 2 + 1;
    fprintf('\ncalculating result for n = %d\n', max_iterations);
    sum_value = zeros(length(x), length(y));
    for n = 1:2:max_iterations % odd numbers
        for i = 1:length(x)
            xNow = x(i);
            %xNow
            %fn
            this_part_value = (1/n)*cosh(n*pi*xNow/a)/cosh(n*pi*b/a)*sin(n*pi*y/a);
            %size(this_part_value)
            %fprintf('at i (%i) this part contributes (%f)\n', n, this_part_value);
            %fprintf(' --- ');
            %this_part_value
            %length(this_part_value)
            %length(sum_value(i, :))
            sum_value(i, :) = sum_value(i, :) + this_part_value;
            %(sum_value)
            %sum(sum(sum_value))
            if isnan(sum(sum(sum_value)))
                broken = true;
                surf(last_value)
                error('');
            end
        end
    end

    fprintf('done iterating, the final sum value found is : \n');
    this_value = sum_value;
    %disp(this_value);
    if exist('last_value', 'var');
        difference = (this_value - last_value);
        %difference(1:5)
        %this_value(1:5)
        %last_value(1:5)
        if(false)
            average = (this_value + last_value) / 2;
            error = sum(abs(difference / average));
        else
            error = sum(sum(abs(difference / this_value)));
        end
        if(error < threshold)
            times_crossed = times_crossed + 1;
        else
            times_crossed = 0;
        end;
        fprintf('At iteration (n level) `%d` the error is `%f` (-vs- %f)\n\n', max_iterations, error, threshold);
     
    end
    last_value = this_value;
end

size(last_value)

surf(last_value, x, y)