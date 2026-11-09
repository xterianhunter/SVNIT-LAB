CC = mpicc
CFLAGS = -O2 -Wall
TARGET = tile_matmul
SRCS = tile_matmul.c

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS) -lm

clean:
	rm -f $(TARGET)

run: $(TARGET)
	mpirun -np 4 ./$(TARGET)

.PHONY: all clean run
