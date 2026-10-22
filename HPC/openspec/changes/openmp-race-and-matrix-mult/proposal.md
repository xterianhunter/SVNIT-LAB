## Why

High-Performance Computing (HPC) relies heavily on shared-memory parallelism using OpenMP to accelerate compute-intensive workloads while maintaining thread safety. This change introduces OpenMP-based demonstration and benchmarking programs to explore fundamental multi-threading concepts: data race conditions, mutual exclusion synchronization using critical sections, and parallel matrix-matrix multiplication comparing coarse-grained versus fine-grained data decomposition strategies on large input datasets.

## What Changes

- Implement a C/C++ OpenMP program demonstrating race conditions when multiple competing threads concurrently update an unsynchronized shared variable/counter.
- Implement an OpenMP critical section solution (`#pragma omp critical`) to enforce mutual exclusion and ensure thread-safe updates to the shared resource.
- Design, implement, and benchmark parallel matrix-matrix multiplication on large matrices using both coarse-grained (row-level / block-level) and fine-grained (element-level / inner loop) data decomposition approaches.
- Provide automated build configuration (Makefile or CMake) and benchmarking harness to measure, compare, and report execution time, speedup, and scaling behavior across varying thread counts.

## Capabilities

### New Capabilities
- `concurrency-control`: Demonstrates race conditions on shared memory without synchronization and resolves them using OpenMP critical sections (`#pragma omp critical`), validating correctness across varying thread counts.
- `parallel-matrix-multiplication`: Implements parallel matrix-matrix multiplication on large matrices, contrasting coarse-grained vs. fine-grained OpenMP decomposition strategies with empirical execution timing and performance metrics.

### Modified Capabilities
<!-- No existing capabilities being modified -->

## Impact

- **Source Code**: New C/C++ source files under lab directories for race condition demonstrations and matrix multiplication benchmarks.
- **Build & Execution**: Compilation with OpenMP flags (`-fopenmp`) with GCC/Clang and execution across configurable thread configurations (`OMP_NUM_THREADS`).
- **Dependencies**: Standard C/C++ toolchain with OpenMP runtime support.
