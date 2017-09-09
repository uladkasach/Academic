#Uladzimir Kasacheuski
#6/5/15
import random




#while(found != 1):
print "\n\nPlease think of a number between one and one hundred. \nI'll guess your number. \nYou tell me if I'm too high, too low, or correct.\n\n";

maxVal = 100;
minVal = 1;
counter = 1;
stat = "";
understood = 1;

while(stat != "c"):
    if(understood == 1):
        guess = random.randint(minVal, maxVal);
    understood = 1;
    print "I Guess: " + str(guess);
    stat = raw_input("Too (h)igh? Too (l)ow? (c)orrect? \n");
    print "\n"
    if(stat == "h"):
        maxVal = guess-1;
    elif(stat == "l"):
        minVal = guess+1;
    elif(stat == "c"):
        print "I got it! It took " + str(counter) + " turns.";
    else:
        print "I didn't understand that... \nTry again. h, l, or c";
        understood = 0;
  
    if(understood == 1):
        counter = counter + 1;
    #print "min = " + str(minVal) + "& high = " + str(maxVal); 
    
    

    
    
    
    
    