## Purpose

Provides capabilities to check whether an $n \times n$ integer matrix is locally balanced (each element equals the sum of its valid orthogonal neighbours) and report the first violating element in row-major order.

## ADDED Requirements

### Requirement: Locally Balanced Matrix Validation
The system SHALL inspect each element $A[i][j]$ of an $n \times n$ matrix in row-major order, compute the sum of all valid neighbours (up, down, left, right) within matrix boundaries, and determine if $A[i][j] == \text{neighbour\_sum}$.

#### Scenario: Locally balanced matrix (all elements satisfy condition)
- **WHEN** matrix is `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`
- **THEN** system determines that every cell equals its neighbour sum (0 == 0) and reports `"Matrix is locally balanced."`

#### Scenario: Balanced non-zero matrix
- **WHEN** matrix is `[[0, 0], [0, 0]]`
- **THEN** system confirms all elements equal their 2 valid neighbours (0 == 0 + 0) and reports `"Matrix is locally balanced."`

---

### Requirement: Row-Major Violation Reporting
The system SHALL report the first violating element encountered during row-major traversal ($i = 0 \dots n-1, j = 0 \dots n-1$), displaying its position `(row, col)`, the element's actual value, and the sum of its valid neighbours.

#### Scenario: First element violates condition
- **WHEN** matrix is `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- **THEN** system reports violation at position `(0, 0)` with value `1` and neighbour sum `6` (`A[0][1] + A[1][0] = 2 + 4 = 6`)

#### Scenario: Violation occurs at interior element
- **WHEN** matrix is `[[2, 1, 2], [1, 5, 1], [2, 1, 2]]`
- **THEN** system identifies position `(1, 1)` where value is `5` and neighbour sum is `4` (`1 + 1 + 1 + 1 = 4`)

---

### Requirement: Boundary and Corner Handling
The system SHALL correctly consider only valid adjacent neighbours:
- 2 neighbours for corner elements
- 3 neighbours for non-corner boundary elements
- 4 neighbours for interior elements
- 0 neighbours (sum = 0) for $1 \times 1$ matrices

#### Scenario: Single element matrix ($1 \times 1$)
- **WHEN** matrix is `[[0]]`
- **THEN** system confirms it is locally balanced (0 == 0)

#### Scenario: Non-zero single element matrix
- **WHEN** matrix is `[[5]]`
- **THEN** system reports violation at position `(0, 0)` with value `5` and neighbour sum `0`
