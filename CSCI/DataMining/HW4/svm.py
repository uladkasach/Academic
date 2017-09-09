'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 svm.py 
'''

from sklearn.svm import SVC
import pandas as pd;
import numpy as np;
import sys;
import os;


###############################################################################################
## USER INPUTS
###############################################################################################
##################
## Define Sources
##################
# Train and Test sources are defined in loop further in code
SOURCE_ROOT = "folds/house_votes.fold"; ## Beginning of source path for all data used
VALIDATION_SOURCE = SOURCE_ROOT + "_validation";
FOLD_SIZE = 3;

#########################################################
## Choose Kernel
#########################################################
acceptable_kernels = ['linear', 'RBF', 'rbf', 'poly', 'sigmoid'];
KERNEL = 'linear';

#######################
## Grid Search Parameters 
#######################
regularization_parameter_search_list = [1, 199, 0.01]; ## 0.5:0.01:1.5
#gamma_search_list = return_centered_search_list(2, 15, 0.1); ## 0.5:0.01:1.5
gamma_search_list = 1;
###############################################################################################
## Load Data
###############################################################################################
def load_data_set(data_source_path):
    print("Loading data from " + data_source_path + " ....");
    with open(data_source_path) as fp:
        source_lines = fp.readlines();
    
    the_labels = [];
    the_data = [];
    
    for index, line in enumerate(source_lines):
        parts = line.rstrip().split(",");
        this_label = parts[0];
        this_data = [int(j) for j in parts[1:]];

        the_labels.append(this_label);
        the_data.append(this_data);

    return the_labels, the_data;
##############################
print("Loading train and test data...");
validation_labels, validation_features = load_data_set(VALIDATION_SOURCE);
full_train_labels = [];
full_train_features = [];
full_test_labels = [];
full_test_features = [];
for fold_id in range(FOLD_SIZE):
    this_train_source = SOURCE_ROOT + "_" + str(fold_id) + "_train";
    this_test_source = SOURCE_ROOT + "_" + str(fold_id) + "_train";
    train_labels, train_features = load_data_set(this_train_source);
    test_labels, test_features = load_data_set(this_test_source);
    full_train_labels.append(train_labels);
    full_train_features.append(train_features);
    full_test_labels.append(test_labels);
    full_test_features.append(test_features);
    
###############################################################################################
## Train and Evaluate a Classifier
###############################################################################################
def train_classifier(arguments, labels, features):
    #print('Training Classifier...');
    classifier = SVC(**arguments);
    classifier.fit(features, labels)
    return classifier;
def generate_predictions(classifier, labels, features):
    #print("Generating predictions...");
    max_predictions = (classifier.predict(features));
    #print(predictions[0:50]);
    #print(labels[0:50]);
    #print(max_predictions[0:50]);

    classification_df = pd.DataFrame();
    classification_df["label"] = labels;
    classification_df["prediction"] = max_predictions;
    return classification_df;
def evaluate_predictions(classification_df):
    #print("Evaluating predictions...");
    total_size = 0;
    total_true = 0;
    for index, row in classification_df.iterrows():
        total_size += 1;
        if(row["label"] == row["prediction"]): total_true += 1;
    accuracy = total_true / total_size;
    return accuracy;
#####################################
def generate_classification_statistics(arguments, full_train_labels, full_train_features, full_test_labels, full_test_features, validation_labels, validation_features, test_validation = True):
    accuracies = [];
    for this_fold in range(FOLD_SIZE):
        #########
        ## Select Data Fold
        #########
        train_labels = full_train_labels[this_fold];
        train_features = full_train_features[this_fold];
        if(test_validation):
            test_labels =  validation_labels;
            test_features = validation_features;
        else:
            test_labels = full_test_labels[this_fold];
            test_features = full_test_features[this_fold];

        ########
        ## Classify, Predict, and Assess
        ########
        classifier = train_classifier(arguments, train_labels, train_features);
        predictions = generate_predictions(classifier, test_labels, test_features);
        accuracy = evaluate_predictions(predictions);
        #print(accuracy);
        accuracies.append(accuracy);
    accuracies = np.array(accuracies);
    mean_acc = np.mean(accuracies);
    std_acc = np.std(accuracies);
    return mean_acc, std_acc;
#####################################


###############################################################################################
## Run grid search
###############################################################################################
def return_centered_search_list(center, interval, interval_scale):
    search_modifier = np.array([i for i in range(interval + 1)]); ## Get integers 0:1:interval
    search_modifier = search_modifier - interval/2; ## Center the numbers at 0, equivilent to subtracting from the mean of the list
    search_modifier = search_modifier * interval_scale;
    search_list = [int((center + i)*1000000)/1000000 for i in search_modifier];
    return search_list;
#############################
regularization_parameter_search_list = return_centered_search_list(regularization_parameter_search_list[0], regularization_parameter_search_list[1], regularization_parameter_search_list[2]);
gamma_search_list = [1];
max_accuracy = 0;
max_set = [];
for regularization_parameter in regularization_parameter_search_list:
    for gamma in gamma_search_list:
        #print("C = ", regularization_parameter, " and gamma = ", gamma);
        #########
        ## Define Arguments
        #########
        classifier_arguments = dict();
        classifier_arguments["C"] = regularization_parameter;
        classifier_arguments["kernel"] = KERNEL;
        classifier_arguments["gamma"] = gamma;

        mean, std = generate_classification_statistics(classifier_arguments, full_train_labels, full_train_features, full_test_labels, full_test_features, validation_labels, validation_features);
        
        new_max_string = "";
        if(mean > max_accuracy):
            max_accuracy = mean;
            max_set = [regularization_parameter, gamma];
            new_max_string = "<--- max";
            
        print("mean : ", mean, ", std : ", std, new_max_string);
#############################################################
## Output Results
#############################################################
#max_set = [0.1, 1];
classifier_arguments = dict();
classifier_arguments["kernel"] = KERNEL;
classifier_arguments["C"] = max_set[0];
classifier_arguments["gamma"] = max_set[1];
mean, std = generate_classification_statistics(classifier_arguments, full_train_labels, full_train_features, full_test_labels, full_test_features, validation_labels, validation_features, test_validation = False);
print("Best scores at ");
print("C = ", max_set[0], " and gamma = ", max_set[1]);
print("mean : ", mean, ", std : ", std);

