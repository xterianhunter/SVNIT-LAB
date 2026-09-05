# Problem 5: Nearly Ordered Employee Directory – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

An employee directory containing $n$ names is expected to be in non-decreasing lexicographical order. Due to data-entry errors, some names may be out of order.

Given the list:
1. **Determine whether it is already sorted** without sorting the complete array.
2. **Identify the positions where the ordering is violated** ($A[i] > A[i+1]$).
3. **Determine whether exchanging only two names can make the complete list sorted**.
4. **If possible, report the two positions** and names to be swapped; otherwise, report that a single swap is insufficient.
5. **State the conditions** under which a single swap can restore the sorted ordering.

---

## 2. Algorithm & Pseudocode

```text
ALGORITHM AnalyzeNearlyOrderedDirectory(names):
    n ← Length(names)
    IF n <= 1 THEN
        RETURN (ALREADY_SORTED, [], NULL)

    violations ← []
    // Step 1: Detect all adjacent drops in a single linear pass
    FOR i FROM 0 TO n - 2 DO:
        IF CompareStrings(names[i], names[i+1]) > 0 THEN
            Append i to violations

    IF Length(violations) == 0 THEN
        RETURN (ALREADY_SORTED, [], NULL)

    // Step 2: Identify candidate swap positions
    IF Length(violations) == 1 THEN
        x ← violations[0]
        y ← violations[0] + 1
    ELSE IF Length(violations) == 2 THEN
        x ← violations[0]
        y ← violations[1] + 1
    ELSE
        // More than 2 drops cannot be resolved by a single swap
        RETURN (CANNOT_BE_SORTED_BY_ONE_SWAP, violations, NULL)

    // Step 3: Verify whether swapping names[x] and names[y] makes list sorted
    Swap(names[x], names[y])
    isSorted ← TRUE
    FOR k FROM 0 TO n - 2 DO:
        IF CompareStrings(names[k], names[k+1]) > 0 THEN
            isSorted ← FALSE
            BREAK
    Swap(names[x], names[y]) // Restore original order

    IF isSorted THEN
        RETURN (FIXABLE_BY_SWAP, violations, (x, y))
    ELSE
        RETURN (CANNOT_BE_SORTED_BY_ONE_SWAP, violations, NULL)
```

---

## 3. Complexity Analysis

### 3.1 Time Complexity

Let $n$ be the number of employee names and $L$ be the maximum string length:
- **Violation Detection Pass**: Evaluates $n - 1$ adjacent pairs: $(n - 1) \times O(L) = O(n \cdot L)$.
- **Candidate Deduction**: $O(1)$ constant time logic based on the size of the violations list.
- **Verification Pass**: Evaluates $n - 1$ adjacent pairs on the simulated swap: $(n - 1) \times O(L) = O(n \cdot L)$.
- **Total Time Complexity**:
  - **Best-Case Time Complexity**: $O(n \cdot L)$ — when already sorted (only 1 pass needed).
  - **Worst-Case Time Complexity**: $O(n \cdot L)$ — when swap candidate is verified (2 linear passes).
  - **Average-Case Time Complexity**: $O(n \cdot L)$.

$$\mathbf{T(n) = O(n \cdot L)}$$

*(Contrast this with sorting the entire array, which would require $O(n \log n \cdot L)$ time).*

### 3.2 Auxiliary Space Complexity

- **No Additional Sorting Buffers**: The check is performed using index pointers and scalar variables (`i`, `x`, `y`, `isSorted`).
- **Violation Tracking**: Holds at most a small list of indices (at most $O(1)$ space for candidates).
- **Auxiliary Space**:
  $$\mathbf{S(n) = O(1)}$$

---

## 4. Conditions Under Which a Single Swap Restores Ordering

Let an array $A$ of size $n$ be obtained by swapping two elements at indices $x < y$ in a sorted array $S$. A single swap can restore the sorted ordering if and only if **all** of the following conditions hold:

### 1. Inversion Drop Count ($1 \le |\text{Violations}| \le 2$)
- **Adjacent Swap ($y = x + 1$)**: Produces **exactly 1 drop** at index $x$ ($A[x] > A[x+1]$).
- **Non-Adjacent Swap ($y > x + 1$)**: Produces **exactly 2 drops**:
  - First drop at index $x$ where $A[x] > A[x+1]$
  - Second drop at index $y - 1$ where $A[y-1] > A[y]$
- If there are $> 2$ drops, exchanging a single pair can never restore order.

### 2. Boundary Compatibility Conditions
After placing $A[y]$ into position $x$ and $A[x]$ into position $y$:
1. $x == 0 \quad \text{or} \quad A[x-1] \le A[y]$ (Left boundary of $x$)
2. $A[y] \le A[x+1] \quad (\text{if } x + 1 < y)$ (Right boundary of $x$)
3. $A[y-1] \le A[x] \quad (\text{if } y - 1 > x)$ (Left boundary of $y$)
4. $y == n - 1 \quad \text{or} \quad A[x] \le A[y+1]$ (Right boundary of $y$)

### 3. Intermediate Monotonicity
For any intermediate elements $k$ strictly between $x$ and $y$ ($x < k < y$):
$$A[y] \le A[k] \le A[x]$$
and all elements in subarray $A[x+1 \dots y-1]$ must already be sorted among themselves.

---

## 5. Representative Test Cases

### Test Case 1: Already Sorted
- **Input**: `Amit, Karan, Neha, Priya, Rahul`
- **Output**: `Already Sorted [✓]` (0 violations).

### Test Case 2: Fixable by Adjacent Swap
- **Input**: `Amit, Karan, Neha, Rahul, Priya`
- **Analysis**:
  - Violation at index 3 (`Rahul` > `Priya`).
  - Swapping position 4 (`Rahul`) and position 5 (`Priya`) gives `Amit, Karan, Neha, Priya, Rahul`.
- **Output**: `Single-Swap Restoration: POSSIBLE [✓]`, Swap positions `(4, 5)`.

### Test Case 3: Fixable by Non-Adjacent Swap
- **Input**: `Rahul, Karan, Neha, Priya, Amit`
- **Analysis**:
  - Violation 1 at index 0 (`Rahul` > `Karan`).
  - Violation 2 at index 3 (`Priya` > `Amit`).
  - Candidate swap: index 0 (`Rahul`) and index 4 (`Amit`).
- **Output**: `Single-Swap Restoration: POSSIBLE [✓]`, Swap positions `(1, 5)`.

### Test Case 4: Multiple Independent Violations (Unfixable by Single Swap)
- **Input**: `Amit, Neha, Karan, Rahul, Priya`
- **Analysis**:
  - Violation 1 at index 1 (`Neha` > `Karan`).
  - Violation 2 at index 3 (`Rahul` > `Priya`).
  - These represent two distinct misordered pairs. A single swap cannot fix both.
- **Output**: `Single-Swap Restoration: NOT POSSIBLE [✗]`.
