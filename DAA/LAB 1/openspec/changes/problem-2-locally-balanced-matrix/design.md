## Context

See `proposal.md`. Problem 2 of DAA Lab Assignment 1 (CSDS103) requires checking whether an $n \times n$ integer matrix is locally balanced ($A[i][j] = \sum \text{valid neighbours}$) and reporting the first violating cell in row-major order. The code should be short, simple, and self-contained with demonstration matrices.

## Goals / Non-Goals

**Goals:**
- Provide a short, readable, and modular Python implementation (`problem2_locally_balanced_matrix.py`).
- Implement bounds-checked orthogonal neighbour summation for 4 directions (up, down, left, right).
- Correctly handle corner (2 neighbours), boundary (3 neighbours), interior (4 neighbours), and $1 \times 1$ (0 neighbours) elements.
- Report the first violating element in row-major order (`(row, col)`, `value`, `neighbour_sum`) or confirm balance.
- Include built-in relevant test matrices (both balanced and unbalanced) with optional interactive user input.

**Non-Goals:**
- Creating an additional auxiliary matrix (auxiliary space must be strictly $O(1)$).

## Decisions

### 1. In-Place Directional Neighbour Calculation
- Use direction offsets `[(-1, 0), (1, 0), (0, -1), (0, 1)]` (Up, Down, Left, Right).
- Check `0 <= i + di < n` and `0 <= j + dj < n` to strictly consider only existing elements within the matrix.
- Single-pass row-major traversal (`i` from 0 to $n-1$, `j` from 0 to $n-1$) guarantees finding the first violation in row-major order.

### 2. Pseudocode

```text
ALGORITHM CheckLocallyBalanced(A, n):
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    FOR i FROM 0 TO n - 1 DO:
        FOR j FROM 0 TO n - 1 DO:
            neighbourSum = 0
            FOR EACH (di, dj) IN DIRECTIONS DO:
                ni = i + di
                nj = j + dj
                IF 0 <= ni < n AND 0 <= nj < n THEN
                    neighbourSum = neighbourSum + A[ni][nj]
            
            IF A[i][j] != neighbourSum THEN
                RETURN (FALSE, (i, j), A[i][j], neighbourSum)

    RETURN (TRUE, NULL, NULL, NULL)
```

## Risks / Trade-offs

- **[$1 \times 1$ Matrix Edge Case]** → Handled: Inner loop finds 0 neighbours (`neighbourSum = 0`), correctly requiring `A[0][0] == 0`.
- **[Time / Space Efficiency]** → $O(n^2)$ time with at most 4 additions per cell, $O(1)$ auxiliary memory.
