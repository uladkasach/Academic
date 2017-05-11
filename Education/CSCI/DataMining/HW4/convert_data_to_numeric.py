'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 convert_data_to_numeric.py
'''

#########################################
## Load Input Data
#########################################
DATA_SOURCE = "house-votes-84.data.txt";
print("Loading data from " + DATA_SOURCE + "...");    
full_data = [];
f = open(DATA_SOURCE, 'r');
for line in f.readlines():
    if(line.rstrip() == ""): continue;
    parts = line.rstrip().split(",");
    full_data.append(parts);
f.close();
#print(the_data);
#print(len(the_data));
##print("End loading data...");


#########################################
## Translate Data to Numeric
#########################################
dictionary = {
        "y" : "1",
        "?" : "0",
        "n" : "-1",
    };
converted_data = [];
for data_row in full_data:
    this_data = [];
    for element in data_row:
        if element in dictionary:
            element = dictionary[element]; # if key is found in dictionary replace it with that value
        this_data.append(element);
    converted_data.append(this_data);
#print(converted_data);


#########################################
## Save as new file
#########################################
destination_path = "numeric_house_votes.csv";
destination = open(destination_path, "w+");
for data_row in converted_data:
    this_string = ",".join(data_row);
    destination.write(this_string + "\n");
