## Purpose

Provides sequential and OpenMP-accelerated sorting algorithms (Merge Sort with sections and Quick Sort with tasks and depth cutoffs) alongside a benchmarking harness for performance evaluation on large datasets.

## ADDED Requirements

### Requirement: Sequential Sorting Algorithms
The system SHALL provide standard sequential implementations of Merge Sort and Quick Sort to establish baseline execution performance.

#### Scenario: Sequential Merge Sort correctness
- **WHEN** an unsorted array of integers is passed to sequential Merge Sort
- **THEN** the array is sorted in non-decreasing order and matches the expected sorted sequence.

#### Scenario: Sequential Quick Sort correctness
- **WHEN** an unsorted array of integers is passed to sequential Quick Sort
- **THEN** the array is sorted in non-decreasing order and matches the expected sorted sequence.

### Requirement: Parallel Merge Sort using OpenMP Sections
The system SHALL provide a parallel Merge Sort implementation using OpenMP `#pragma omp parallel sections` and `#pragma omp section` constructs to divide array halves across available threads.

#### Scenario: Parallel Merge Sort execution and correctness
- **WHEN** an unsorted array of integers is processed with the OpenMP section-based Merge Sort
- **THEN** sorting subproblems are executed concurrently in separate OpenMP sections and the final array is verified to be correctly sorted.

### Requirement: Parallel Quick Sort using OpenMP Tasks
The system SHALL provide a parallel Quick Sort implementation using OpenMP `#pragma omp task` directives to asynchronously process recursive partitions.

#### Scenario: Parallel Quick Sort task execution
- **WHEN** an unsorted array of integers is processed with OpenMP task-based Quick Sort
- **THEN** left and right subarray partitions are spawned as OpenMP tasks synchronized with `#pragma omp taskwait`, producing a correctly sorted array.

### Requirement: Depth-Limited Hybrid Quick Sort with Insertion Sort Cutoff
The system SHALL provide a hybrid parallel Quick Sort that tracks recursion depth (e.g., depth cutoff 4 or 8) and transitions to sequential Insertion Sort when either the depth limit is reached or the partition size drops below a sequential threshold.

#### Scenario: Switching to insertion sort below cutoff
- **WHEN** a recursive partition reaches the maximum depth limit or size threshold
- **THEN** further task generation is halted and the partition is sorted sequentially via insertion sort, yielding a correctly sorted array with reduced task overhead.

### Requirement: Benchmarking and Comparison Reporting
The system SHALL provide an automated benchmarking harness that executes all sorting variants on identical large integer arrays, measures execution time using `omp_get_wtime()`, validates correctness, and prints a comparative performance table.

#### Scenario: Performance comparison table generation
- **WHEN** the benchmark program is executed on an input size array (e.g. 100,000 to 1,000,000+ elements)
- **THEN** the program validates each algorithm's sort output, records wall-clock execution time, and outputs a formatted table showing algorithm name, array size, thread count, execution time, and speedup relative to sequential baselines.
