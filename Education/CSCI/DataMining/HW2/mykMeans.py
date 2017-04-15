import sys;
import numpy;
import random;




##############################################################################
## Define K-Means Algorithm and support functions
#############################################################################
def calculate_SSE(v1, v2):
    '''
    total_E = 0;
    for i in range(len(v1)):
        this_v1_element = v1[i];
        this_v2_element = v2[i];
        this_error = (this_v1_element - this_v2_element)**2;
        total_E += this_error;
    '''
    #print(v1);
    #print(v2);
    total_E = sum(((v1 - v2))**2)
    #print(total_E);
    return total_E;
def find_closest_cluster_for(data_point, centroids_set):
    distances = [];
    for index, centroid in enumerate(centroids_set):
        this_distance = calculate_SSE(data_point, centroid);
        distances.append(this_distance);
        if 'min_distance' not in locals() or min_distance >= this_distance:
            #print("--" + str(index) + " for " + str(this_distance));
            min_distance = this_distance;
            min_distance_index = index;
    #print(distances);
    #print("min distance: ", min_distance_index);
    return min_distance_index;
def calculate_centroid_for(this_cluster, old_centroid):
    if(len(this_cluster) == 0):
        return old_centroid;
    sum_vector = numpy.zeros(len(this_cluster[0])); 
    for this_element in this_cluster:
        sum_vector += this_element;
    new_centroid = sum_vector / float(len(this_cluster));
    return new_centroid;

##########################################
## Define K-Means
##########################################
def k_means_algorithm(K, the_data, threshold_difference = 0.001, initial_centroid_indicies = None):
    #######################
    ## Generate Initial Centroids
    #######################
    initial_centroids = [];
    if(initial_centroid_indicies is None):
        chosen_values = [];
        while len(initial_centroids) < K:
            random_value = random.randint(0,len(the_data)-1);
            #random_value = len(initial_centroids);
            if(random_value in chosen_values):
                continue;
            chosen_values.append(random_value);
            initial_centroids.append(the_data[random_value]);
    else:
        print("Selecting initial centroids from user choice...");
        chosen_values = [];
        for index in initial_centroid_indicies:
            if(index in chosen_values):
                print("Warning - an initial centroid was selected twice.")
            initial_centroids.append(the_data[index]);
            
    initial_centroids = numpy.array(initial_centroids);
    print("Initial Centroids: ");
    print(initial_centroids);
    #######################
    ## Run K-Means
    #######################
    centroids = initial_centroids;
    loop_index = 0;
    #print(centroids);
    while 'difference' not in locals() or difference > threshold_difference:
        loop_index += 1;
        #########
        ## Cluster Assignment
        #########
        clusters = [[] for i in range(K)];
        assignments = numpy.zeros(len(the_data), 'int') - 1;
        for index, this_data in enumerate(the_data):
            closest_cluster_index = find_closest_cluster_for(this_data, centroids);
            assignments[index] = closest_cluster_index;
            clusters[closest_cluster_index].append(this_data);
            #print(centroids);
            #print(this_data);
            #print(clusters);
            #exit();
        #########
        ## Centroid Update
        #########
        old_centroids = centroids;
        #new_centroids = numpy.zeros(centroids.shape);
        new_centroids = [];
        for index, this_cluster in enumerate(clusters):
            this_new_centroid = calculate_centroid_for(this_cluster, old_centroids[index]);
            #new_centroids[index] = this_new_centroid;
            new_centroids.append(this_new_centroid);
        centroids = new_centroids;
        #print(centroids);
        #for a_cluster in clusters:
        #    print(len(a_cluster));
        print(assignments);
        print(new_centroids);
        
        #########
        ## Calculate Difference
        #########
        total_difference = 0;
        for i in range(K):
            this_old_centroid = old_centroids[i];
            this_new_centroid = new_centroids[i];
            this_difference = calculate_SSE(this_old_centroid, this_new_centroid);
            total_difference += this_difference;
        difference = total_difference;
        
    #####################
    ## Calculate SSE for each cluster
    #####################
    total_error = [[] for i in range(K)];
    for index, this_cluster in enumerate(clusters):
        this_centroid = centroids[index];
        total_cluster_error = 0;
        for element in this_cluster:
            this_error = calculate_SSE(element, this_centroid);
            total_cluster_error += this_error;
        total_error[index] = total_cluster_error;
    cluster_error = total_error;
            
        
        
    return [loop_index, centroids, cluster_error, clusters, assignments];
        
        




if __name__ == "__main__":
    #########################################
    ## Read User Inputs
    #########################################
    DATA_SOURCE = sys.argv[1];
    K = int(sys.argv[2]);
    if(len(sys.argv) > 3):
        INITIAL_CENTROID_SOURCE = sys.argv[3];
    else:
        INITIAL_CENTROID_SOURCE = None;


    print("Loading data from " + DATA_SOURCE + "...");    
    #########################################
    ## Load Input Data
    #########################################
    the_data = [];
    f = open(DATA_SOURCE, 'r');
    for line in f.readlines():
        parts = line.rstrip().split(",");
        this_data = numpy.array([float(i) for i in parts[:]]);
        #print(this_data);
        the_data.append(this_data);
    f.close();
    the_data = numpy.array(the_data);
    #print(the_data);
    #print(len(the_data));
    
    
    ##########################################
    ## Determine Initial Centroid Indicies if they exist
    ##########################################
    if(INITIAL_CENTROID_SOURCE is not None):
        initial_centroid_indicies = [];
        f = open(INITIAL_CENTROID_SOURCE, 'r');
        for line in f.readlines():
            this_index = int(line.rstrip());
            initial_centroid_indicies.append(this_index);
        f.close();
        initial_centroid_indicies = numpy.array(initial_centroid_indicies);
        print(initial_centroid_indicies);
        print(K);
        if(len(initial_centroid_indicies) != K):
            print("List of initial centroid indicies must be same length as K. Error.");
            exit();
    else:
        initial_centroid_indicies = None;


    TEST = False;
    if(TEST == True):
        from sklearn import datasets;
        import matplotlib.pyplot as plt;
        Xi, yi = datasets.make_blobs(500, random_state=1111)
        print(yi[0:10]);
        Xi = Xi.astype(numpy.float32)
        the_data = Xi;
    
    print("Running K-Means...");
    iterations, centroids, cluster_error, clusters, assignments = k_means_algorithm(K, the_data, initial_centroid_indicies = initial_centroid_indicies);
    #print(iterations);
    #print(centroids);
    #print(cluster_error);
    #print(assignments[0:10]);

    if(TEST == True):
        plt.scatter(*Xi.T, c='k', lw=0);
        plt.scatter(*Xi.T, c=assignments, lw=0, vmax=K + 0.5, label='data');
        plt.scatter(*centroids.T, c='none', s=100, edgecolor='r', lw=2, label='prototypes');
        plt.legend(scatterpoints=3);
        plt.show()


    ##########################################
    ## Output Requested Results
    ##########################################
    print ("\nResults...");
    print ("Data points in input file : " + str(len(the_data)));
    print ("Dimensionality of data    : " + str(len(the_data[0])));
    print ("Value of k                : " + str(K));
    print ("Iterations to Converge    : " + str(iterations));
    print ("Total SSE Cost            : " + str(sum(cluster_error)));
    print ("Final Cluster Statistics  : ");
    for i in range(K):
        print (" - Cluster " + str(i));
        string = "";
        for val in centroids[i]:
            string += str(val) + " ";
        print (" -- Mean : " + string);
        print (" -- SSE  : " + str(cluster_error[i]));
        print (" -- Size : " + str(len(clusters[i])));
    print ("Final Cluster Assignments : ");
    print(assignments);


