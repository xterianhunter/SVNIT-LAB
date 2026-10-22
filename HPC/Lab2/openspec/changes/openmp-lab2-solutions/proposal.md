## Why

This change provides clean, concise, and minimal C implementations using OpenMP for HPC Lab 2 assignments: demonstrating race conditions in concurrent multi-threaded execution, resolving race conditions using `#pragma omp critical`, and performing parallel matrix-matrix multiplication comparing coarse-grained and fine-grained decompositions.

## What Changes

- Create `race_condition.c`: A minimal OpenMP program showing non-deterministic counter corruption caused by unsynchronized concurrent writes to a shared variable across threads.
- Create `critical_section.c`: A minimal OpenMP program showing correct shared counter aggregation using `#pragma omp critical` to prevent race conditions.
- Create `matrix_mult.c`: A minimal OpenMP program implementing parallel matrix-matrix multiplication comparing coarse-grained (distributing outer loop rows) and fine-grained (parallelizing inner loop operations or collapsing loop spaces) decompositions with execution timing using `omp_get_wtime()`.
- Create `Makefile`: A minimal build configuration to compile the three OpenMP programs using `gcc -fopenmp -O2`.

## Capabilities

### New Capabilities
- `openmp-race-condition`: Multi-threaded shared counter increment demonstrating unsynchronized race conditions alongside critical section synchronization.
- `openmp-matrix-multiplication`: Parallel matrix multiplication implementations comparing coarse-grained vs. fine-grained thread decomposition strategies.

### Modified Capabilities
*(None)*

## Impact

- Adds three standalone C source files (`race_condition.c`, `critical_section.c`, `matrix_mult.c`) and a `Makefile` under the Lab 2 workspace.
- Requires GCC with OpenMP support (`-fopenmp`).
