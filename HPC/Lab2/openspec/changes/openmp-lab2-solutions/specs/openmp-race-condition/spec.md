## Purpose

Demonstrates race conditions in multi-threaded OpenMP programs and provides synchronized critical section solutions.

## ADDED Requirements

### Requirement: Demonstrate Unsynchronized Race Condition
The program SHALL execute multiple OpenMP threads incrementing a shared counter without synchronization and display the resulting incorrect count and expected count.

#### Scenario: Running unsynchronized race condition executable
- **WHEN** the executable is run with multiple OpenMP threads
- **THEN** it outputs the number of threads, the expected counter value, and an actual counter value that exhibits data loss due to concurrent write collisions

### Requirement: Correct Shared Counter Using Critical Section
The program SHALL protect concurrent access to a shared counter across multiple OpenMP threads using `#pragma omp critical` and verify correctness against the expected value.

#### Scenario: Running critical section executable
- **WHEN** the executable is run with multiple OpenMP threads
- **THEN** it outputs the final counter value which strictly equals the expected value with zero lost updates
