#Uladzimir Kasacheuski
#6/5/15
import random


#maxVal = 100;
#minVal = 1;


#while(found != 1):
print "I'm thinking of a number between 1 and 100. \nGuess a number and i'll tell you if you're too high, too low, or if you've got it right. \nGood Luck!";

number = random.randint(1, 100);
counter = 1;
guess = 999;

while(number != guess):
    guess = raw_input(str(counter) + ") Please Enter a Number\n - ");
    counter += 1;
    guess = int(guess);
    if(guess == number):
        print "Correct! \nIt took " + str(counter) + " turns.";
    elif(guess > 100):
        print "Number is less that 101!";
    elif(guess < 1): 
        print "Number is greater than 0!";
    elif(guess < number):
        print "Too Low!";
    elif(guess > number):
        print "Too High!";
    
        
        
    
    

    

    
    
    
    
    