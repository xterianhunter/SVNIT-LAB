# Problem 2: Locally Balanced Matrix – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

An $n \times n$ integer matrix $A$ is defined as **locally balanced** if every non-boundary element (where all 4 neighbours: up, down, left, right are present and valid) equals the sum of its four orthogonal neighbours:

$$A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1] \quad \text{for } 1 \le i, j \le n-2$$

Boundary elements (row $0$, row $n-1$, column $0$, column $n-1$) are excluded from evaluation as they do not possess all four orthogonal neighbours.

If the matrix is not balanced, the algorithm reports the **first violating element in row-major order** along with its position $(i, j)$, its value $A[i][j]$, and its calculated 4-neighbour sum.

---

## 2. Algorithm & Pseudocode

```text
ALGORITHM IsLocallyBalanced(A, n):
    // Matrices of size n < 3 have no interior elements where all 4 neighbours exist
    IF n < 3 THEN
        RETURN (TRUE, NULL, NULL, NULL)

    // Check all non-boundary elements (1 <= i <= n-2, 1 <= j <= n-2)
    FOR i FROM 1 TO n - 2 DO:
        FOR j FROM 1 TO n - 2 DO:
            neighbourSum ← A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]
            
            // Check balance condition
            IF A[i][j] != neighbourSum THEN
                RETURN (FALSE, (i, j), A[i][j], neighbourSum)

    RETURN (TRUE, NULL, NULL, NULL)
```

---

## 3. Element Classification & Boundary Handling

| Element Type | Number of Valid Neighbours | Positions | Handled in Balance Check? | Reason |
| :--- | :---: | :--- | :---: | :--- |
| **Corner Elements** | **2** | $(0,0), (0,n-1), (n-1,0), (n-1,n-1)$ | **Ignored** | Lacks full set of 4 orthogonal neighbours |
| **Boundary Elements (Edge)** | **3** | Non-corner elements in row $0, n-1$ and col $0, n-1$ | **Ignored** | Lacks full set of 4 orthogonal neighbours |
| **Interior (Non-Boundary) Elements** | **4** | $1 \le i \le n-2, \quad 1 \le j \le n-2$ | **Evaluated** | All 4 orthogonal neighbours (Up, Down, Left, Right) exist |
| **Small Matrices ($n < 3$)** | **$<4$** | All elements | **Vacuously Balanced** | No elements satisfy the 4-neighbour condition |

---

## 4. Complexity Analysis

### 4.1 Time Complexity

- **Number of Evaluated Elements**: Exactly $(n - 2)^2$ interior elements.
- **Operations per Element**: 3 additions and 1 comparison ($O(1)$ constant time).
- **Row-Major Traversal**:
  - **Best-Case Time Complexity**: $O(1)$ — when the first non-boundary element $(1, 1)$ violates the condition.
  - **Worst-Case Time Complexity**: $O(n^2)$ — when the matrix is locally balanced, or the first violation occurs at the final interior element $(n-2, n-2)$.
  - **Average-Case Time Complexity**: $O(n^2)$.

$$\mathbf{T(n) = O(n^2)}$$

### 4.2 Auxiliary Space Complexity

- **No Additional Matrix**: The check is performed directly on the input matrix $A$ in place.
- **Auxiliary Space**: $O(1)$ scalar variables (`i`, `j`, `neighbourSum`).

$$\mathbf{S(n) = O(1)}$$

---

## 5. Representative Test Cases

### Test Case 1: Balanced $3 \times 3$ Matrix
- **Matrix**:
  ```text
  6   1   8
  5  15   7
  7   2  10
  ```
- **Evaluation**:
  - Center element $(1, 1)$: $A[1][1] = 15$
  - 4-Neighbour Sum: $A[0][1](1) + A[2][1](2) + A[1][0](5) + A[1][2](7) = 15$
  - $15 == 15 \rightarrow$ **Locally Balanced Matrix [✓]**

### Test Case 2: Unbalanced $3 \times 3$ Matrix
- **Matrix**:
  ```text
  1  2  3
  4  5  6
  7  8  9
  ```
- **Evaluation**:
  - Center element $(1, 1)$: $A[1][1] = 5$
  - 4-Neighbour Sum: $A[0][1](2) + A[2][1](8) + A[1][0](4) + A[1][2](6) = 20$
  - $5 \ne 20 \rightarrow$ **NOT Balanced [✗]**
  - First Violation at $(1, 1)$, Value $= 5$, Neighbour Sum $= 20$.
