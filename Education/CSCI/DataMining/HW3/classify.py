import sys
import numpy
import math

'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW3/; 
python3 model.py iris.txt.shuffled
'''

def classify_this_point(a_data, priors, means, covariances):
    # P(c_i | x) = f_i(x | means[i], covariances[i]) * prior
    classes = list(priors.keys());
    dimensions = len(a_data);
    max_class = "";
    max_posterior = 0;
    for this_class in classes:
        #print("class : ", this_class);
        #print("a_data : ", a_data);
        means_difference_i = (a_data - means[this_class]);
        covar_inverse_i = numpy.linalg.inv(covariances[this_class]);
        #print(covariances[this_class]);
        #print("means_difference_i : ", means_difference_i); 
        #print("covar_inverse_i : \n", covar_inverse_i);
        exponent_i = numpy.dot(covar_inverse_i, means_difference_i);
        exponent_i = numpy.dot(means_difference_i, exponent_i);
        exponent_i = exponent_i / -2;
        #print("exponent_i : ", exponent_i);
        base_i = ((2*math.pi)**(dimensions/2)) * (numpy.linalg.det(covariances[this_class])**(1/2));
        base_i = base_i**-1;
        #print("det : ", numpy.linalg.det(covariances[this_class]));
        #print("sqrt det : ", (numpy.linalg.det(covariances[this_class])**(1/2)));
        #print("other part : ", ((2*math.pi)**(dimensions/2)));
        #print("base_i : ", base_i);
        f_i = base_i * math.e**(exponent_i); 
        #print("f_1 : ", f_i);
        #print("prior : ", priors[this_class]);
        posterior = priors[this_class] * f_i;
        #print("posterior : ", posterior);
        if(posterior > max_posterior):
            max_class = this_class;
            max_posterior = posterior;
    #print("Max Class : ", max_class);
    return max_class;
    

if __name__ == "__main__":
    #########################################
    ## Read User Inputs
    #########################################
    TEST_DATA_SOURCE = sys.argv[1];
        
        
    ##########################################
    ## Load Model
    ##########################################
    all_data = {
        "priors" : dict(),
        "means" : dict(),
        "covariances" : dict(),
    }
    current_reading = None;
    f = open("model.txt", 'r');
    for line in f.readlines():
        parts = line.rstrip().split(":");
        if(parts[0] == "priors"):
            current_reading = "priors";
            continue;
        elif(parts[0] == "means"):
            current_reading = "means";
            continue;
        elif(parts[0] == "covariances"):
            current_reading = "covariances";
            continue;
                
        if(len(parts) < 2): continue; ## check if empty line
        #print(parts);
        label = parts[0];
        parts = parts[1].split(",");
        
        this_data_dict = all_data[current_reading];
        if label not in this_data_dict: 
            this_data_dict[label] = [];
        this_data_dict[label].append([float(i) for i in parts]);
        all_data[current_reading] = this_data_dict;
    f.close();
    #print(all_data);
    
    #######
    ## Clean the loaded data
    #######
    priors = all_data["priors"];
    for k,v in priors.items():
        priors[k] = (float(v[0][0]));
    #print(priors);
    means = all_data["means"];
    for k,v in means.items():
        data = (numpy.array([float(i) for i in v[0]]));
        means[k] = data;
    #print(means);
    covariances = all_data["covariances"];
    #print(covariances);
    for k,v in covariances.items():
        #print(v);
        covariances[k] = numpy.array(v); 
    #print(covariances);
    possible_classes = sorted(list(priors.keys()));
    
    ######
    ## Feedback
    ######
    print("Model Loaded:");
    #print("priors : ", priors);
    #print("means : ", means);
    print("priors : ");
    print(priors);
    print("means : ");
    print(means);
    print("covariances : ");
    for k,v in covariances.items():
        print(k);
        print(v);
    print("\n\n");
        
        
    print("Loading test data from " + TEST_DATA_SOURCE + "...");    
    #########################################
    ## Load Input Data
    #########################################
    the_data = [];
    the_labels = [];
    f = open(TEST_DATA_SOURCE, 'r');
    for line in f.readlines():
        if(line.rstrip() == ""): continue;
        parts = line.rstrip().split(",");
        this_data = numpy.array([float(i) for i in parts[:-1]]);
        this_word = parts[-1];
        #print(this_data);
        the_data.append(this_data);
        the_labels.append(this_word);
        #print(this_word);
    f.close();
    the_data = numpy.array(the_data);
    #print(the_data);
    #print(len(the_data));
    print("Done...");
    print("\n\n");
    
    
    ##########################################
    ## For each data point, classify it
    ##########################################
    actual_hold_predictions = dict();
    for index in range(len(the_data)):
        a_data = the_data[index];
        a_class = the_labels[index];
        prediction = classify_this_point(a_data, priors, means, covariances);
        if(a_class not in actual_hold_predictions):
            #actual_hold_predictions[a_class] = dict({k: 0 for k in possible_classes});
            actual_hold_predictions[a_class] = dict();
            for k in possible_classes:
                actual_hold_predictions[a_class][k] = 0; 
        if(prediction not in actual_hold_predictions[a_class]):
            actual_hold_predictions[a_class][prediction] = 0;
        actual_hold_predictions[a_class][prediction] += 1;
        
    print(actual_hold_predictions);
    
    
    ###########################################
    ## Print Confusion Matrix
    ###########################################
    print(possible_classes);
    print("\n\n");
    print("{0:8s}".format("actu.") +  " \ " + "{0:8s}".format("pred.") + " | " + " | ".join(["{0:20s}".format(class_name) for class_name in possible_classes]));
    for actual_class in possible_classes:
        string = ("{0:19s}".format(actual_class));
        actual_predicted = actual_hold_predictions[actual_class];
        for predicted_class in possible_classes:
            predicted_value = actual_predicted[predicted_class];
            string += " | " + "{0:20d}".format(predicted_value);
        print(string);
    print("\n\n");
    
    