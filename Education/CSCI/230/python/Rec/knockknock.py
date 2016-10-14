
name = raw_input("\n\nHowdy! \nWhat's your name, friend? \n-");
import time;

def print_nnl(string):
    import sys;
    sys.stdout.write(string);
    sys.stdout.flush();

def naturalWait():
    time.sleep(0.3);
    print_nnl(".");
    time.sleep(0.35);
    print_nnl(".");
    time.sleep(0.4);
    print ".";
    time.sleep(0.8);

jokeName = "Not Set";
jokeLine = "Not Set again";

def setName(int):
    global jokeName;
    global jokeLine
    if(int == 1):
        jokeName = "Wooden shoe";
        jokeLine = "Wooden shoe like to know...";
        return jokeName;
    elif(int == 2):
        jokeName = "Honey bee";
        jokeLine = "Honey, bee a dear and get me a beer.";
        return jokeName;

print_nnl("Thats a great name, " + name );
naturalWait();

print_nnl( "Heres a Knock Knock Joke for ya");
naturalWait();

knocker = raw_input("Knock Knock \n-");
naturalWait();

if not (knocker == "Who's there?") and not (knocker == "who's there?") and not (knocker == "who's there") and not (knocker == "Who's there"):
    print_nnl("Sorry. I couldn't understand that, " + name);
    naturalWait();
    responce = raw_input('Did you mean "Who\'s there?" (Yes/No)\n-');
    naturalWait();
    if not (responce == "Yes") and not (responce == "yes"):
        print "In that case, I don't know that one yet. Come back later and see if I've learned it.";
        quit();
    else:
        print_nnl("Great!");
        naturalWait();
        knocker = raw_input("It's " + setName(1)+"\n-");
        naturalWait();
else:
    knocker = raw_input(setName(2)+"\n-");
    naturalWait();
        
if not (knocker == jokeName +" who?") and not (knocker == jokeName +" who"):
    print_nnl("Hmmm ");
    naturalWait();
    responce = raw_input('Did you mean "' + jokeName +' who?" (Yes/No)\n-');
    naturalWait();
    if not (responce == "Yes") and not (responce == "yes"):
        print "Well i'm gonna pretend you said yes anyway! Muahaha!";
        naturalWait();
        print "Wooden show who?...";
    else:
        print_nnl("Great!");
        naturalWait();

print "\n" + jokeLine;        
print "\n    Ha!";            
print "\n\n\n";  
        