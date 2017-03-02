function x = x_of_t(t, A, g, w, phi)
    x = A*exp(-g*t)*cos(w*t-phi); 
end