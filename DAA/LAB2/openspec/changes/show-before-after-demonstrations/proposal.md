## Why

Academic lab reports and lab viva evaluations require both proof of algorithmic correctness (demonstrating the exact input state before and after applying an algorithm) and empirical asymptotic scalability across input sizes. Adding clear "Before & After" demonstration sections to the clean scripts makes the program output immediately self-verifying, intuitive to read in a report, and complete.

## What Changes

- Update `clean_code/problem1_searching.py`:
  - Add a `demonstrate_searching(n=10)` section printing the sample input array before search, followed by step-by-step outcomes (target, found index, comparisons) for Beginning, Middle, End, and Absent cases.
- Update `clean_code/problem2_sorting.py`:
  - Add a `demonstrate_sorting(n=10)` section printing the array Before Sorting and After Sorting (with comparison counts) across Random, Already Sorted, and Reverse Sorted inputs.
- Update `clean_code/problem3_matrix.py`:
  - Add a `demonstrate_matrix_operations(n=3)` section printing Matrix A and Matrix B Before Operations, followed by the computed output matrices After Addition ($A+B$), After Transposition ($A^T$), and After Multiplication ($A \times B$).
- Retain the full 10-size benchmark tables and theoretical analysis across all three scripts.

## Capabilities

### New Capabilities
- `show-before-after-demonstrations`: Explicit before-and-after state demonstration routines for searching, sorting, and matrix operations in `clean_code/` scripts.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**:
  - `clean_code/problem1_searching.py`
  - `clean_code/problem2_sorting.py`
  - `clean_code/problem3_matrix.py`
- **Dependencies**: Python standard library only.
