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
unique_cluster_mapper = dict();
def retreive_label_for_centroid_and_update_clusters(centroid, label = False):
    if(label == False):
        label = len(unique_cluster_mapper)
        unique_cluster_mapper[label] = {"center" : [0, 0, 0], "count": 0}; ## initialize a new label
        unique_cluster_mapper[label]["center"] = centroid;

    ## DISABLED UPDATING - TAKES TOO MUCH TIME

    ## cluster = unique_cluster_mapper[label];
    #print(cluster["center"]);
    #all = [cluster["center"] for _ in range(cluster["count"])];
    #all.append(centroid);
    #cluster["center"] = np.mean(np.array(all), axis=0);
    #cluster["count"] = len(all);
    #unique_cluster_mapper[label] = cluster;
    return label;

def within(range, val1, val2):
    return np.abs(val1 - val2) <= range;
def map_centroid_to_cluster(centroid):
    centroid = [int(centroid[0]), int(centroid[1]), int(centroid[2])]

    mapped_label = False;
    for key, val in unique_cluster_mapper.iteritems():
        val = val["center"];
        if(within(10, val[0], centroid[0]) and within(10, val[1], centroid[1]) and within(10, val[1], centroid[1])):
            mapped_label = key; ## we found the right label
            break;

    ## retreive label and update centroid
    label = retreive_label_for_centroid_and_update_clusters(centroid, mapped_label);


    ## increment counter
    if(label not in unique_clusters): unique_clusters[label] = 0; ## keep track of unique cluster id's; we will have to make a probability map for each.
    unique_clusters[label] += 1; ## keep track of how many times a pixel is mapped to that cluster; we will use this to not make maps of low quality clusters.

    return label;

def map_labels_to_centers(labels, centers):
    new_labels = [];
    for label in labels:
        new_labels.append(map_centroid_to_cluster(centers[label])); ## convert label to a string as well
    return new_labels;

def kmeans(image,k):
    print '   running k means...'
    kmeans = KMeans(n_clusters=k, n_jobs=2).fit(image)
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

def probability_map(source_path, output_path, k=8, iterations=3):
    global unique_clusters;
    print("");
    print("------ conducting iterative kmeans on " + source_path + " with " + str(k) + " clusters and  " + str(iterations) + " iterations ------")

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
        print("generating results...");
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
    probability_map(source_path, output_path, int(k_number));
