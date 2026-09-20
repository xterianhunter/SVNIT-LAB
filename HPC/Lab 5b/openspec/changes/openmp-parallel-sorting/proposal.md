## Why

Evaluating parallel programming paradigms requires empirical comparison against sequential baselines. This change implements and evaluates OpenMP parallel sorting algorithms (Merge Sort with sections and Quick Sort with tasks), contrasting them with sequential versions and an optimized depth-limited hybrid Quick Sort with insertion sort cutoffs on large integer arrays.

## What Changes

- Implement sequential Merge Sort and sequential Quick Sort algorithms as baselines.
- Implement parallel Merge Sort using OpenMP sections (`#pragma omp section`).
- Implement parallel Quick Sort using OpenMP tasks (`#pragma omp task`).
- Implement depth-limited parallel Quick Sort (configured for depth cutoff 4/8) transitioning to sequential insertion sort for small partitions to minimize task overhead.
- Provide a clean, robust benchmark harness that verifies sort correctness, measures execution time via `omp_get_wtime()`, and outputs a formatted comparative performance table.
- Provide instructions and formatted outputs suitable for laboratory report submission.

## Capabilities

### New Capabilities
- `parallel-sorting`: Implementation of sequential, OpenMP section-based, OpenMP task-based, and depth-limited hybrid sorting algorithms with a verification and benchmarking driver.

### Modified Capabilities
*(None)*

## Impact

- Adds standalone, clean C source code (e.g., `sort_benchmark.c`) requiring an OpenMP-compatible compiler (e.g., `gcc -fopenmp`).
- Generates reproducible performance comparison metrics for lab reporting without extraneous dependencies.
