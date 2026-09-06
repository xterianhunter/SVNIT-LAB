## Purpose

Performs matrix multiplication on two dynamically allocated 2D matrices based on user-provided dimensions and elements.

## ADDED Requirements

### Requirement: Matrix Dimension Validation and Allocation
The program SHALL read dimensions for Matrix A (rows $r_1$, cols $c_1$) and Matrix B (rows $r_2$, cols $c_2$), dynamically allocate memory for both matrices and the result matrix, and verify compatibility ($c_1 = r_2$).

#### Scenario: Compatible matrix dimensions
- **WHEN** user inputs dimensions where columns of Matrix A equals rows of Matrix B
- **THEN** dynamic memory is allocated for Matrix A, Matrix B, and result Matrix C ($r_1 \times c_2$)

#### Scenario: Incompatible matrix dimensions
- **WHEN** user inputs dimensions where $c_1 \neq r_2$
- **THEN** the program outputs an error message and terminates without performing multiplication

### Requirement: Matrix Multiplication Computation
The program SHALL calculate the product $C = A \times B$ such that $C[i][j] = \sum_{k=0}^{c_1-1} A[i][k] \times B[k][j]$.

#### Scenario: Multiplied matrix values
- **WHEN** valid matrices A and B are entered
- **THEN** result matrix C is computed and displayed correctly

### Requirement: Matrix Deallocation
The program SHALL free all dynamically allocated memory for all matrices before exiting.

#### Scenario: Clean memory release
- **WHEN** matrix multiplication completes and output is displayed
- **THEN** all row pointers and matrix structures are freed
