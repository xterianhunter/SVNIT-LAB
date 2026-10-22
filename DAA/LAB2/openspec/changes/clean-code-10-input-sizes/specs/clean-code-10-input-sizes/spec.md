## Purpose

Expands the benchmarking evaluation dataset in `clean_code/` scripts to at least 10 distinct input sizes to clearly exhibit asymptotic scaling across searching, sorting, and matrix algorithms.

## ADDED Requirements

### Requirement: 10 Input Sizes for Problem 1 Searching
The system SHALL configure `clean_code/problem1_searching.py` to benchmark Linear Search and Binary Search across at least 10 distinct array sizes: `(10, 20, 50, 75, 100, 150, 200, 300, 400, 500)`.

#### Scenario: Running search benchmark on 10 input sizes
- **WHEN** `clean_code/problem1_searching.py` executes
- **THEN** it automatically generates/loads datasets for all 10 sizes, evaluates Beginning, Middle, End, and Absent positions, and tabulates all 80 benchmark records

### Requirement: 10 Input Sizes for Problem 2 Sorting
The system SHALL configure `clean_code/problem2_sorting.py` to benchmark Bubble Sort, Selection Sort, and Insertion Sort across at least 10 distinct array sizes: `(20, 40, 60, 80, 100, 150, 200, 300, 400, 500)` for Random, Already Sorted, and Reverse Sorted inputs.

#### Scenario: Running sorting benchmark on 10 input sizes
- **WHEN** `clean_code/problem2_sorting.py` executes
- **THEN** it benchmarks all 3 algorithms across 3 input types for each of the 10 sizes, displaying comparison counts and execution times in a 90-row structured table

### Requirement: 10 Input Sizes for Problem 3 Matrix Operations
The system SHALL configure `clean_code/problem3_matrix.py` to benchmark Matrix Addition, Matrix Transpose, and Matrix Multiplication across at least 10 square matrix dimensions: `(10, 20, 30, 40, 50, 75, 100, 150, 200, 300)`.

#### Scenario: Running matrix benchmark on 10 matrix dimensions
- **WHEN** `clean_code/problem3_matrix.py` executes
- **THEN** it dynamically adjusts runs and benchmarks all 3 operations across the 10 dimensions, tabulating execution times from 10x10 to 300x300
