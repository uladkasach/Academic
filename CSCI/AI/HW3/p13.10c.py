from random import randint;
import numpy;

def pull_lever():
    possible_results = ["bar", "bell", "lemon", "cherry"];
    possible_winners = {"bar-bar-bar" : 20, "bell-bell-bell" : 15, "lemon-lemon-lemon" : 5, "cherry-cherry-cherry" : 3, "cherry-cherry-?" : 2, "cherry-?-?" : 1};
    results = [];
    for i in range(3):
        this_choice = possible_results[randint(0,len(possible_results) - 1)];
        results.append(this_choice);
    final_result = "-".join(results);
    
    ## Accomodate wild ?'s
    results[2] = "?";
    final_result_last_q = "-".join(results);
    results[1] = "?";
    final_result_last_2_q = "-".join(results);
    
    if(final_result in possible_winners):
        winnings = possible_winners[final_result];
    elif(final_result_last_q in possible_winners):
        winnings = possible_winners[final_result_last_q];
    elif(final_result_last_2_q in possible_winners):
        winnings = possible_winners[final_result_last_2_q];
    else:
        winnings = 0;
    
    
    #print("{:20s}".format(final_result), "->", winnings);
    return winnings;
        

def sample_plays_possible():
    coins = 10;
    counter = 0;
    while coins > 0:
        coins -= 1;
        counter += 1;
        winnings = pull_lever();
        coins += winnings;
        #print(counter, ":", winnings, "->", coins);
    return counter;


total_samples = 100000;
samples = [];
for i in range(total_samples):
    plays = sample_plays_possible();
    samples.append(plays);
    #print(plays);
    if(i % 500 == 0):
        print("At sample ", i);
mean = numpy.mean(samples);
variance = numpy.var(samples);
median = numpy.median(samples);

print("Mean : ", mean);
print("Median : ", median);
print("Variance : ", variance);