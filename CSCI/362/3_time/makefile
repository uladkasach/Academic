binary:  sMergeSort.o sHeapSort.o sQuickSort.o sInsertionSort.o fundementals.o cInputGenerator.o cInputLoader.o main.o
	g++  sMergeSort.o sHeapSort.o sQuickSort.o sInsertionSort.o fundementals.o cInputGenerator.o cInputLoader.o  main.o -o binary	
    
fundementals.o: fundementals.h fundementals.cpp 
	g++ -c fundementals.cpp
    
cInputGenerator.o: fundementals.o cInputGenerator.h cInputGenerator.cpp 
	g++ -c cInputGenerator.cpp
    
cInputLoader.o: fundementals.o cInputLoader.h cInputLoader.cpp 
	g++ -c cInputLoader.cpp
    
sInsertionSort.o: fundementals.o sInsertionSort.h sInsertionSort.cpp 
	g++ -c sInsertionSort.cpp
    
sQuickSort.o: fundementals.o sQuickSort.h sQuickSort.cpp 
	g++ -c sQuickSort.cpp
    
sHeapSort.o: fundementals.o sHeapSort.h sHeapSort.cpp 
	g++ -c sHeapSort.cpp
    
sMergeSort.o: fundementals.o sMergeSort.h sMergeSort.cpp 
	g++ -c sMergeSort.cpp
    
clean:
	rm -f *.o
	rm binary