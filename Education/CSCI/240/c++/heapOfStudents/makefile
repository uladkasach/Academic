heapOfStudents: cStudent.o cAddr.o cDate.o main.o
	g++ cStudent.o cAddr.o cDate.o main.o -o heapOfStudents	
cStudent.o: cStudent.cpp cStudent.h cAddr.h cDate.h
	g++ -c cStudent.cpp
cAddr.o: cAddr.cpp cAddr.h
	g++ -c cAddr.cpp
cDate.o: cDate.cpp cDate.h
	g++ -c cDate.cpp
main.o: main.cpp cStudent.h 
	g++ -c main.cpp
clean:
	rm -f *.o
	rm heapOfStudents