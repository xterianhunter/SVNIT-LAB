CC = gcc
CFLAGS = -fopenmp -O2 -Wall
TARGETS = race_condition critical_section matrix_mult

all: $(TARGETS)

race_condition: race_condition.c
	$(CC) $(CFLAGS) -o $@ $<

critical_section: critical_section.c
	$(CC) $(CFLAGS) -o $@ $<

matrix_mult: matrix_mult.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(TARGETS)

.PHONY: all clean
