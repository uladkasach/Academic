
## How to Run
1. ensure `Pillow`/`PIL`, `Numpy`, `skimage`, and `scikit-learn` packages are installed
2. run `python extract.py -h` for arguments list
    - first argument is expected to be the path to the image
        - e.g., `python extract.py images/source/fingerprint_3.jpg`
    - optional argument, `-t` / `--threshold`, defines the threshold value at which to consider a ridge or not
        - e.g., `python extract.py images/source/fingerprint_3.jpy -t 3`

## Processing Steps
1. retreive the image and cast to grayscale
2. detect ridges using hessian_matrix
    - methodology found at  https://stackoverflow.com/questions/48727914/how-to-use-ridge-detection-filter-in-opencv
3. convert ridge "density" to binary ridge image
    - use the threshold to map "intensity" produced by the ridge detection algorithm to binary image
4. skeletonize ridges (ridge thinning) with scikit-image's `skeletonize` method
    - http://scikit-image.org/docs/dev/auto_examples/edges/plot_skeleton.html
5. extract minutae: ridge endings and ridge bifurcations
    - from `Jain, Anil, and Sharath Pankanti. "Automated Fingerprint Identification and." Advances in Fingerprint Technology (2001): 275.`:
        - ridge bifurcations -> 3 ridge pixel neighbors
        - ridge endings -> one ridge pixel neighbor
6. plot results
    - special care taken to overlay minutae over the skeletonized image
    ![fingerprint_3_minutae](https://user-images.githubusercontent.com/10381896/38402956-df80271e-392d-11e8-8f9a-5a923437fdd9.png)
