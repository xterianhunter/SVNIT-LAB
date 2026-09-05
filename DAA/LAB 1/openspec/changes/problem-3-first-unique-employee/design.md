## Context

See `proposal.md`. Problem 3 of DAA Lab Assignment 1 (CSDS103) requires designing two solutions to find the first unique employee in an access log sequence:
1. Solution 1 using only the given list and repeated comparisons ($O(n^2)$ time, $O(1)$ space).
2. Solution 2 using an additional data structure / frequency map ($O(n)$ time, $O(n)$ space).
We must compare both in terms of time complexity, auxiliary space, and suitability for large inputs.

## Goals / Non-Goals

**Goals:**
- Provide clean, simple, and instructive Python implementations of both algorithms in `problem3_first_unique_employee.py`.
- Handle user input (comma-separated strings) and demonstrate both algorithms side by side.
- Support boundary cases (all duplicates, all unique, single item, empty list).
- Document algorithmic pseudocode, complexity proofs, and comparative evaluation in `problem3_analysis.md`.

**Non-Goals:**
- Using black-box libraries that obscure algorithmic fundamentals.

## Decisions

### 1. Algorithm 1: In-Place Repeated Comparisons (`find_first_unique_brute_force`)
- Iterate $i$ from 0 to $n-1$.
- For each $i$, check if any other index $j \ne i$ has `names[j] == names[i]`.
- Return the first `names[i]` for which no other match exists.
- Return `None` if no unique element exists.

### 2. Algorithm 2: Frequency Map (`find_first_unique_hash_map`)
- Pass 1: Build a frequency dictionary `freq` mapping name $\rightarrow$ count.
- Pass 2: Iterate through the original list in access order; return the first name with `freq[name] == 1`.
- Return `None` if no unique element exists.

### 3. Pseudocode

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

ALGORITHM FindFirstUniqueHashMap(names):
    freq ← Empty Hash Map
    FOR EACH name IN names DO:
        freq[name] ← freq[name] + 1
    
    FOR EACH name IN names DO:
        IF freq[name] == 1 THEN
            RETURN name
    RETURN NULL
```

## Risks / Trade-offs

- **[Worst-case Hash Collisions]** → Mitigated by Python's built-in SipHash randomized dictionary with $O(1)$ amortized lookup.
- **[Memory Overhead of Hash Map]** → $O(u \cdot L)$ space is modest for standard modern RAM.
