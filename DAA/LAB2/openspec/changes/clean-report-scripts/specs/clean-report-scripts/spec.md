## Purpose

Provides concise, readable, first-principle implementations of searching, sorting, and matrix algorithms in `clean_code/` formatted specifically for lab report submissions and oral viva evaluation.

## ADDED Requirements

### Requirement: Clean Problem 1 Searching Script
The system SHALL provide `clean_code/problem1_searching.py` implementing first-principles Linear Search and Binary Search, reading input arrays of sizes (10, 50, 100, 200) from files, benchmarking four test cases (Beginning, Middle, End, Absent), and printing a clean tabular results summary with theoretical analysis.

#### Scenario: Running clean searching benchmark
- **WHEN** `clean_code/problem1_searching.py` is executed
- **THEN** it generates/loads file datasets, executes search benchmarks across all test cases, and outputs a formatted metrics table and complexity analysis within standard terminal width

### Requirement: Clean Problem 2 Sorting Script
The system SHALL provide `clean_code/problem2_sorting.py` implementing first-principles Bubble Sort (with early termination), Selection Sort, and Insertion Sort across Random, Already Sorted, and Reverse Sorted inputs for sizes (50, 100, 200, 500), displaying execution times, comparisons, and theoretical complexity bounds in a clean table.

#### Scenario: Running clean sorting benchmark
- **WHEN** `clean_code/problem2_sorting.py` is executed
- **THEN** it benchmarks all 3 sorting algorithms across all 3 input configurations and prints an organized results table with $\mathcal{O}(n)$, $\mathcal{O}(n^2)$, and $\Theta(n^2)$ analysis

### Requirement: Clean Problem 3 Matrix Script
The system SHALL provide `clean_code/problem3_matrix.py` implementing first-principles Matrix Addition, Matrix Transpose, and Matrix Multiplication on programmatically generated square matrices of sizes (10x10, 50x50, 100x100, 200x200, 500x500), displaying execution times in microseconds/milliseconds alongside theoretical complexities ($\mathcal{O}(n^2)$ vs $\mathcal{O}(n^3)$).

#### Scenario: Running clean matrix benchmark
- **WHEN** `clean_code/problem3_matrix.py` is executed
- **THEN** it benchmarks addition, transpose, and multiplication across all matrix dimensions and prints a structured comparison table

### Requirement: Conciseness and Zero-Dependency Portability
All scripts placed in `clean_code/` SHALL be self-contained, standard-library-only, free of heavy inline markup/SVG templates, and concise (~100–150 lines) so they are directly readable and suitable for lab report inclusion.

#### Scenario: Script structure and line economy
- **WHEN** any script in `clean_code/` is inspected
- **THEN** it contains pure algorithm logic, data generation/file loading, benchmarking harness, and table printer without extraneous markup code
