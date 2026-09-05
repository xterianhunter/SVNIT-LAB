## Purpose

Provides from-scratch implementations of Matrix Addition, Matrix Transpose, and Matrix Multiplication, and benchmarks their execution times across square matrices of increasing dimension to evaluate $\mathcal{O}(n^2)$ and $\mathcal{O}(n^3)$ complexities.

## ADDED Requirements

### Requirement: Matrix Addition Algorithm
The system SHALL implement element-wise matrix addition $C = A + B$ for two $n \times n$ matrices without using external numerical libraries.

#### Scenario: Add two square matrices
- **WHEN** Matrix Addition is performed on two $n \times n$ matrices $A$ and $B$
- **THEN** the resultant matrix $C$ has $C[i][j] = A[i][j] + B[i][j]$ computed in $\mathcal{O}(n^2)$ time

### Requirement: Matrix Transpose Algorithm
The system SHALL implement matrix transposition $A^T$ for an $n \times n$ matrix by interchanging rows and columns.

#### Scenario: Transpose a square matrix
- **WHEN** Matrix Transpose is performed on matrix $A$
- **THEN** the resultant matrix $T$ satisfies $T[i][j] = A[j][i]$ for all $0 \le i, j < n$ computed in $\mathcal{O}(n^2)$ time

### Requirement: Matrix Multiplication Algorithm
The system SHALL implement standard matrix multiplication $C = A \times B$ for two $n \times n$ matrices using the classical triple-nested loop formulation without external libraries.

#### Scenario: Multiply two square matrices
- **WHEN** Matrix Multiplication is performed on matrices $A$ and $B$
- **THEN** each element $C[i][j] = \sum_{k=0}^{n-1} A[i][k] B[k][j]$ is computed executing $n^3$ multiplications in $\mathcal{O}(n^3)$ time

### Requirement: Programmatic Matrix Generation and Benchmarking
The system SHALL programmatically generate random integer square matrices for sizes $10 \times 10, 50 \times 50, 100 \times 100, 200 \times 200, 500 \times 500$, measure execution latency, and display results in a structured table.

#### Scenario: Benchmark execution across sizes
- **WHEN** the benchmarking harness executes across all specified matrix dimensions
- **THEN** average execution times (in $\mu\text{s}$ and $\text{ms}$) are tabulated alongside asymptotic complexity observations
