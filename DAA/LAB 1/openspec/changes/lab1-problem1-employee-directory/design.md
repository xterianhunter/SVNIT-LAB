## Context

See `proposal.md` for background and motivation. This design addresses Problem 1 of DAA Lab Assignment 1 (CSDS103): Employee Directory. The program must accept comma-separated employee names from the user, arrange them in lexicographical order using a custom sorting algorithm (no built-in sorting allowed), report all duplicate names or confirm their absence, and provide comprehensive complexity and comparative analysis.

## Goals / Non-Goals

**Goals:**
- Implement a custom, comparison-based sorting algorithm from scratch (Merge Sort) tailored for string lists.
- Implement an explicit character-by-character string comparison function (`compare_strings`) defining standard ASCII lexicographical ordering.
- Implement an $O(n)$ single-pass duplicate detection algorithm on the sorted array.
- Parse comma-separated input with robust whitespace trimming and edge case handling (empty input, single element, all duplicates, all distinct).
- Document algorithm pseudocode, best/average/worst case time complexity, auxiliary space complexity, and a thorough comparative discussion of duplicate detection with vs. without sorting.

**Non-Goals:**
- Using built-in sorting utilities (such as Python's `sort()`, `sorted()`, or C++ `std::sort`).
- Using high-level collection counting functions (e.g. `collections.Counter`) for the core problem logic.

## Decisions

### 1. Algorithm Selection: Merge Sort
- **Choice**: Merge Sort (Divide and Conquer).
- **Rationale**:
  - Predictable $O(n \log n)$ time complexity across best, average, and worst cases.
  - Stable sort, well-suited for deterministic lexicographical ordering.
- **Alternative Considered**: Quick Sort ($O(n \log n)$ average, but $O(n^2)$ worst-case on already sorted or identical inputs unless randomized/median-of-three is applied) and Bubble/Insertion Sort ($O(n^2)$ time complexity).

### 2. Case Sensitivity and Character Comparison Definition
- **Choice**: Standard ASCII lexicographical comparison.
- **Rule**:
  - For strings $S_1$ and $S_2$, compare characters $S_1[i]$ and $S_2[i]$ using ordinal values `ord(c)`.
  - Uppercase characters (`'A'`–`'Z'`, ASCII 65–90) precede lowercase characters (`'a'`–`'z'`, ASCII 97–122).
  - If one string is a proper prefix of another, the shorter string precedes the longer string (e.g., `"Amit"` < `"Amita"`).
- **Alternative Considered**: Case-insensitive comparison (converting to lowercase). However, ASCII-based order preserves exact input identity and complies with standard DAA lexicographical definitions.

### 3. Duplicate Detection on Sorted Array
- **Choice**: Linear scan through the sorted list.
- **Mechanism**:
  - Consecutive identical names are grouped in a single pass ($O(n)$ time).
  - If a name appears at index $i$ and matches $i+1$, its frequency is tallied.
  - Names with frequency $\ge 2$ are printed with their count and position/summary.
  - If no duplicates are found, output `"No duplicate names exist."`

### 4. Duplicate Detection Without Sorting (Comparative Analysis)
- **Nested Loops (Brute Force)**:
  - Time: $O(n^2 \cdot L)$
  - Space: $O(1)$
  - Pros/Cons: Minimal space, but intractable for large $n$.
- **Hash Table / Frequency Map**:
  - Time: $O(n \cdot L)$ average
  - Space: $O(n \cdot L)$
  - Pros/Cons: Linear average time, but does not produce lexicographically sorted output; requires hash table overhead.
- **Trie (Prefix Tree)**:
  - Time: $O(n \cdot L)$
  - Space: $O(\Sigma \cdot n \cdot L)$
  - Pros/Cons: Can sort and count duplicates, but incurs significant pointer/memory overhead.

## Pseudocode

```text
ALGORITHM CustomCompare(s1, s2):
    len1 = Length(s1), len2 = Length(s2)
    minLen = Min(len1, len2)
    FOR i FROM 0 TO minLen - 1 DO:
        IF ASCII(s1[i]) < ASCII(s2[i]) THEN RETURN -1
        IF ASCII(s1[i]) > ASCII(s2[i]) THEN RETURN 1
    IF len1 < len2 THEN RETURN -1
    IF len1 > len2 THEN RETURN 1
    RETURN 0

ALGORITHM MergeSort(arr):
    IF Length(arr) <= 1 THEN RETURN arr
    mid = Length(arr) // 2
    left = MergeSort(arr[0 ... mid - 1])
    right = MergeSort(arr[mid ... Length(arr) - 1])
    RETURN Merge(left, right)

ALGORITHM Merge(left, right):
    result = []
    i = 0, j = 0
    WHILE i < Length(left) AND j < Length(right) DO:
        IF CustomCompare(left[i], right[j]) <= 0 THEN
            Append left[i] to result; i = i + 1
        ELSE
            Append right[j] to result; j = j + 1
    Append remaining elements of left and right to result
    RETURN result

ALGORITHM FindDuplicatesInSorted(sortedArr):
    duplicates = []
    n = Length(sortedArr)
    i = 0
    WHILE i < n DO:
        count = 1
        WHILE i + 1 < n AND CustomCompare(sortedArr[i], sortedArr[i + 1]) == 0 DO:
            count = count + 1
            i = i + 1
        IF count > 1 THEN
            Append (sortedArr[i], count) to duplicates
        i = i + 1
    RETURN duplicates
```

## Risks / Trade-offs

- **[Memory allocation during Merge Sort]** → Mitigation: List slicing in Python allocates new sub-arrays; for $n$ employee names, $O(n)$ space is well within memory constraints.
- **[Empty or whitespace-only inputs]** → Mitigation: Clean input parsing with strip and filter removes empty token anomalies.
