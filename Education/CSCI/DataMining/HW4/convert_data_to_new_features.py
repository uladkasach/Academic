'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 convert_data_to_new_features.py
'''

#########################################
## Load Input Data
#########################################
DATA_SOURCE = "data/itemset_house_votes.csv";
print("Loading data from " + DATA_SOURCE + "...");    
full_data = [];
f = open(DATA_SOURCE, 'r');
for line in f.readlines():
    if(line.rstrip() == ""): continue;
    parts = line.rstrip().split(",");
    full_data.append(parts);
f.close();
#print(full_data);
#print(len(the_data));
##print("End loading data...");


#########################################
## Load Features
#########################################
DATA_SOURCE = "eclat_confident_rules.txt";
print("Loading data from " + DATA_SOURCE + "...");    
features_data = [];
f = open(DATA_SOURCE, 'r');
for line in f.readlines():
    if(line.rstrip() == ""): continue;
    parts = line.rstrip().split(",");
    new_parts = [(str(int(float(part)))) for part in parts];
        
    features_data.append(new_parts);
f.close();
#print(the_data);
#print(len(the_data));
##print("End loading data...");


#########################################
## For each row, build binary list of whether it has that feature or not
#########################################
converted_data = [];
for row in full_data:
    converted_row = [];
    head = row[-1];
    if(head == "100"): head = "republican";
    if(head == "200"): head = "democrat";
    converted_row.append(head); ## append label
    for feature in features_data:
        if (set(feature).issubset(row)): 
            converted_row.append("1");
        else:
            converted_row.append("0");
    converted_data.append(converted_row);
            

#########################################
## Save as new file
#########################################
destination_path = "data/item_feature_house_votes.csv";
destination = open(destination_path, "w+");
for data_row in converted_data:
    this_string = ",".join(data_row);
    destination.write(this_string + "\n");
