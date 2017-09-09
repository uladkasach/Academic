n = 10;
omega = 2*pi/n;


total_work = 0;
for i = 0:n-1
    for j = 0:n-1
        if(i == j) 
            continue
        end;
        this_distance = ((cos(i*omega) - cos(j*omega))^2 + (sin(i*omega) - sin(j*omega))^2)^(1/2);
        this_work = 0.5/this_distance;
        fprintf(' %d, %d \n', i, j);
        fprintf('   this work: %f\n', this_work);
        total_work = total_work + this_work;
    end
end


fprintf('total work : %f', total_work);

        
        