## Context

See `proposal.md`. Problem 6 of DAA Lab Assignment 1 (CSDS103) requires determining whether an integer array of size $n$ has a dominant element (occurring $> \lfloor n/2 \rfloor$ times).
We must design two solutions:
1. Solution 1 based on repeated counting/comparisons ($O(n^2)$ time, $O(1)$ space).
2. Solution 2 that reduces repeated work (Boyer-Moore Voting Algorithm, $O(n)$ time, $O(1)$ space).
We will compare their complexities and determine whether additional storage is necessary.

## Goals / Non-Goals

**Goals:**
- Provide a clean, short, and simple Python implementation (`problem6_dominant_element.py`).
- Implement both algorithms clearly and verify their equivalence.
- Prove that $O(1)$ auxiliary space is sufficient to achieve $O(n)$ time.
- Provide automated unit tests in `test_problem6.py`.
- Provide a comprehensive analysis report in `problem6_analysis.md`.

**Non-Goals:**
- Using black-box counter libraries (`collections.Counter`) for the core algorithmic steps.

## Decisions

### 1. Algorithm 1: Repeated Counting (`find_dominant_brute_force`)

```text
ALGORITHM FindDominantBruteForce(arr):
    n ← Length(arr)
    threshold ← Floor(n / 2)
    
    FOR i FROM 0 TO n - 1 DO:
        count ← 0
        FOR j FROM 0 TO n - 1 DO:
            IF arr[j] == arr[i] THEN
                count ← count + 1
        IF count > threshold THEN
            RETURN (arr[i], count)
            
    RETURN NULL
```

### 2. Algorithm 2: Boyer-Moore Voting Algorithm (`find_dominant_boyer_moore`)

```text
ALGORITHM FindDominantBoyerMoore(arr):
    n ← Length(arr)
    IF n == 0 THEN
        RETURN NULL
        
    // Phase 1: Candidate Selection
    candidate ← NULL
    count ← 0
    FOR EACH num IN arr DO:
        IF count == 0 THEN
            candidate ← num
            count ← 1
        ELSE IF num == candidate THEN
            count ← count + 1
        ELSE
            count ← count - 1
            
    // Phase 2: Candidate Verification
    actualCount ← 0
    FOR EACH num IN arr DO:
        IF num == candidate THEN
            actualCount ← actualCount + 1
            
    IF actualCount > Floor(n / 2) THEN
        RETURN (candidate, actualCount)
    ELSE
        RETURN NULL
```

## Risks / Trade-offs

- **[Unverified Candidate in Boyer-Moore]** → Boyer-Moore Phase 1 only identifies a potential majority element. If no majority exists, Phase 1 still outputs a candidate. Thus, Phase 2 verification is **strictly mandatory** to guarantee correctness.
- **[Auxiliary Storage]** → Both algorithms use $O(1)$ scalar variables, proving no additional arrays or hash maps are required.
