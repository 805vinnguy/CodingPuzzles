CC=gcc

CXX=g++

CFLAGS=-Wall -g

CPPFLAGS=-Wall -g

SRCS=Solution.cpp

OBJS=$(subst .cc,.o,$(SRCS))

BIN=solution

all: $(BIN)

solution: $(OBJS)
	$(CXX) $(CPPFLAGS) -o $(BIN) $(OBJS)

solution.o: $(SRCS)

clean:
	rm -f *.o

distclean:
	rm -f $(BIN)