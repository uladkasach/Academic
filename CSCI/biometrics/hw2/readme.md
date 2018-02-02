## requirements:
(1) implement iterative k-means, as described in the class and below, and leave k (number of clusters) as an open parameter to be set by the user -- UG & GR

(2) cluster the image pixels with respect to color -- UG & GR

## grading:
Upload your matlab code (70%) and a 1-page report (30%) of your results (for better illustration, use images as well) and discussion of the results (e.g., how does the choice of k affect the results? how does the face pixel sample size affect the results?)

## installation:

1. unzip the package
2. ensure python package dependencies are satisfied
    - ensure python version is atleast `2.7.12`
    - ensure packages `Pillow` and `Scikit-Learn` are available
        - e.g., `sudo pip install scikit-learn pillow numpy matplotlib`

## running
`python kmeans.py <image_id> <k>`
- image_id: image to segment
    - `1` -> `images/source/haiying.jpg`
    - `2` -> `images/source/lihua.jpg`
- k: cluster count

the output is generated in `/images/pred/`
- example output can be found under `/example/`

**note**: this package caches results. To overwrite cache set the environmental variable `OVERWRITE=true` (e.g., `export OVERWRITE=true`)


## comments:
it is important to note that even though one selects `k=3`, because of random initialization we may actually detect that we have found `k != 3` unique centroids throughout the `n` iterations we evaluated probabilities on. Therefore, **the output may provide more than `k` output class probability maps.**
    - however, we only generate probability maps on clusters that receive more than 5% of the pixel assignments total.
