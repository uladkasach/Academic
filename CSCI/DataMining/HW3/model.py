import sys
import numpy

'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW3/; 
python3 model.py iris.txt.shuffled
'''

def calculate_priors_on(the_labels):
    freq = dict();
    total = 0;
    for a_label in the_labels:
        #print(a_label);
        if a_label in freq:
            freq[a_label] += 1;
        else:
            freq[a_label] = 1;
        total += 1;
    #print(freq);
    #print(total);
    #freq = {k: v/total for k, v in freq.items()}
    prior = dict();
    for k, v in freq.items():
        prior[k] = v/float(total);
        
    #print(prior);
    return prior;
    
    
def calculate_means_on(the_labels, the_data):
    freq = dict();
    sums = dict();
    means = dict();
    total = 0;
    for index, a_label in enumerate(the_labels):
        this_data = the_data[index];
        #print(a_label);
        if a_label not in freq:
            freq[a_label] = 1;
            sums[a_label] = numpy.copy(this_data);
        else:
            freq[a_label] += 1;
            sums[a_label] = sums[a_label] + this_data;
        total += 1;
    #print(freq);
    for k, v in freq.items():
        #print("k:", k);
        #print("v:", v);
        this_sum = sums[k];
        #print("sum:", this_sum);
        #print("->",this_sum/v);
        means[k] = this_sum/v;
    #print(means);
    return means;


def calculate_covariance_on(the_labels, the_data, naive = False):
    #print(the_data);
    seperated_data = dict();
    covariances = dict();
    for index, a_label in enumerate(the_labels):
        this_data = the_data[index];
        if a_label not in seperated_data:
            seperated_data[a_label] = [];
        seperated_data[a_label].append(this_data);
        #print("appending ", this_data, " to ", a_label);
    #print(freq);
    #print(means);
    for k, v in seperated_data.items():
        print(len(v));
        this_data_set = numpy.array(v);
        #print(this_data_set);
        covariances[k] = numpy.cov(this_data_set, bias=True, rowvar=False);
        #print(covariances[k]);
        
    if(naive == True):
        dimensions = len(the_data[0]);
        #print(dimensions);
        identity = numpy.eye(dimensions, dtype=int);
        #covariances = {k: numpy.multiply(v, identity) for k, v in covariances.items()}
        new_covariances = dict();
        for k, v in covariances.items(): 
            new_covariances[k] = numpy.multiply(v, identity);
        #for k, v in covariances.items():
            #print(v);
        covariances = new_covariances;
    return covariances;
    

if __name__ == "__main__":
    #########################################
    ## Read User Inputs
    #########################################
    data_string = "";
    DATA_SOURCE = sys.argv[1];
    bool_naive = False;
    if(len(sys.argv) > 2):
        bool_naive = True if sys.argv[2] == "true" else False;
        
    print("Loading data from " + DATA_SOURCE + "...");    
    #########################################
    ## Load Input Data
    #########################################
    the_data = [];
    the_labels = [];
    f = open(DATA_SOURCE, 'r');
    for line in f.readlines():
        if(line.rstrip() == ""): continue;
        parts = line.rstrip().split(",");
        this_data = numpy.array([float(i) for i in parts[:-1]]);
        this_word = parts[-1];
        #print(this_data);
        ##print("Found data: ", this_data, " for label " , this_word);
        the_data.append(this_data);
        the_labels.append(this_word);
        #print(this_word);
        ##print("Now the data = ", the_data);
    f.close();
    the_data = numpy.array(the_data);
    #print(the_data);
    #print(len(the_data));
    ##print("End loading data...");
    
    
    ##########################################
    ## Calculate Priors
    ##########################################
    priors = calculate_priors_on(the_labels);
    print(priors);
    data_string += "priors:";
    data_string += "\n";
    for k,v in priors.items():
        data_string += k + ":" + "{0:.2f}".format(v);
        data_string += "\n";
    data_string += "\n";
    
    
    ##########################################
    ## Calculate Means
    ##########################################
    means = calculate_means_on(the_labels, the_data);
    print(means);
    data_string += "means:";
    data_string += "\n";
    for k,v in means.items():
        data_string += k + ":" + ",".join(["{0:.2f}".format(vi) for vi in v]);
        data_string += "\n";
    data_string += "\n";

    ##########################################
    ## Calculate Covariances
    ##########################################
    covariances = calculate_covariance_on(the_labels, the_data, bool_naive);
    #print(covariances);
    data_string += "covariances:";
    data_string += "\n";
    for k,cov in covariances.items():
        print(cov);
        for cov_row in cov:
            data_string += k + ":" + ",".join(["{0:.2f}".format(vi) for vi in cov_row]);
            data_string += "\n";
    data_string += "\n";

    
    ##########################################
    ## Output model.txt
    ##########################################
    myfile = open("model.txt", "w+");
    myfile.write(data_string);
    myfile.close();
    print("Model written.");