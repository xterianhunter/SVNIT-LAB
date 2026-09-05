## Why

This change implements Problem 3 from DAA Lab Assignment 2 (CSDS103, SVNIT). It provides clean, from-scratch implementations of fundamental matrix operations—Matrix Addition ($\mathcal{O}(n^2)$), Matrix Transposition ($\mathcal{O}(n^2)$), and Matrix Multiplication ($\mathcal{O}(n^3)$)—and benchmarks their execution times across square matrices of sizes $10 \times 10, 50 \times 50, 100 \times 100, 200 \times 200, 500 \times 500$ to experimentally validate their polynomial time complexity bounds.

## What Changes

- Implement core matrix operations from first principles:
  - **Matrix Addition**: Element-wise sum of two $n \times n$ matrices ($\mathcal{O}(n^2)$).
  - **Matrix Transpose**: Inversion of rows and columns ($A^T[i][j] = A[j][i]$) in $\mathcal{O}(n^2)$.
  - **Matrix Multiplication**: Classical triple-loop matrix product $C[i][j] = \sum_k A[i][k] B[k][j]$ ($\mathcal{O}(n^3)$).
- Implement programmatic square matrix generator for sizes $N \in \{10, 50, 100, 200, 500\}$.
- Benchmark execution latency using high-resolution monotonic timers (`time.perf_counter_ns()`).
- Output structured comparison tables (Matrix Size vs Execution Time) and theoretical complexity comparisons.
- Provide a dedicated, clean, and concise single-file script `problem3_matrix.py` suited for M.Tech lab evaluation.

## Capabilities

### New Capabilities
- `matrix-algorithms`: Implementations of Matrix Addition, Transpose, and Multiplication from scratch, square matrix generator, benchmarking harness, tabular output, and complexity analysis.

### Modified Capabilities
<!-- None -->

## Impact

- **New files**:
  - `problem3_matrix.py` (self-contained, clean script for M.Tech student lab submission)
- **Dependencies**: Python standard library only (`time`, `random`), guaranteeing 100% portability without external dependencies (no NumPy/SciPy required).
