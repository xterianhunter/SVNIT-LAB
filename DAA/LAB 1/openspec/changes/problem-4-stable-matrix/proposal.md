## Why

In an $n \times n$ integer matrix, stability requires every non-boundary (interior) element to satisfy $A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]$. To solve Problem 4 of DAA Lab Assignment 1 (CSDS103), we need an algorithm and clean program to determine if a matrix is stable. If it is unstable, the program must calculate the absolute differences $D(i, j) = |A[i][j] - \text{Neighbours}(i, j)|$, report the number and positions of all violating elements, and pinpoint the element with the maximum absolute difference.

## What Changes

- Create `problem4_stable_matrix.py` implementing single-pass interior element inspection.
- Compute $D(i, j)$ for all $1 \le i, j \le n-2$ without allocating any auxiliary matrix.
- Report total count of violations, list of all violating $(i, j)$ coordinates, and the maximum deviation position $(i, j)$ with its difference.
- Provide interactive CLI and built-in sample matrices (stable and unstable).
- Create automated unit tests in `test_problem4.py` and comprehensive complexity analysis in `problem4_analysis.md`.

## Capabilities

### New Capabilities
- `stable-matrix`: Matrix stability evaluation, violation counting, position tracking, and maximum deviation analysis for non-boundary elements.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New script `problem4_stable_matrix.py`.
- **Tests**: `test_problem4.py` testing stable and unstable matrices of varying dimensions ($3 \times 3$, $4 \times 4$, $5 \times 5$, and small matrices $n < 3$).
- **Documentation**: `problem4_analysis.md` analyzing best/worst case complexity ($O(n^2)$), auxiliary space ($O(1)$), and proof that no additional matrix is needed.
