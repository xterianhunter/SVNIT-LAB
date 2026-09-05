# Problem 3: First Unique Employee – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

A company records the access sequence of $n$ employee names. An employee is considered **unique** if their name occurs **exactly once** in the complete sequence.

Given a sequence of $n$ employee names, design and compare two solutions to identify the **first unique employee**:
1. **Approach 1**: Uses only the given list and repeated comparisons (in-place).
2. **Approach 2**: Uses an additional data structure (frequency hash map).

Compare the two approaches in terms of time complexity, auxiliary space, and suitability for large input sequences.

---

## 2. Approach 1: Repeated Pairwise Comparisons (In-Place)

### 2.1 Description
Iterate through the array element-by-element. For each element at index $i$, scan the entire list to check if another index $j \ne i$ contains the identical name. The first element that has no duplicate anywhere else is returned immediately.

### 2.2 Pseudocode
```text
ALGORITHM FindFirstUniqueBruteForce(names):
    n ← Length(names)
    
    FOR i FROM 0 TO n - 1 DO:
        isUnique ← TRUE
        FOR j FROM 0 TO n - 1 DO:
            IF i != j AND names[i] == names[j] THEN
                isUnique ← FALSE
                BREAK
        
        IF isUnique THEN
            RETURN names[i]
            
    RETURN NULL
```

### 2.3 Complexity Analysis
- **Best-Case Time Complexity**: $O(n \cdot L)$ — occurs when the very first element `names[0]` is unique (scans $n-1$ elements once).
- **Worst-Case Time Complexity**: $O(n^2 \cdot L)$ — occurs when no unique employee exists, or the only unique employee is at the last position `names[n-1]`.
- **Average-Case Time Complexity**: $O(n^2 \cdot L)$.
- **Auxiliary Space Complexity**: $O(1)$ — requires no auxiliary arrays or data structures.

---

## 3. Approach 2: Additional Data Structure (Frequency Hash Map)

### 3.1 Description
Utilize a two-pass algorithm:
1. **Pass 1 (Counting)**: Traverse the sequence and store frequency counts of each distinct employee name in a hash table.
2. **Pass 2 (Lookup)**: Traverse the original sequence in its original access order and query the hash table. The first element with `freq[name] == 1` is returned.

### 3.2 Pseudocode
```text
ALGORITHM FindFirstUniqueHashMap(names):
    freq ← Empty Hash Table
    
    // Pass 1: Build frequency map
    FOR EACH name IN names DO:
        IF name NOT IN freq THEN
            freq[name] ← 0
        freq[name] ← freq[name] + 1
    
    // Pass 2: Find first unique in original order
    FOR EACH name IN names DO:
        IF freq[name] == 1 THEN
            RETURN name
            
    RETURN NULL
```

### 3.3 Complexity Analysis
- **Best-Case Time Complexity**: $O(n \cdot L)$ — building the map takes $O(n \cdot L)$ time, and the lookup finds the first element in $O(L)$ time.
- **Worst-Case Time Complexity**: $O(n \cdot L)$ average (or $O(n^2 \cdot L)$ in the theoretical worst-case of catastrophic hash collisions).
- **Average-Case Time Complexity**: $O(n \cdot L)$ linear time.
- **Auxiliary Space Complexity**: $O(u \cdot L)$ where $u$ is the number of distinct employee names ($u \le n$).

---

## 4. Comparison of Approaches

| Metric | Approach 1 (Repeated Comparisons) | Approach 2 (Frequency Map) |
| :--- | :--- | :--- |
| **Best-Case Time** | $O(n \cdot L)$ | $O(n \cdot L)$ |
| **Average-Case Time** | $O(n^2 \cdot L)$ | $O(n \cdot L)$ |
| **Worst-Case Time** | $O(n^2 \cdot L)$ | $O(n \cdot L)$ |
| **Auxiliary Space** | **$O(1)$** (Zero extra memory) | **$O(u \cdot L)$** ($u \le n$) |
| **Data Structure Used** | None (in-place list traversal) | Hash Table / Dictionary |
| **Number of Passes** | Up to $n$ scans | Exactly 2 linear passes |
| **Suitability for Large $n$ ($n \ge 10^5$)** | **Unsuitable** ($\approx 10^{10}$ comparisons) | **Highly Suitable** ($\approx 2 \times 10^5$ operations) |
| **Suitability for Embedded / Low-RAM** | **Highly Suitable** (no memory allocation) | Unsuitable if memory is tightly constrained |

### 4.1 Suitability for Large Input
- For small sequences ($n \le 50$), Approach 1 is simple and introduces no hashing overhead.
- For enterprise-scale access logs ($n \ge 10^5$), Approach 1 becomes computationally intractable ($O(n^2)$ takes hours), whereas Approach 2 finishes in a few milliseconds ($O(n)$ linear time).
- **Verdict**: **Approach 2 (Frequency Map)** is superior and strongly recommended for production systems and large datasets.

---

## 5. Representative Test Cases

### Test Case 1: Lab Sheet Example
- **Input**: `Amit, Neha, Amit, Rahul, Neha, Karan, Rahul`
- **Output**: `Karan`

### Test Case 2: No Unique Employee
- **Input**: `Amit, Neha, Amit, Neha`
- **Output**: `No unique employee found.`

### Test Case 3: All Unique Employees
- **Input**: `Amit, Neha, Karan, Rahul`
- **Output**: `Amit` (first in sequence order)

### Test Case 4: Unique Employee at the End
- **Input**: `A, B, A, B, C`
- **Output**: `C`

### Test Case 5: Single Employee Access
- **Input**: `Karan`
- **Output**: `Karan`
