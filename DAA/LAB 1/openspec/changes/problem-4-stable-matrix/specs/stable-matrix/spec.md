## Purpose

Provides capabilities to check the stability of an $n \times n$ integer matrix, identify all violating non-boundary elements, and report the position with the maximum absolute difference between the element and its orthogonal neighbours.

## ADDED Requirements

### Requirement: Matrix Stability Evaluation
The system SHALL evaluate each non-boundary element ($1 \le i \le n-2, 1 \le j \le n-2$) of an $n \times n$ integer matrix and determine whether $A[i][j] == A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]$.

#### Scenario: Completely stable matrix
- **WHEN** matrix is `[[6, 1, 8], [5, 15, 7], [7, 2, 10]]`
- **THEN** system determines center element equals neighbour sum ($15 == 1+2+5+7$) and reports `"Matrix is stable."`

#### Scenario: Small matrix with no non-boundary elements ($n < 3$)
- **WHEN** matrix is `[[1, 2], [3, 4]]`
- **THEN** system confirms there are no non-boundary elements and reports `"Matrix is stable."`

---

### Requirement: Violation Counting and Tracking
The system SHALL calculate the absolute difference $D(i, j) = |A[i][j] - (A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1])|$ for all non-boundary elements. If any $D(i, j) > 0$, the system SHALL report the total count and the exact coordinate positions of all violating elements.

#### Scenario: Single violating element
- **WHEN** matrix is `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- **THEN** system reports 1 violating element at position `(1, 1)`

#### Scenario: Multiple violating elements
- **WHEN** a $4 \times 4$ matrix has deviations at `(1, 1)` and `(2, 2)`
- **THEN** system reports `2` violating elements and lists positions `[(1, 1), (2, 2)]`

---

### Requirement: Maximum Absolute Difference Identification
When the matrix is not stable, the system SHALL determine and report the position having the maximum absolute difference $\max D(i, j)$, along with its value, neighbour sum, and calculated deviation $D(i, j)$.

#### Scenario: Maximum deviation reporting
- **WHEN** matrix is `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- **THEN** system identifies position `(1, 1)` with value `5`, neighbour sum `20`, and maximum difference `D(1, 1) = 15`
