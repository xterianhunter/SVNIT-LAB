## Purpose

Provides parallel matrix-matrix multiplication implementations comparing coarse-grained and fine-grained OpenMP thread decomposition strategies.

## ADDED Requirements

### Requirement: Parallel Matrix Multiplication Decomposition Comparison
The program SHALL perform matrix-matrix multiplication using coarse-grained decomposition and fine-grained decomposition, verify computed matrix results, and print timing comparisons.

#### Scenario: Running matrix multiplication benchmark
- **WHEN** the matrix multiplication program is executed with defined dimensions and thread count
- **THEN** it outputs execution wall-clock time for coarse-grained decomposition, execution wall-clock time for fine-grained decomposition, and verification status confirming correct results
