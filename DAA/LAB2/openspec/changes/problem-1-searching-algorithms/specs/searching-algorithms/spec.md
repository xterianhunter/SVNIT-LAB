## Purpose

Provides linear and binary search algorithms, file-based input processing, automated positional benchmarking, and tabular and visual empirical performance reporting for algorithm analysis.

## ADDED Requirements

### Requirement: Linear Search Execution
The system SHALL implement a sequential Linear Search algorithm that examines each element of an array iteratively from start to finish without using built-in search functions.

#### Scenario: Element found at beginning, middle, or end
- **WHEN** Linear Search is executed on an array containing the target element
- **THEN** the algorithm returns the zero-based index of the target element and records total comparisons

#### Scenario: Element absent
- **WHEN** Linear Search is executed on an array not containing the target element
- **THEN** the algorithm returns `-1` (or indicates absence) after checking all elements

### Requirement: Binary Search Execution
The system SHALL implement a Binary Search algorithm that repeatedly divides a sorted array search interval in half without using built-in search functions.

#### Scenario: Element found in sorted array
- **WHEN** Binary Search is executed on a sorted array containing the target element
- **THEN** the algorithm returns the zero-based index of the target element in $O(\log n)$ comparisons

#### Scenario: Element absent in sorted array
- **WHEN** Binary Search is executed on a sorted array not containing the target element
- **THEN** the algorithm returns `-1` after the search interval becomes empty

### Requirement: File-Based Input Processing
The system SHALL support reading integer arrays from input files for standard sizes (10, 50, 100, 200) and generate formatted dataset files if they do not exist.

#### Scenario: Load dataset from file
- **WHEN** the benchmark engine loads input for a specified size $N \in \{10, 50, 100, 200\}$
- **THEN** the dataset is read from disk into an integer array and sorted for binary search suitability

### Requirement: Multi-Case Benchmarking Suite
The system SHALL benchmark execution times for both Linear Search and Binary Search across four distinct positional test cases: element near beginning, element near middle, element near end, and element absent.

#### Scenario: Benchmark execution timing
- **WHEN** the benchmark suite runs across all input sizes and test cases
- **THEN** execution times are measured using high-precision timers (`time.perf_counter_ns`) averaged over multiple iterations to ensure statistical reliability

### Requirement: Tabular Results and Visualization Export
The system SHALL format experimental results in a structured comparison table and generate plots of Input Size vs Execution Time comparing empirical behavior with theoretical complexity.

#### Scenario: Generate report and plots
- **WHEN** benchmarking completes
- **THEN** the system prints a formatted comparison table and generates plot artifacts (SVG/HTML and terminal visualization) alongside theoretical complexity commentary
