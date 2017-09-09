'''
cd /var/www/git/Academic/Education/CSCI/DataMining/HW4; python3 convert_data_again.py
'''

dest = open("data/itemset_house_votes.csv", "w+");
f = open("data/house-votes-84.data.txt", "r");
lines = f.readlines()
for line in lines:
    strpline = line.rstrip()
    arr = strpline.split(",")
    newline = [];
    for i in range(len(arr)):
        if arr[i] == "y":
            newline.append(i)
    if arr[0] == "republican":
        newline.append(100)
    else:
        newline.append(200)
    print(*newline, sep=",");
    dest.write(",".join([str(i) for i in newline]) + "\n");