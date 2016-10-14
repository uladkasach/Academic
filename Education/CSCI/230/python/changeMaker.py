#Uladzimir Kasacheuski
#6/5/15

print ("Booting Change-Make-ah-Mah-Tron 9000\n\n\n");


#make sure user doesn't enter a negative number
change = -99;
while (change < 0) :
    price = raw_input("What is the total price? \n $");
    paid = raw_input("How much was Paid? \n $");
    price = float(price);
    paid = float(paid);
    change = paid - price;
    if(change < 0):
        print "They owe you more money... \nTry Again when you're ready.\n";

# Normalize the cents for when user does not define them or goes into sub penny values
changeBills = int(change // 1);
changeCents = change % 1;
changeCents = int(changeCents * 100);
        
    
changestr = str(changeBills) + "." + str(changeCents);      
print "Change : $" + changestr;
change = int(change*100);
print "Also known as " + str(change) + " Cents \n Please Tend :";

twenties = change // 2000;
print " - Twenties : " + str(twenties);
#change = change - 2000 * twenties;
change = change % 2000;

tens = change // 1000;
print " - Tens : " + str(tens);
#change = change - 1000 * tens;
change = change % 1000;

fives = change // 500;
print " - Fives : " + str(fives);
#change = change - 500 * fives;
change = change % 500;

ones = change // 100;
print " - Ones : " + str(ones);
#change = change - 100 * ones;
change = change % 100;

quarters = change // 25;
print " - Quarters : " + str(quarters);
#change = change - 25 * quarters;
change = change % 25;

dimes = change // 10;
print " - Dimes : " + str(dimes);
#change = change - 10 * dimes;
change = change % 10;

nickles = change // 5;
print " - Nickles : " + str(nickles);
#change = change - 5 * nickles;
change = change % 5;

pennies = change // 1;
print " - Pennies : " + str(pennies);
#change = change - 1 * pennies;

#print "Change Left : " + str(change);
print "All Done";

