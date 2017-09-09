binary: dsChessBoard.o dsStack.o dsLinkedList.o cKnight.o cUserInput.o main.o
	g++ dsChessBoard.o dsStack.o dsLinkedList.o cKnight.o cUserInput.o main.o -o binary	
    
dsLinkedList.o: dsLinkedList.cpp dsLinkedList.h
	g++ -c dsLinkedList.cpp
dsStack.o: dsLinkedList.o dsStack.cpp dsStack.h 
	g++ -c dsStack.cpp
dsChessBoard.o: dsChessBoard.cpp dsChessBoard.h
	g++ -c dsChessBoard.cpp
    
cUserInput.o: dsLinkedList.o cUserInput.cpp cUserInput.h 
	g++ -c cUserInput.cpp
cKnight.o: dsStack.o dsChessBoard.o cKnight.h cKnight.cpp 
	g++ -c cKnight.cpp
    
clean:
	rm -f *.o
	rm binary