function x = x_dot_of_t(t, A, g, w, phi)
    x = A*(-g)*exp(-g*t)*cos(w*t-phi) + A*exp(-g*t)*(-w)*sin(w*t-phi); 
end