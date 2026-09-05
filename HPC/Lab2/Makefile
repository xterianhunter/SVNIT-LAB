CC ?= gcc
CFLAGS ?= -fopenmp -O3 -Wall -Wextra -std=c11
LDFLAGS ?= -fopenmp -lm

TARGET = linear_regression
SRC = linear_regression.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all run clean
