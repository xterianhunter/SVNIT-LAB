## Why

Gradient Descent for multi-variable linear regression on large datasets involves compute-intensive summation of loss gradients across millions of data points per iteration. This change introduces a clean, minimal OpenMP parallelized implementation of 2D-feature linear regression (3-dimensional data space: $X_1, X_2 \to Y$) to evaluate and compare running time performance and speedup against a sequential baseline.

## What Changes

- Implement sequential and OpenMP-parallelized batch Gradient Descent for multi-variable linear regression with 2D features ($x_1, x_2$) and 1D label ($y$).
- Apply OpenMP parallel loop reductions (`#pragma omp parallel for reduction(+:...)`) to parallelize the per-iteration gradient accumulation across large sample sets.
- Provide a concise benchmarking and execution setup inside the `Lab2/` folder to compare sequential vs parallel execution times across various thread counts.
- Add minimal build configuration (`Makefile`) inside `Lab2/` with `-fopenmp -O3 -lm`.

## Capabilities

### New Capabilities
- `parallel-linear-regression`: Implements sequential and OpenMP parallel gradient descent for 2D feature linear regression on large datasets, measuring and comparing execution time and speedup.

### Modified Capabilities
<!-- No existing capabilities being modified -->

## Impact

- **Source Code**: Minimal C implementation files and build configuration placed directly inside `Lab2/`.
- **Toolchain**: Requires GCC/Clang with OpenMP support (`-fopenmp`) and standard C math library (`-lm`).
- **Performance**: Accelerates gradient evaluation on multi-core systems when training over large datasets ($10^6+$ datapoints).
