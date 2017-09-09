A = [ 2 3 1 -2; 5 3 6 -1; 1 3 2 2; 0 4 1 2]
B = [ -1 3 2 1; 4 2 -3 1; 1 0 3 2; 2 -2 1 4]

A11 = [2 3; 5 3]
A12 = [1 -2; 6 -1]
A21 = [1 3; 0 4]
A22 = [ 2 2; 1 2]
    
B11 = [-1 3; 4 2]
B12 = [2 1; -3 1]
B21 = [ 1 0; 2 -2]
B22 = [3 2; 1 4]
    
p1 = (A11 + A22)*(B11+B22)
p2 = (A21 + A22)*(B11)
p3 = (A11)*(B12 - B22)
p4 = (A22)*(B21 - B11)
p5 = (A11 + A12)*(B22)
p6 = (A21 - A11)*(B11 + B12)
p7 = (A12 - A22)*(B21 + B22)

product = [ p1 + p4 - p5 + p7, p3+p5; p2+p4, p1+p3-p2+p6 ]
verify_product = A*B