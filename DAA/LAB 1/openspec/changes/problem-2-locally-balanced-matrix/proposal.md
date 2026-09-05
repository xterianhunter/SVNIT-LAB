## Why

An $n \times n$ integer matrix is locally balanced if each element equals the sum of its valid adjacent neighbours in the four orthogonal directions (up, down, left, right). To solve Problem 2 of DAA Lab Assignment 1 (CSDS103), we need an algorithm and concise program to determine whether a given matrix is locally balanced, and if not, report the first violating element in row-major order with its row/column position, value, and calculated neighbour sum. The solution must gracefully handle corner (2 neighbours), boundary (3 neighbours), interior (4 neighbours), and $1 \times 1$ boundary cases.

## What Changes

- Create a clean and short Python program (`problem2_locally_balanced_matrix.py`) to verify local balance of an $n \times n$ matrix.
- Implement directional neighbour calculation considering only valid in-bounds matrix cells.
- Report either `"Matrix is locally balanced"` or detailed information on the first violating element (`row`, `col`, `value`, `neighbour_sum`) in row-major order.
- Include built-in relevant example matrices (balanced and unbalanced) as well as optional user input.
- Create automated unit tests in `test_problem2.py` and detailed complexity/boundary analysis in `problem2_analysis.md`.

## Capabilities

### New Capabilities
- `locally-balanced-matrix`: Verification of locally balanced property for $n \times n$ integer matrices and reporting first row-major violation.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New script `problem2_locally_balanced_matrix.py`.
- **Tests**: `test_problem2.py` covering balanced matrices, unbalanced matrices, corners, edges, and single-element matrices.
- **Documentation**: `problem2_analysis.md` documenting corner/edge/interior logic, pseudocode, and time/space complexity analysis ($O(n^2)$ time, $O(1)$ auxiliary space).
