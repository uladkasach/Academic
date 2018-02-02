## note, feature space is spanned by 3 dimensions: (r, g, b). not by spacial image dimensions, (x, y).
## i.e., image = list of data points which we want to cluster

from sklearn.cluster import KMeans;
import numpy as np;
import images.loader as images;
import util;
import sys;
import os;
import json;

unique_clusters = dict({});

def map_labels_to_centers(labels, centers):
    new_labels = [];
    for label in labels:
        new_labels.append(str(centers[label])); ## convert label to a string as well
    return new_labels;

def kmeans(image,k):
    print '   running k means...'
    kmeans = KMeans(n_clusters=k).fit(image)
    #print kmeans.labels_[:10];
    #print kmeans.cluster_centers_
    labels = kmeans.labels_;
    centers = kmeans.cluster_centers_;
    labels = map_labels_to_centers(labels, centers);
    return labels;

def aggregate_results(agg, new):
    global unique_clusters;
    if(agg == False): agg = [{} for _ in range(len(new))];
    for index, value in enumerate(new):
        if(value not in unique_clusters): unique_clusters[value] = 0; ## keep track of unique cluster id's; we will have to make a probability map for each.
        unique_clusters[value] += 1; ## keep track of how many times a pixel is mapped to that cluster; we will use this to not make maps of low quality clusters.
        if(value not in agg[index]): agg[index][value] = 0;
        agg[index][value] += 1;
    return agg;

def calculate_probabilities_for_pixel(pixel, iterations):
    #print(unique_clusters);
    prob = dict();
    for cluster in unique_clusters:
        if cluster not in pixel:
             prob[cluster] = 0;
        else:
            prob[cluster] = pixel[cluster]/float(iterations); # divide by total clusterings
    #print(json.dumps(prob, indent=2));
    return prob;

def map_probability_to_color(probability):
    value = int(255 * probability);
    return [value, value, value];

def map_results_to_probabilies(results, iterations):
    probability_map = dict({}); ## will be an "image" of "pixels" for each cluster. e.g., {cluster1:[], cluster2:[],...}
    for pixel in results:
        prob = calculate_probabilities_for_pixel(pixel, iterations);
        for cluster, probability in prob.iteritems(): ## map each cluster key to the probability map
            if(cluster not in probability_map): probability_map[cluster] = [];
            color = map_probability_to_color(probability);
            probability_map[cluster].append(color);
            #print(color);
        #print(json.dumps(probability_map, indent=2));
    return probability_map;


def filter_unique_clusters(clusters, size, iterations):
    total_pixels = size[0] * size[1] * iterations;
    threshold_pixels = total_pixels * 0.05;
    pop_clusters = [];
    for key, value in clusters.iteritems():
        if(value < threshold_pixels): continue;
        pop_clusters.append(key);
    return pop_clusters;

def probability_map(source_path, output_path, k=8, iterations=10):
    global unique_clusters;
    print("");
    print("------ conducting iterative kmeans on " + source_path + " with " + str(iterations) + " iterations ------")

    bool_overwrite = "OVERWRITE" in os.environ and os.environ["OVERWRITE"] == "true"; ## if environmental variable set to overwrite, overwrite
    if(os.path.isfile(output_path) and not bool_overwrite):
        print(output_path + " already exists");
        return True;

    image, size = images.load(source_path);
    image = images.unravel(image, size);
    print 'image[:5] : ';
    print image[:5];

    if(False): ## to test the reravel operation
        image = images.reravel(image, size);
        images.save(image, 'test.jpg');
        exit();

    cache = util.load_from_cache(source_path + str(k) + str(iterations) + ".pkl");
    if(cache == False):
        full_results = False;
        for index in range(iterations):
            these_results = kmeans(image, k);
            full_results = aggregate_results(full_results, these_results);
        unique_clusters = filter_unique_clusters(unique_clusters, size, iterations);
        util.save_to_cache("full_results.pkl", [full_results, iterations, unique_clusters]);
    else:
        full_results, iterations, unique_clusters = cache;

    print "unique clusters:";
    print(unique_clusters);

    probabilities = map_results_to_probabilies(full_results, iterations);
    #print(probabilities);
    cluster_count = 0;
    for cluster, map in probabilities.iteritems():
        map = np.array(map);
        prediction = util.map_probabilities_to_image(image, map);
        prediction = images.reravel(prediction, size);
        try:
            images.save(prediction, output_path + ".cluster_" + str(cluster_count) + ".jpg");
        except TypeError:
            print("type error occured when attempting to save probability map...");
        cluster_count += 1;
    return True;

if __name__ == "__main__":
    print sys.argv
    if(len(sys.argv) < 3):
        print "error. image number or k number is not defined.";
        exit();
    image_number = sys.argv[1];
    k_number = sys.argv[2];

    source_path, output_path = util.name_gen(image_number, k_number);
    probability_map(source_path, output_path);
