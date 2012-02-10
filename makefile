# you may need t ochange the paths below...
GOCC=/opt/go/bin/8g
GOLINK=/opt/go/bin/8l
GOFLAGS=

CPPCC=g++
CC=gcc
FLAGS=-c -g


all: euler02 euler03 euler04 euler05 euler07 euler08 euler09 euler10

euler02: euler02.8
	$(GOLINK) -o $@ $^

euler03: euler03.8
	$(GOLINK) -o $@ $^

euler04: euler04.o
	$(CPPCC) -o $@ $^

euler05: euler05.8
	$(GOLINK) -o $@ $^

euler07: euler07.8
	$(GOLINK) -o $@ $^

euler08: euler08.o
	$(CPPCC) -o $@ $^

euler09: euler09.8
	$(GOLINK) -o $@ $^

euler10: euler10.8
	$(GOLINK) -o $@ $^

euler12: euler12.8
	$(GOLINK) -o $@ $^

euler14: euler14.8
	$(GOLINK) -o $@ $^

%.o: %.c
	$(CC) $(FLAGS) $+ -I.

%.o: %.cpp
	$(CPPCC) $(FLAGS) $+ -I.

%.8: %.go
	$(GOCC) $+

.PHONY:
	clean

clean:
	rm -f *.8 *.o euler0[0-9] euler[0-9][0-9]
