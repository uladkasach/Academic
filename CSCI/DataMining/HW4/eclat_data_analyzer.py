'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 eclat_data_analyzer.py
'''
import pandas as pd;


ITEMSET_SOURCE = "eclat_set_results.txt";
RULE_SOURCE = "eclat_rule_results.txt";

#########################################
## Helper Functions
#########################################
def get_stats(line):
    line = line.rstrip();
    relevant = (line.split("("))[1];
    relevant = (relevant.split(")"))[0];
    relevant = relevant.split(",");
    support = float(relevant[0]);
    confidence = None;
    if(len(relevant) > 1):
        confidence = float(relevant[1]);
    return support, confidence;
def get_items(line):
    line = line.rstrip();
    relevant = (line.split("("))[0];
    rule = relevant;
    relevant = relevant.split(" <- ");
    if(len(relevant) > 1):
        head = relevant[0];
        relevant = relevant[1];
    else:
        head = None;
        relevant = relevant[0];
    relevant = relevant.split(" ");
    body = [];
    full_items = [];
    for i in relevant:
        if(i != ""): body.append(float(i));
        if(i != ""): full_items.append(float(i));
    if(head is not None): full_items.append(int(head));
    return head, body, full_items, rule;

#########################################
## Load Input Data
#########################################
def load_data(data_source):
    f = open(data_source, 'r');
    lines = f.readlines();
    #random.shuffle(lines); ## shuffle lines
    return lines;
def parse_data_into_frame(data):
    df = pd.DataFrame()
    for index, line in enumerate(data):
        support, confidence = get_stats(line);
        head, body, items, rule = get_items(line);
        contains_100 = 100 in items;
        contains_200 = 200 in items;
        df = df.append({
             #"orig_index": index,
             #"items": items,
             "rule" : rule,
             "100" : contains_100,
             "200" : contains_200,
             "head" : head,
             "body" : body,
             "support":  support,
             "confidence": confidence,
            }, ignore_index=True);
    return df;
rule_data = parse_data_into_frame(load_data(RULE_SOURCE));
itemset_data = parse_data_into_frame(load_data(ITEMSET_SOURCE));
    

#########################################
## Find top 10 support from data
#########################################
if(False):
    itemset_data = itemset_data.sort(['support'], ascending=[0]);
    df.index = range(0,len(df))
    print(df['line']);
    
##########################################
## Find # containing 100 and 200
##########################################
if(False):
    print(itemset_data);
    sum_row=itemset_data[["100"]].sum()
    print(sum_row);
    sum_row=itemset_data[["200"]].sum()
    print(sum_row);

    
##########################################
## Write top 10 rules for 100 and 200, order confidence decreasing
##########################################
if(False):
    head_100 = rule_data.loc[rule_data['head'] == "100"];
    head_100 = head_100.sort(['confidence'], ascending=[0]);
    head_100.index = range(0,len(head_100))
    print(head_100);

    over_75 = head_100.loc[head_100['confidence'] > 0.75];
    sum_row=over_75[["100"]].sum()
    print(over_75);



head_200 = rule_data.loc[rule_data['head'] == "200"];
head_200 = head_200.sort(['confidence'], ascending=[0]);
head_200.index = range(0,len(head_200))
print(head_200);

over_75 = head_200.loc[head_200['confidence'] > 0.75];
sum_row=over_75[["200"]].sum()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(over_75)
print(sum_row);


################################################
## Record Confident rules for 100 and 200
################################################
dest = open("eclat_confident_rules.txt", "w+");
for index, row in rule_data.iterrows():
    if(row["head"] == "100" or row["head"] == "200"):
        dest.write(",".join([str(i) for i in row["body"]]) + "\n");


