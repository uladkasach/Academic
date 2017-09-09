fun = @(u, phi) u./sqrt(1 + u.^2 + 2.*u.*cos(phi))

integral2(fun,0,1,0,2*pi)