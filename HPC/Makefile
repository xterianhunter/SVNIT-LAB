CC ?= gcc
CFLAGS ?= -fopenmp -O3 -Wall -Wextra -std=c11
LDFLAGS ?= -fopenmp -lm

SRC_DIR = src
BIN_DIR = bin

TARGETS = $(BIN_DIR)/race_condition $(BIN_DIR)/critical_section $(BIN_DIR)/matrix_mult

.PHONY: all clean help

all: $(TARGETS)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

$(BIN_DIR)/race_condition: $(SRC_DIR)/race_condition.c $(SRC_DIR)/common.h | $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $(SRC_DIR)/race_condition.c $(LDFLAGS)

$(BIN_DIR)/critical_section: $(SRC_DIR)/critical_section.c $(SRC_DIR)/common.h | $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $(SRC_DIR)/critical_section.c $(LDFLAGS)

$(BIN_DIR)/matrix_mult: $(SRC_DIR)/matrix_mult.c $(SRC_DIR)/common.h | $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $(SRC_DIR)/matrix_mult.c $(LDFLAGS)

clean:
	rm -rf $(BIN_DIR)

help:
	@echo "OpenMP HPC Labs Build Targets:"
	@echo "  make all              - Build all executables (race_condition, critical_section, matrix_mult)"
	@echo "  make clean            - Remove compiled binaries"
	@echo "  make help             - Display this help message"
