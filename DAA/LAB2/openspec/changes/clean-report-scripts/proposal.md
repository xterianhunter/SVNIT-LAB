## Why

Lab submission reports and viva evaluations require clean, concise, readable code listings without extensive visualization HTML/SVG template bloat. The current standalone problem scripts contain several hundred lines of inline SVG and HTML generators. To make the code clean, elegant, and directly report-ready, we need concise rewritten versions of Problem 1, Problem 2, and Problem 3 located in a dedicated directory (`clean_code/`) that retain 100% functional correctness, first-principle implementations, benchmarking, and tabular complexity analysis while stripping out unnecessary boilerplate.

## What Changes

- Create a new directory `clean_code/` dedicated to concise, submission-ready lab scripts.
- Implement `clean_code/problem1_searching.py`:
  - First-principles Linear Search & Binary Search.
  - File-based dataset loading for sizes 10, 50, 100, 200.
  - 4 test cases (Beginning, Middle, End, Absent).
  - Concise timing harness and formatted console results table with theoretical comparison.
- Implement `clean_code/problem2_sorting.py`:
  - First-principles Bubble Sort (early exit), Selection Sort, and Insertion Sort.
  - 3 input distributions (Random, Sorted, Reverse) across sizes 50, 100, 200, 500.
  - High-precision timing, comparison tracking, and formatted console results table.
- Implement `clean_code/problem3_matrix.py`:
  - First-principles Matrix Addition, Matrix Transpose, and Matrix Multiplication.
  - Programmatic square matrix generation for sizes 10x10, 50x50, 100x100, 200x200, 500x500.
  - Adaptive run timing and formatted tabular output comparing $\mathcal{O}(n^2)$ vs $\mathcal{O}(n^3)$.
- Keep each script short (~100–140 lines), standard-library-only, well-commented, and directly printable for academic lab report inclusion.

## Capabilities

### New Capabilities
- `clean-report-scripts`: Concise, report-ready implementations of Problem 1 (Searching), Problem 2 (Sorting), and Problem 3 (Matrix operations) in `clean_code/` focusing on core logic, benchmarking, and clear tabular output.

### Modified Capabilities
<!-- None -->

## Impact

- **New Files**:
  - `clean_code/problem1_searching.py`
  - `clean_code/problem2_sorting.py`
  - `clean_code/problem3_matrix.py`
- **Dependencies**: Python standard library only (`time`, `random`, `os`).
