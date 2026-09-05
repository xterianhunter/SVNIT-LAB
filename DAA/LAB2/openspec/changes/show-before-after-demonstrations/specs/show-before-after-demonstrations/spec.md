## Purpose

Provides visible before-and-after demonstration outputs for searching, sorting, and matrix operations in `clean_code/` scripts to prove algorithmic correctness alongside asymptotic scaling benchmarks.

## ADDED Requirements

### Requirement: Searching Before-and-After Demonstration
The system SHALL implement a demonstration routine in `clean_code/problem1_searching.py` that prints the initial sample array (e.g. $N=10$) before search, followed by detailed search outcomes (target value, result index, comparisons taken) for Beginning, Middle, End, and Absent positions.

#### Scenario: Running search demonstration
- **WHEN** `clean_code/problem1_searching.py` executes
- **THEN** it prints the array before search, followed by formatted before/after search queries, before proceeding to the 10-size benchmark table

### Requirement: Sorting Before-and-After Demonstration
The system SHALL implement a demonstration routine in `clean_code/problem2_sorting.py` that prints the sample array Before Sorting and After Sorting across Random, Already Sorted, and Reverse Sorted inputs with comparison counts.

#### Scenario: Running sorting demonstration
- **WHEN** `clean_code/problem2_sorting.py` executes
- **THEN** it prints Before and After states for each sorting algorithm and distribution before displaying the 10-size benchmark table

### Requirement: Matrix Operations Before-and-After Demonstration
The system SHALL implement a demonstration routine in `clean_code/problem3_matrix.py` that prints sample matrices $A$ and $B$ before operations, followed by computed output matrices After Addition ($A+B$), After Transposition ($A^T$), and After Multiplication ($A \times B$).

#### Scenario: Running matrix demonstration
- **WHEN** `clean_code/problem3_matrix.py` executes
- **THEN** it neatly formats and prints input matrices and resultant output matrices before displaying the 10-size benchmark table
