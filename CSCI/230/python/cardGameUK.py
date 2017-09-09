""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
    
    Uladzimir Kasacheuski 6/12/15
"""
import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def clearDeck():
    global cardLoc;
    cardLoc = [0] * NUMCARDS;
    
    
def assignCard(who):
    global cardLoc;
    done = 0;
    while(done == 0):
        ran = random.randint(0, 51);
        #print ran;
        if(cardLoc[ran] == 0):
            done = 1;
            cardLoc[ran] = who;
            #print "Given to " + str(who);
            
def cardDetails(index):
    return rankName[index%13] + " of " + suitName[index/13]
            
def showDeck():
    print "\nLocation of all cards";
    total = len(cardLoc);
    #count = 0;
    #print total;
    #while(count < total):
    for count in range(total):
        print str(count) + "     " + cardDetails(count) + "     " + playerName[cardLoc[count]];
        #count += 1;  
        
def showHand(who):
    print "\nPlayer " + playerName[who] + " hand:";
    total = len(cardLoc);
    count = 0;
    while(count < total):
        if(cardLoc[count] == who):
            print cardDetails(count);
        count += 1;
def main():
  clearDeck();

  for i in range(5):
    assignCard(PLAYER);
    assignCard(COMP);

  showDeck()
  showHand(PLAYER)
  showHand(COMP)  

main();
print "";
#print cardLoc;

#index = 20;
#print suitName[index/13];