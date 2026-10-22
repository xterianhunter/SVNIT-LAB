## Why

CS103 (Design and Analysis of Algorithms) Lab Assignment 6 requires implementing large integer multiplication using the Karatsuba Divide and Conquer algorithm ($O(n^{\log_2 3}) \approx O(n^{1.585})$) and comparing it against conventional multiplication ($O(n^2)$). Appending this implementation concisely to the existing `daa_assignments_1_to_5.ipynb` notebook fulfills the lab curriculum requirements in a single, compact, and easily reviewable submission.

## What Changes

- Append Assignment 6 at the end of the existing notebook `daa_assignments_1_to_5.ipynb`:
  - **Conventional Multiplication**: Standard digit-by-digit / grade-school multiplication simulating fixed-size base operations ($O(n^2)$).
  - **Karatsuba Algorithm**: Divide-and-conquer multiplication splitting numbers into high and low halves and computing 3 recursive products instead of 4 ($O(n^{1.585})$).
  - **Empirical Benchmarks**: Test with integers of increasing digit lengths (e.g., 64, 128, 256, 512, 1024 digits), verifying product correctness and measuring execution times in microseconds ($\mu\text{s}$).
  - **Complexity Analysis**: Tabulate empirical speedups against theoretical bounds ($O(n^2)$ vs. $O(n^{1.585})$).

## Capabilities

### New Capabilities
- `karatsuba-multiplication`: Concise implementations and comparative benchmarks for conventional and Karatsuba large integer multiplication.

### Modified Capabilities
*(None)*

## Impact

- Extends the existing `daa_assignments_1_to_5.ipynb` notebook without modifying previous assignments.
- Uses only Python standard libraries (`random`, `math`, `time`).
