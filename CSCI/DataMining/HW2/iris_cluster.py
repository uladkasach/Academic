import mykMeans
import numpy

#########################################
## Read User Inputs
#########################################
DATA_SOURCE = 'iris.txt';
initial_centroid_indicies = None;
K = 3;

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

TEST = False;
if(TEST == True):
    from sklearn import datasets;
    import matplotlib.pyplot as plt;
    Xi, yi = datasets.make_blobs(500, random_state=1111)
    print(yi[0:10]);
    Xi = Xi.astype(numpy.float32)
    the_data = Xi;

print("Running K-Means...");
iterations, centroids, cluster_error, clusters, assignments = mykMeans.k_means_algorithm(K, the_data, initial_centroid_indicies = initial_centroid_indicies);
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


############################################
## Calculate Purity
############################################
######
## Generate true assignments
######
true_assignments = [];
for i in range(len(the_data)):
    if(i < 50):
        true_assignments.append("a");
    elif(i < 100):
        true_assignments.append("b");
    else:
        true_assignments.append("c");
#print(true_assignments);
######
## Generate Clusters based on index
######
clusters = [[],[],[]];
for index, cluster_index in enumerate(assignments):
    clusters[cluster_index].append(index);
#print (clusters);
######
## For each cluster, find the maximum number of elements of any partion in each cluster
######
max_in_cluster = [];
individual_purities = [];
for this_cluster in clusters:
    ##print(" Running cluster.... ");
    partition_contents = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        };
    for element in this_cluster:
        ##print(element);
        this_partition = true_assignments[element];
        #print("for index "+ str(element) +" found partition to be " + this_partition);
        partition_contents[this_partition] += 1;
    ##print(" Total partition contents found... ");
    ##print(partition_contents);
    max_value = 0;
    max_partition = None;
    for key, value in partition_contents.iteritems():
        if(value > max_value):
            max_value = value;
            max_partition = key;
    ##print('Max partition = ' + max_partition);
    max_in_cluster.append(max_value);
    this_purity = max_value/float(len(this_cluster));
    individual_purities.append(this_purity);
    
    
print("Max Partition Quantity in Each Cluster:");
print(max_in_cluster);
purity = sum(max_in_cluster)/float(len(the_data));
print("Purity = " + str(float(purity)));

total_purity = 0;
for index, purity_part in enumerate(individual_purities):
    total_purity += purity_part * len(clusters[index]);
total_purity = total_purity / float(len(the_data));

print("Purity = " + str(total_purity));

