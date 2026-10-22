## Purpose

Compares sequential quicksort against a depth-limited parallel quicksort using OpenMP sections, measuring and printing wall-clock time for both.

## ADDED Requirements

### Requirement: Sequential quicksort
The program SHALL sort an integer array using a standard recursive quicksort without any parallelism and report the wall-clock time taken.

#### Scenario: Sequential sort produces correct output
- **WHEN** the program is compiled and executed
- **THEN** the sequential quicksort sorts the array in ascending order and prints the elapsed time.

### Requirement: Parallel quicksort with depth-limited sections
The program SHALL sort an identical copy of the array using a recursive quicksort that employs `#pragma omp parallel sections` to recurse into left and right partitions concurrently. The parallel quicksort function MUST accept a `depth` parameter (4th argument) that is decremented on each recursive call; when `depth` reaches zero the function MUST fall back to sequential sorting.

#### Scenario: Parallel sort produces correct output with speedup
- **WHEN** the program is compiled with `-fopenmp` and executed with multiple threads
- **THEN** the parallel quicksort sorts the array in ascending order, prints the elapsed time, and the program prints both times for comparison.

### Requirement: Time comparison output
The program SHALL print the elapsed wall-clock time for both the sequential and parallel quicksort runs so the user can directly compare them.

#### Scenario: Both times are printed
- **WHEN** the program finishes execution
- **THEN** the stdout output contains clearly labelled sequential time and parallel time values.
