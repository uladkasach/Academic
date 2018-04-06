import numpy as np;
import images.loader as images;
import argparse;
from skimage.feature import hessian_matrix, hessian_matrix_eigvals;
import matplotlib.pyplot as plt;
from skimage.morphology import skeletonize

## parse arguments
parser = argparse.ArgumentParser();
parser.add_argument('image_path', help='Path to image');
parser.add_argument('-t', '--threshold', type=float, default=2)
args = parser.parse_args();

## retreive image
image, size = images.load(args.image_path);
image = images.to_grayscale(image);
print(size);
print(image);
print(image.shape)
#plt.imshow(image);

## detect ridges
def detect_ridges(gray, sigma=3.0):
    # https://stackoverflow.com/questions/48727914/how-to-use-ridge-detection-filter-in-opencv
    hxx, hxy, hyy = hessian_matrix(gray, sigma)
    i1, i2 = hessian_matrix_eigvals(hxx, hxy, hyy)
    maxima_ridges = i1;
    minima_ridges = i2;
    return maxima_ridges, minima_ridges;
ridges, __ = detect_ridges(image);
print(ridges);
print(ridges.shape)
#plt.imshow(ridges);

## convert to binary
def convert_to_binary(ridges, threshold=3):
    binary_ridges = [];
    for row in ridges:
        binary_row = [];
        for pixel in row:
            if(pixel) >= threshold:
                value = 1;
            else:
                value = 0;
            binary_row.append(value);
        binary_ridges.append(binary_row);
    binary_ridges = np.array(binary_ridges);
    return binary_ridges;
binary_ridges = convert_to_binary(ridges, threshold=args.threshold);
#plt.imshow(binary_ridges);

## skeletonize ridges  (ridge thinning)
skeleton = skeletonize(binary_ridges)



## detect minutae
# 1 neighbor -> ridge ending
# 3 neighbors -> biforcation
def calculate_neighbors(image, index):
    # define range
    delta_x_range = [-1, 0, 1];
    delta_y_range = [-1, 0, 1];

    # calculate neighbors
    ridge_neighbors = 0;
    for delta_x in delta_x_range:
        for delta_y in delta_y_range:
            x = index[0] + delta_x;
            y = index[1] + delta_y;
            if(x < 0 or y < 0 or x >= image.shape[0] or y >= image.shape[1]): continue; # skip if out of bounds
            if(image[x,y] == 1):
                ridge_neighbors += 1;

    # subtract 1 since we counted the source image
    ridge_neighbors -= 1;

    # return result
    return ridge_neighbors;
def find_minutae(skeleton):
    minutae = [];
    for x, row in enumerate(skeleton):
        minutae_row = [];
        for y, pixel in enumerate(row):
            if(skeleton[x,y] == 1):# if a ridge, assess if a minutae
                ridge_neighbors = calculate_neighbors(skeleton, (x,y));
                if(ridge_neighbors == 1 or ridge_neighbors == 3):
                    value = 1;
                else:
                    value = 0;
            else: # else, not a minuatae
                value = 0;
            minutae_row.append(value);
        minutae.append(minutae_row);
    minutae = np.array(minutae);
    return minutae;
minutae = find_minutae(skeleton);
print(minutae);


# display results
fig, axes = plt.subplots(nrows=1, ncols=4, sharex=True, sharey=True)
ax = axes.ravel()
ax[0].imshow(image, cmap=plt.cm.gray)
ax[1].imshow(binary_ridges, cmap=plt.cm.gray)
ax[2].imshow(skeleton, cmap=plt.cm.gray)

# show minutae highlighting the skeleton w/ overlay
overlay = np.zeros((minutae.shape[0],minutae.shape[1],4)) # init RGBA overlay matrix
overlay[...,0] = 1. # set the red channel to 1
overlay[...,3] = minutae # use highlight matrix as the alpha value, 1 to show, 0 to hide
ax[3].imshow(skeleton, cmap=plt.cm.gray, alpha=0.2)
ax[3].imshow(overlay)

fig.tight_layout()
plt.show()
