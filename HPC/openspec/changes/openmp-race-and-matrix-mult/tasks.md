## 1. Project Infrastructure & Common Utilities

- [x] 1.1 Create project directory structure (`src/`, `bin/`, `scripts/`) and common utility header (`src/common.h`) containing matrix allocation, random initialization, timer utilities (`omp_get_wtime()`), and numerical verification functions, verifying with header compilation tests.
- [x] 1.2 Implement root `Makefile` with targets for compiling race condition, critical section, and matrix multiplication executables using `gcc -fopenmp -O3 -Wall`, verifying build and clean targets.

## 2. Concurrency Control & Race Condition Demonstrations

- [x] 2.1 Implement `src/race_condition.c` demonstrating a multi-threaded race condition on an unsynchronized shared counter, verifying that execution with `OMP_NUM_THREADS > 1` produces non-deterministic final counts differing from the expected total.
- [x] 2.2 Implement `src/critical_section.c` utilizing `#pragma omp critical` to enforce mutual exclusion on the shared counter, verifying that execution across arbitrary thread counts consistently yields the exact theoretical count.

## 3. Parallel Matrix Multiplication Implementation

- [x] 3.1 Implement sequential baseline matrix-matrix multiplication in `src/matrix_mult.c` to serve as the ground-truth reference for verification and speedup calculation.
- [x] 3.2 Implement coarse-grained parallel matrix multiplication in `src/matrix_mult.c` using row-level distribution (`#pragma omp parallel for schedule(static)`), and verify output correctness against the sequential baseline.
- [x] 3.3 Implement fine-grained parallel matrix multiplication in `src/matrix_mult.c` using element-level fine task/dynamic scheduling (`#pragma omp parallel for collapse(2) schedule(dynamic, 1)`), and verify output correctness against the sequential baseline.

## 4. Benchmarking, Analysis & Documentation

- [x] 4.1 Create automated benchmark script `scripts/run_benchmarks.sh` to run both coarse-grained and fine-grained matrix multiplication across large matrix sizes ($N \ge 1000$) and multiple thread configurations ($T \in \{1, 2, 4, 8\}$).
- [x] 4.2 Execute benchmarks, collect execution time, speedup, and efficiency metrics, and document comparative performance analysis highlighting trade-offs between coarse and fine granularity.
