## Why

Gradient descent for linear regression on large datasets involves intensive data-parallel computations across all training samples. Parallelizing the gradient accumulation across threads using OpenMP significantly reduces execution time and demonstrates parallel scaling compared to sequential gradient descent.

## What Changes

- Implement sequential gradient descent for 2D feature linear regression ($y = w_1 x_1 + w_2 x_2 + b$).
- Implement parallel gradient descent using OpenMP directives (`#pragma omp parallel for reduction(...)`).
- Generate synthetic 3-dimensional dataset ($x_1, x_2, y$) with a large number of datapoints (e.g. $10^6$ to $10^7$ samples).
- Provide a timing and performance comparison between sequential and OpenMP parallel execution using `omp_get_wtime()`.
- Ensure clean, short, and concise C code with zero unnecessary abstractions or boilerplate.

## Capabilities

### New Capabilities
- `linear-regression-openmp`: Parallel linear regression with 2D features and 1D label using OpenMP gradient descent and timing comparison.

### Modified Capabilities
<!-- None -->

## Impact

- Creates a standalone C program (`linear_regression_omp.c`).
- Requires GCC or compatible C compiler with OpenMP support (`-fopenmp`).
- No breaking changes or impacts on existing systems.
