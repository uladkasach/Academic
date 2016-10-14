crittercar: critter.o car.o main.o
	g++ critter.o car.o main.o -o crittercar
critter.o: critter.cpp critter.h
	g++ -c critter.cpp
car.o: car.cpp car.h critter.h
	g++ -c car.cpp
main.o: main.cpp car.h critter.h
	g++ -c main.cpp
clean:
	rm -f *.o
	rm crittercar