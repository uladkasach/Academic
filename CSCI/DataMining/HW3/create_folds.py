import sys;
import numpy as np;

DATA_SOURCE = "iris.txt.shuffled";
FOLDS = 3;

print("Loading data from " + DATA_SOURCE + " and sorting it into folds...");    
#########################################
## Load Input Data
#########################################
the_data = [];
the_labels = [];
f = open(DATA_SOURCE, 'r');
lines = f.readlines();
items_per_fold = int(len(lines) / FOLDS);

## create files in which folds will be held
files = [];
for i in range(FOLDS):
    files.append(dict({"test" : open("folds/" + DATA_SOURCE+".fold_"+str(i)+"_test", "w+"), "train" : open("folds/" + DATA_SOURCE+".fold_"+str(i)+"_train", "w+")}));
for line_index, line in enumerate(lines):
    if(line.rstrip() == ""): continue;
    for file_index, a_file in enumerate(files):
        ## first 50 go in test of fold_1 if items per fold is 50, else go in train
        #print("new-----");
        #print("f_i : ", file_index);
        #print("l_i : ", line_index);
        #print("l_i = ", line_index, " -> ", np.floor(line_index / items_per_fold) );
        #line = str(line_index);
        test_class = int(np.floor(line_index / items_per_fold));
        #print("test_class : ", test_class);
        if(test_class == file_index):
            a_file["test"].write(line);
        else:
            a_file["train"].write(line);
        
f.close();
#print(the_data);
#print(len(the_data));
##print("End loading data...");
print("End.");