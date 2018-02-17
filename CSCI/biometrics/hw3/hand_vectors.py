import matplotlib.pyplot as plt
import numpy as np;
from PIL import Image;
import sys;

src = sys.argv[1]; # "hand1.jpg";
im = Image.open(src); ## e.g., "source/camel_1.jpg"

plt.imshow(im)
plt.axis('image')
pts = plt.ginput(20, 0, mouse_add=1) # it will wait for three clicks

print "The point selected are"
print pts # ginput returns points as tuples


def vector_and_xy(pts, index): ## extract euclidean distance and return x,y pairs to plot on picture for that line
    these_points = [pts[index+0], pts[index+1]];
    delta_x = these_points[0][0] - these_points[1][0];
    delta_y = these_points[0][1] - these_points[1][1];
    distance = np.sqrt(delta_x**2 + delta_y**2);
    x_list = [these_points[0][0], these_points[1][0]]
    y_list = [these_points[0][1], these_points[1][1]]
    return distance, x_list, y_list;

vector = [];
for index in range(2):
    index_use = index*2;
    distance, x, y = vector_and_xy(pts, index_use);
    vector.append(distance);
    plt.plot(x,y,'-o');


print(vector);
plt.show()
