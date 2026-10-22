## Purpose

Calculates the scalar dot product of two vectors using dynamically allocated arrays with user-provided size and values.

## ADDED Requirements

### Requirement: Vector Allocation and Input
The program SHALL prompt the user for vector size $n$, dynamically allocate two arrays of size $n$, and populate them from standard input.

#### Scenario: Read vector dimension and values
- **WHEN** user enters vector size $n$ followed by elements for vector A and vector B
- **THEN** memory for both vectors is allocated and elements are stored

### Requirement: Dot Product Computation
The program SHALL compute the scalar dot product $\sum_{i=0}^{n-1} A[i] \times B[i]$.

#### Scenario: Dot product of two vectors
- **WHEN** vector A is `[1, 2, 3]` and vector B is `[4, 5, 6]`
- **THEN** computed dot product is `32` ($1\cdot 4 + 2\cdot 5 + 3\cdot 6$)

### Requirement: Vector Memory Deallocation
The program SHALL free both dynamically allocated vector buffers before termination.

#### Scenario: Memory cleanup
- **WHEN** calculation completes and result is printed
- **THEN** both vector buffers are released using standard free
