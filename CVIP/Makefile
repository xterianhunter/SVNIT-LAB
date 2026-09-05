# Makefile for SVNIT CVIP Lab Assignments (Lab 1 & Lab 2)
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -O2
LDFLAGS = -lm

TARGET1 = lab1_analysis
TARGET2 = lab2_analysis

all: $(TARGET1) $(TARGET2)

$(TARGET1): lab1_analysis.c
	$(CC) $(CFLAGS) lab1_analysis.c $(LDFLAGS) -o $(TARGET1)

$(TARGET2): lab2_analysis.c
	$(CC) $(CFLAGS) lab2_analysis.c -o $(TARGET2)

lab1: $(TARGET1)
lab2: $(TARGET2)

run-lab1: $(TARGET1)
	./$(TARGET1) sample_01.pgm sample_02.pgm

run-lab2: $(TARGET2)
	./$(TARGET2) sample_01.pgm sample_01.ppm

run: run-lab1 run-lab2

clean:
	rm -f $(TARGET1) $(TARGET2) sample_01_brightened.pgm

.PHONY: all lab1 lab2 run-lab1 run-lab2 run clean
