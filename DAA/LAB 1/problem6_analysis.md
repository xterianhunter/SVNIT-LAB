# Problem 6: Dominant Element – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

Given an integer array $A$ of size $n$, determine whether there exists a **dominant element** (majority element) that occurs strictly more than half of the time, i.e.:

$$\text{Count}(x) > \lfloor n / 2 \rfloor$$

### Objectives:
1. Develop two different solutions:
   - **Approach 1**: Based on repeated counting/comparison ($O(n^2)$ time, $O(1)$ space).
   - **Approach 2**: An optimized approach that eliminates repeated work (**Boyer-Moore Majority Voting Algorithm**, $O(n)$ time, $O(1)$ space).
2. Compare their time and space complexities.
3. Determine and justify whether the dominant element can be identified **without using additional storage**.

---

## 2. Approach 1: Repeated Counting / Comparisons (Brute Force)

### 2.1 Description
Iterate through the array. For each element $A[i]$, count its frequency across the entire array $A$ using an inner loop. If the count exceeds $\lfloor n/2 \rfloor$, return $A[i]$ immediately.

### 2.2 Pseudocode
```text
ALGORITHM FindDominantBruteForce(A, n):
    threshold ← Floor(n / 2)
    
    FOR i FROM 0 TO n - 1 DO:
        count ← 0
        FOR j FROM 0 TO n - 1 DO:
            IF A[j] == A[i] THEN
                count ← count + 1
        
        IF count > threshold THEN
            RETURN (A[i], count)
            
    RETURN NULL
```

### 2.3 Complexity Analysis
- **Best-Case Time Complexity**: $O(n)$ — occurs when the first element $A[0]$ is the dominant element and is verified in the first inner loop pass.
- **Worst-Case Time Complexity**: $O(n^2)$ — occurs when no dominant element exists, or the dominant element is tested last.
- **Average-Case Time Complexity**: $O(n^2)$.
- **Auxiliary Space Complexity**: $O(1)$ scalar variables (`i`, `j`, `count`, `threshold`).

---

## 3. Approach 2: Boyer-Moore Majority Voting Algorithm (Optimized)

### 3.1 Description
The Boyer-Moore algorithm exploits the property that pairing and eliminating distinct elements guarantees that if a dominant element exists ($> n/2$ occurrences), it will survive as the candidate.
1. **Phase 1 (Candidate Selection)**:
   Maintain a `candidate` and a `count`.
   - If `count == 0`: set `candidate = A[i]` and `count = 1`.
   - If $A[i] == \text{candidate}$: increment `count`.
   - Otherwise: decrement `count` (pairing distinct elements).
2. **Phase 2 (Candidate Verification)**:
   Perform a single linear pass to count the exact occurrences of `candidate`. If `actual_count > n // 2`, return `(candidate, actual_count)`; otherwise, return `NULL`.

### 3.2 Pseudocode
```text
ALGORITHM FindDominantBoyerMoore(A, n):
    IF n == 0 THEN
        RETURN NULL

    // Phase 1: Candidate Selection
    candidate ← NULL
    count ← 0
    FOR EACH x IN A DO:
        IF count == 0 THEN
            candidate ← x
            count ← 1
        ELSE IF x == candidate THEN
            count ← count + 1
        ELSE
            count ← count - 1

    // Phase 2: Mandatory Verification
    actualCount ← 0
    FOR EACH x IN A DO:
        IF x == candidate THEN
            actualCount ← actualCount + 1

    IF actualCount > Floor(n / 2) THEN
        RETURN (candidate, actualCount)
    ELSE
        RETURN NULL
```

### 3.3 Complexity Analysis
- **Phase 1 Time**: Exactly $n$ element inspections $\rightarrow \Theta(n)$.
- **Phase 2 Time**: Exactly $n$ element comparisons $\rightarrow \Theta(n)$.
- **Total Time Complexity**: $\Theta(n)$ in all cases (Best, Worst, Average).
- **Auxiliary Space Complexity**: $O(1)$ — requires only two scalar variables (`candidate` and `count`).

---

## 4. Complexity Comparison

| Metric | Approach 1 (Repeated Counting) | Approach 2 (Boyer-Moore Voting) | Hash Table Approach |
| :--- | :--- | :--- | :--- |
| **Best-Case Time** | $O(n)$ | $\mathbf{O(n)}$ | $O(n)$ |
| **Average-Case Time** | $O(n^2)$ | $\mathbf{O(n)}$ | $O(n)$ |
| **Worst-Case Time** | $O(n^2)$ | $\mathbf{O(n)}$ | $O(n)$ (or $O(n^2)$ hash collision) |
| **Auxiliary Space** | **$O(1)$** | **$O(1)$** | $O(u) \le O(n)$ (Frequency Map) |
| **In-Place Execution?** | Yes | **Yes** | No (allocates hash table) |
| **Suitability for Large $n$** | Intractable for $n \ge 10^5$ | **Highly Optimal** | Good, but incurs memory overhead |

---

## 5. Can the Dominant Element Be Identified Without Additional Storage?

### **YES, absolutely.**

### Theoretical Justification:
1. **Space Bounds**: The Boyer-Moore algorithm requires strictly **$O(1)$ auxiliary storage**, allocating only two scalar registers (`candidate` and `count`).
2. **No Array Sorting or Mutation**: Unlike sorting-based approaches (which require $O(n \log n)$ time or in-place array modifications), Boyer-Moore leaves the input array completely unmodified.
3. **No Hash Table Overhead**: While a frequency map achieves $O(n)$ time, it consumes $O(n)$ extra memory. Boyer-Moore eliminates all memory overhead while preserving the optimal $O(n)$ time bound.

---

## 6. Representative Test Cases

### Test Case 1: Lab Sheet Example
- **Input**: `2, 2, 1, 2, 3, 2, 2` ($n=7$, threshold $= 3$)
- **Output**: Dominant Element = `2` (Count: 5 > 3)

### Test Case 2: No Dominant Element
- **Input**: `1, 2, 3, 4, 2, 2` ($n=6$, threshold $= 3$)
- **Analysis**: Element `2` occurs 3 times ($3 \ngtr 3$).
- **Output**: `No dominant element exists.`

### Test Case 3: All Elements Identical
- **Input**: `7, 7, 7, 7` ($n=4$, threshold $= 2$)
- **Output**: Dominant Element = `7` (Count: 4 > 2)

### Test Case 4: Single-Element Array
- **Input**: `[42]` ($n=1$, threshold $= 0$)
- **Output**: Dominant Element = `42` (Count: 1 > 0)

### Test Case 5: Negative Integers
- **Input**: `-5, -5, 2, -5` ($n=4$, threshold $= 2$)
- **Output**: Dominant Element = `-5` (Count: 3 > 2)
