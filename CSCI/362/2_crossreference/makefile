binary: dsBinarySearchTree.o cInputParser.o main.o
	g++ dsBinarySearchTree.o cInputParser.o main.o -o binary	
    
dsBinarySearchTree.o: dsBinarySearchTree.cpp dsBinarySearchTree.h
	g++ -c dsBinarySearchTree.cpp
    
cInputParser.o: cInputParser.cpp cInputParser.h
	g++ -c cInputParser.cpp
    
clean:
	rm -f *.o
	rm binary