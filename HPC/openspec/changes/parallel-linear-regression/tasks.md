## 1. Directory and Build Setup

- [x] 1.1 Create `Lab2/` directory and configure `Lab2/Makefile` to compile OpenMP programs with `-fopenmp -O3 -Wall -lm` and verify `make` compiles target binaries without errors.

## 2. Linear Regression Implementation

- [x] 2.1 Implement 3D dataset generation ($X_1, X_2 \to Y$) with configurable sample size $N$, ground-truth weights, and noise in `Lab2/linear_regression.c` and verify data buffer allocation and initialization.
- [x] 2.2 Implement sequential batch gradient descent in `Lab2/linear_regression.c` and verify model convergence and parameter recovery.
- [x] 2.3 Implement OpenMP-parallelized batch gradient descent with reduction clauses in `Lab2/linear_regression.c` and verify that parallel weights match sequential results within floating-point tolerance.

## 3. Benchmarking and Performance Evaluation

- [x] 3.1 Implement benchmarking harness in `Lab2/linear_regression.c` to measure wall-clock execution time via `omp_get_wtime()` across sequential baseline and multi-threaded configurations (e.g., 1, 2, 4, 8 threads).
- [x] 3.2 Execute the benchmark on large datasets ($N \ge 1{,}000{,}000$), calculate speedup ($S = T_{\text{seq}} / T_{\text{par}}$), and verify tabular performance output.
