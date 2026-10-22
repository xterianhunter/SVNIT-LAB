## Purpose

Provides implementations of Bubble Sort, Selection Sort, and Insertion Sort, along with automated benchmarking across random, sorted, and reverse-sorted datasets to analyze best-case and worst-case time complexities.

## ADDED Requirements

### Requirement: Bubble Sort Algorithm
The system SHALL implement an in-place Bubble Sort algorithm with an early-exit optimization flag that halts execution when no swaps occur during an entire pass.

#### Scenario: Sorting random array
- **WHEN** Bubble Sort is executed on an unsorted array
- **THEN** the array is sorted in non-decreasing order with $\mathcal{O}(n^2)$ average comparisons

#### Scenario: Sorting already sorted array
- **WHEN** Bubble Sort is executed on an already sorted array
- **THEN** the algorithm terminates after 1 pass in $\mathcal{O}(n)$ time

### Requirement: Selection Sort Algorithm
The system SHALL implement an in-place Selection Sort algorithm that repeatedly finds the minimum element from the unsorted sub-array and places it at the beginning.

#### Scenario: Sorting array across any input distribution
- **WHEN** Selection Sort is executed on random, sorted, or reverse-sorted input
- **THEN** the algorithm always executes exactly $\frac{n(n-1)}{2}$ comparisons ($\Theta(n^2)$ complexity)

### Requirement: Insertion Sort Algorithm
The system SHALL implement an in-place Insertion Sort algorithm that builds the sorted array one element at a time by shifting larger elements to the right.

#### Scenario: Sorting already sorted array
- **WHEN** Insertion Sort is executed on an already sorted array
- **THEN** the algorithm completes in linear time $\mathcal{O}(n)$ with $n-1$ comparisons

#### Scenario: Sorting reverse-sorted array
- **WHEN** Insertion Sort is executed on a reverse-sorted array
- **THEN** the algorithm executes $\mathcal{O}(n^2)$ comparisons and maximum element shifts

### Requirement: Multi-Distribution Benchmarking and Reporting
The system SHALL benchmark all three algorithms across multiple array sizes on Random, Already Sorted, and Reverse Sorted inputs, displaying formatted execution tables and complexity analysis.

#### Scenario: Benchmark execution and output
- **WHEN** the benchmark harness runs
- **THEN** execution times in microseconds/milliseconds and comparison counts are reported in a structured comparison table
