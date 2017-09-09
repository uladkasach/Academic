'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 analyze_odds_ratio.py
'''
import pandas as pd;

#########################################
## Load Input Data
#########################################
DATA_SOURCE = "data/numeric_house_votes.csv";
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
## For each feature, calculate odds ratio for each feature
##      Odds ratio = P(class|true) / P(class|false) = P(c|t)/p(t) / P(c|f) / p(f) = P(c|t)*P(f) / P(c|f)*P(t)
#########################################
def calculate_odds_ratio_for(class_type, feature_id, full_data):
    true_count = 0;
    false_count = 0;
    class_and_feature_true_count = 0;
    class_and_feature_false_count = 0;
    for row in full_data:
        if(row[feature_id] == "1"): 
            true_count  += 1;
            if(row[0] == class_type): class_and_feature_true_count += 1;
        else:
            false_count  += 1;
            if(row[0] == class_type): class_and_feature_false_count += 1;
    ratio = class_and_feature_true_count * false_count / (class_and_feature_false_count * true_count);
    return ratio;
    
#########################################
df = pd.DataFrame();
class_type = "democrat";
for feature_id in range(1, len(full_data[0])):
    ratio = calculate_odds_ratio_for(class_type, feature_id, full_data);
    print(ratio);
    df = df.append({
            "odds" : ratio,
            "feature_id" : feature_id,
    }, ignore_index = True);

print(df);
df = df.sort(['odds'], ascending=[0]);
df.index = range(0,len(df))
print(df);