# Problem 4: Stable Matrix – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

Given an $n \times n$ integer matrix $A$, a matrix is called **stable** if every non-boundary (interior) element equals the sum of its four orthogonal neighbours (up, down, left, right):

$$A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1] \quad \text{for } 1 \le i, j \le n-2$$

If the matrix is not stable, the algorithm must:
1. Report the **number of violating elements**.
2. Report the **exact coordinate positions $(i, j)$** of all violating elements.
3. Identify the position with the **maximum absolute difference** between the element and its neighbour sum:
   $$D(i, j) = |A[i][j] - (A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1])|$$

---

## 2. Algorithm & Pseudocode

```text
ALGORITHM CheckMatrixStability(A, n):
    // Matrices of size n < 3 have no interior elements
    IF n < 3 THEN
        RETURN (TRUE, 0, [], NULL)

    violatingPositions ← []
    maxDiff ← -1
    maxDiffInfo ← NULL

    // Traverse all non-boundary elements
    FOR i FROM 1 TO n - 2 DO:
        FOR j FROM 1 TO n - 2 DO:
            neighbourSum ← A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]
            diff ← Abs(A[i][j] - neighbourSum)
            
            IF diff > 0 THEN
                Append (i, j) to violatingPositions
                IF diff > maxDiff THEN
                    maxDiff ← diff
                    maxDiffInfo ← ((i, j), A[i][j], neighbourSum, diff)

    IF Length(violatingPositions) == 0 THEN
        RETURN (TRUE, 0, [], NULL)
    ELSE
        RETURN (FALSE, Length(violatingPositions), violatingPositions, maxDiffInfo)
```

---

## 3. Complexity Analysis

### 3.1 Time Complexity

- **Number of Evaluated Elements**: There are $(n - 2)^2$ non-boundary interior elements.
- **Operations per Element**: 3 additions, 1 subtraction, 1 absolute value calculation, and 1 comparison ($O(1)$ constant time per element).
- **Best-Case Time Complexity**: $\Theta((n - 2)^2) = \mathbf{\Theta(n^2)}$
  - Even if the matrix is completely stable, every single interior element must be examined to verify that no violation exists.
- **Worst-Case Time Complexity**: $\Theta((n - 2)^2) = \mathbf{\Theta(n^2)}$
  - Even when multiple violations exist, all elements must still be examined to find the absolute maximum difference across the entire matrix.
- **Average-Case Time Complexity**: $\mathbf{\Theta(n^2)}$.

$$\mathbf{T(n) = \Theta(n^2)}$$

### 3.2 Auxiliary Space Complexity

- **Scalar Tracking Variables**: Variables `i`, `j`, `neighbourSum`, `diff`, and `maxDiff` require $O(1)$ memory.
- **Output Storage**: Storing the positions of $k$ violations requires $O(k)$ space where $k \le (n-2)^2$.
- **Total Auxiliary Space**:
  $$\mathbf{S(n) = O(1)} \quad (\text{ignoring output report array})$$

---

## 4. Is an Additional Matrix Required?

**No, an additional matrix is NOT required.**

### Justification:
1. **Read-Only Operations**: Checking stability requires only reading the values of $A[i-1][j], A[i+1][j], A[i][j-1], A[i][j+1]$ and comparing with $A[i][j]$.
2. **No In-Place Mutation Conflicts**: Because the matrix values are never updated during the calculation, calculating the difference for $(i, j)$ does not alter the neighbour values needed for subsequent elements like $(i, j+1)$ or $(i+1, j)$.
3. **Memory Optimization**: Storing differences in a separate $n \times n$ matrix would consume unnecessary $O(n^2)$ space. By maintaining a single running maximum difference scalar variable, we achieve $O(1)$ auxiliary space.

---

## 5. Representative Test Cases

### Test Case 1: Stable $3 \times 3$ Matrix
- **Matrix**:
  ```text
  6   1   8
  5  15   7
  7   2  10
  ```
- **Evaluation**: Non-boundary cell $(1, 1)$: $A[1][1] = 15$, Neighbours $= 1 + 2 + 5 + 7 = 15$.
- **Output**: `Stability Status: STABLE [✓]`

### Test Case 2: Unstable $3 \times 3$ Matrix
- **Matrix**:
  ```text
  1  2  3
  4  5  6
  7  8  9
  ```
- **Evaluation**: Non-boundary cell $(1, 1)$: $A[1][1] = 5$, Neighbours $= 2 + 8 + 4 + 6 = 20$. Difference $= |5 - 20| = 15$.
- **Output**:
  - `Stability Status: NOT STABLE [✗]`
  - `Total Violating Elements: 1`
  - `Violating Positions: [(1, 1)]`
  - `Max Difference at (1, 1): Value = 5, Neighbour Sum = 20, Max |Diff| = 15`

### Test Case 3: $4 \times 4$ Matrix with Multiple Violations
- **Matrix**:
  ```text
   1   2   3   4
   5  20  10   6
   7   8  40   9
   1   2   3   4
  ```
- **Output**:
  - `Total Violating Elements: 4`
  - `Violating Positions: [(1, 1), (1, 2), (2, 1), (2, 2)]`
  - `Max Difference at (2, 1): Value = 8, Neighbour Sum = 69, Max |Diff| = 61`
