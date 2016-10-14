""" 
    crypto.py
    Implements a simple substitution cypher
    
    Uladzimir Kasacheuski
    6/12/15
    
    This script removes all characters that are not in the alpha string and keeps spaces.
    
    It also generates random keys.
    
    Thanks for your time.
"""

import random


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

#Generate Random Key
def ranKey():
    global key;
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    key = "";
    total = 26;
    count = 0;
    while(count < total):
        end = len(alpha2)-1;
        #print end;
        val = random.randint(0, end);
        #print val;
        char = alpha2[val];
        #print char;
        alpha2 = alpha2.replace(char, "");
        #print alpha;
        key += char;
        count += 1;
    


    
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = raw_input("text to be encoded: ")
      print encode(plain)
    elif response == "2":
      coded = raw_input("code to be decyphered: ")
      print decode(coded)
    elif response == "0":
      print "Thanks for doing secret spy stuff with me."
      keepGoing = False
    elif response == "3":
      ranKey();
      #print key;
      print "New key is set.";
    else:
      print "I don't know what you want to do..."

    
def menu():
    print "\nSECRET DECODER MENU \n\n  0) Quit\n  1) Encode\n  2) Decode\n  3) Create New Key \n";
    response = raw_input("What do you want to do? ");
    return response;

def encode(text):
    #return text;
    #return alpha[1];
    text = text.upper();
    total = len(text);
    newText = "";
    thecount = 0;
    while(thecount < total):
        char = text[thecount];
        #print char;
        if(char == " "):
            encodedChar = " ";
        else:
            pos = alpha.find(char);
            #print pos;
            if(pos == -1):
                encodedChar = "";
            else:
                encodedChar = key[pos];
        #print encodedChar;
        newText += encodedChar;
        thecount += 1;
    return newText;

def decode(text):
    #return text;
    #return alpha[1];
    text = text.upper();
    total = len(text);
    newText = "";
    thecount = 0;
    while(thecount < total):
        char = text[thecount];
        #print char;
        if(char == " "):
            encodedChar = " ";
        else:
            pos = key.find(char);
            #print pos;
            if(pos == -1):
                encodedChar = "";
            else:
                encodedChar = alpha[pos];
        #print encodedChar;
        newText += encodedChar;
        thecount += 1;
    return newText;
    
    
    
    
main();


    