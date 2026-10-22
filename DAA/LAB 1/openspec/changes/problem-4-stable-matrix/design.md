## Context

See `proposal.md`. Problem 4 of DAA Lab Assignment 1 (CSDS103) requires checking the stability of an $n \times n$ matrix:
$$A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1] \quad \text{for } 1 \le i, j \le n-2$$
If unstable, the algorithm must calculate the absolute differences $D(i, j) = |A[i][j] - \text{NeighbourSum}(i, j)|$, count and list all violating positions, and identify the position with the maximum difference $\max D(i, j)$.

## Goals / Non-Goals

**Goals:**
- Provide a clean, short, and simple Python implementation (`problem4_stable_matrix.py`).
- Implement single-pass interior element scanning ($O(n^2)$ time, $O(1)$ auxiliary memory).
- Track total violations, all violating coordinates, and the maximum deviation cell.
- State explicitly that no additional matrix is required.
- Provide automated unit tests in `test_problem4.py` and analysis in `problem4_analysis.md`.

**Non-Goals:**
- Allocating an auxiliary difference matrix (an additional matrix is not needed).

## Decisions

### 1. In-Place Single-Pass Evaluation
- Traverse non-boundary rows $i \in [1, n-2]$ and columns $j \in [1, n-2]$.
- For each interior element, compute $S(i, j) = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]$ and $D(i, j) = |A[i][j] - S(i, j)|$.
- Maintain running list of violating positions and update the maximum difference tracking variables (`max_diff`, `max_pos`).

### 2. Pseudocode

```text
ALGORITHM CheckMatrixStability(A, n):
    IF n < 3 THEN
        RETURN (TRUE, 0, [], NULL)

    violatingPositions ← []
    maxDiff ← -1
    maxDiffInfo ← NULL

    FOR i FROM 1 TO n - 2 DO:
        FOR j FROM 1 TO n - 2 DO:
            nSum ← A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]
            diff ← Abs(A[i][j] - nSum)
            
            IF diff > 0 THEN
                Append (i, j) to violatingPositions
                IF diff > maxDiff THEN
                    maxDiff ← diff
                    maxDiffInfo ← ((i, j), A[i][j], nSum, diff)

    IF Length(violatingPositions) == 0 THEN
        RETURN (TRUE, 0, [], NULL)
    ELSE
        RETURN (FALSE, Length(violatingPositions), violatingPositions, maxDiffInfo)
```

## Risks / Trade-offs

- **[Ties in Maximum Difference]** → Handled: Preserves first maximum difference position in row-major order.
- **[Memory footprint]** → Auxiliary space is $O(1)$ scalar variables (no extra matrix required).
