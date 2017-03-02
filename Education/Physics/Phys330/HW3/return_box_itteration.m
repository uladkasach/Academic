

function [xNew, yNew, neutrality_ratio] = return_box_itteration(x, y, peak_val)
    % start at x = peak_val, y = 0; Increment y untill at peak, then
    % decrement x, building a box;
    xNew = x;
    yNew = y;
    neutrality_ratio = 1/2;
    if(x == 0 && y == 0)
        xNew = peak_val;
        yNew = 0;
        return;
    elseif(x == peak_val && y < peak_val)
        yNew = y + 1;
        if(yNew == peak_val) 
            neutrality_ratio = 1/4;
        end
        return;
    elseif (x == peak_val && y == peak_val)
        xNew = x - 1;
        return;
    elseif (y == peak_val && x == 0)
        %fprintf('found me');
        xNew = 0 -1;
        yNew = 0 -1;
        return;
    elseif (y == peak_val && x < peak_val)
        xNew = x - 1;
        return;
    end
end