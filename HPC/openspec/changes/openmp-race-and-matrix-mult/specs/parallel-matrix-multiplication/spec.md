## Purpose

Provides OpenMP parallel matrix-matrix multiplication implementations supporting coarse-grained and fine-grained data decomposition strategies with empirical performance comparison on large matrices.

## ADDED Requirements

### Requirement: Matrix Multiplication Numerical Correctness
The system SHALL correctly compute the matrix product $C = A \times B$ for two input square/rectangular matrices of dimension $N \times N$ and verify computational correctness against a sequential baseline or theoretical checksum.

#### Scenario: Verification against sequential baseline
- **WHEN** parallel matrix multiplication is executed with arbitrary thread counts
- **THEN** every element of the resulting matrix $C$ SHALL match the corresponding value in the sequentially computed reference matrix within floating-point epsilon tolerance (or exact match for integer arithmetic)

### Requirement: Coarse-Grained Data Decomposition
The system SHALL implement a coarse-grained OpenMP parallel matrix-matrix multiplication approach where chunks of rows (or outer-loop iterations) are partitioned among threads.

#### Scenario: Multi-threaded execution of coarse-grained decomposition
- **WHEN** the coarse-grained matrix multiplication is executed on large matrices (e.g., $N \ge 1000$) using multiple threads (`OMP_NUM_THREADS > 1`)
- **THEN** outer-loop rows SHALL be distributed across threads with low scheduling/synchronization overhead and output total computation wall-clock time

### Requirement: Fine-Grained Data Decomposition
The system SHALL implement a fine-grained OpenMP parallel matrix-matrix multiplication approach where individual matrix elements or inner loops/tasks are parallelized across threads.

#### Scenario: Multi-threaded execution of fine-grained decomposition
- **WHEN** the fine-grained matrix multiplication is executed on the same matrix dimensions and thread configurations as the coarse-grained version
- **THEN** fine-grained tasks/inner iterations SHALL execute in parallel across threads and output total computation wall-clock time

### Requirement: Performance Comparison and Benchmarking Harness
The system SHALL provide a benchmarking facility and driver to measure and compare execution time, speedup, and efficiency between coarse-grained and fine-grained data decomposition methods across different matrix sizes and thread counts.

#### Scenario: Benchmark execution and comparative reporting
- **WHEN** the benchmark driver runs both coarse-grained and fine-grained decomposition methods on large matrices with thread counts varying from 1 to $T_{\max}$
- **THEN** the benchmark SHALL output a structured comparison showing execution wall-clock time (seconds), speedup relative to single-threaded baseline, and performance differences between coarse and fine granularity
