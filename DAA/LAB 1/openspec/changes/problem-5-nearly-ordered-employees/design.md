## Context

See `proposal.md`. Problem 5 of DAA Lab Assignment 1 (CSDS103) requires analyzing an employee directory to:
1. Determine if it is already sorted without sorting the full array.
2. Identify all ordering violations ($A[i] > A[i+1]$).
3. Determine if swapping only two names can restore the sorted order, and if so, report the two positions $(x, y)$ and names.
4. State the conditions under which a single swap restores ordering.

## Goals / Non-Goals

**Goals:**
- Implement a clean, concise, and educational Python solution in `problem5_nearly_ordered_directory.py`.
- Run in $O(n \cdot L)$ linear time and $O(1)$ auxiliary memory.
- Identify all violations and candidate swap indices without sorting the whole list.
- Provide automated unit tests in `test_problem5_nearly_ordered.py`.
- Detail the theoretical conditions for single-swap restorability in `problem5_nearly_ordered_analysis.md`.

**Non-Goals:**
- Calling built-in sorting functions ($O(n \log n)$) to determine sortedness.

## Decisions

### 1. Algorithm: Inversion Detection & Swap Verification

```text
ALGORITHM AnalyzeNearlyOrderedDirectory(names):
    n ← Length(names)
    IF n <= 1 THEN
        RETURN (ALREADY_SORTED, [], NULL)

    violations ← []
    FOR i FROM 0 TO n - 2 DO:
        IF Compare(names[i], names[i+1]) > 0 THEN
            Append i to violations

    IF Length(violations) == 0 THEN
        RETURN (ALREADY_SORTED, [], NULL)

    IF Length(violations) == 1 THEN
        x ← violations[0]
        y ← violations[0] + 1
    ELSE IF Length(violations) == 2 THEN
        x ← violations[0]
        y ← violations[1] + 1
    ELSE
        RETURN (CANNOT_BE_SORTED_BY_ONE_SWAP, violations, NULL)

    // Verification by simulating the single swap
    Swap(names[x], names[y])
    isSorted ← TRUE
    FOR k FROM 0 TO n - 2 DO:
        IF Compare(names[k], names[k+1]) > 0 THEN
            isSorted ← FALSE
            BREAK
    Swap(names[x], names[y]) // Revert

    IF isSorted THEN
        RETURN (FIXABLE_BY_SWAP, violations, (x, y))
    ELSE
        RETURN (CANNOT_BE_SORTED_BY_ONE_SWAP, violations, NULL)
```

### 2. Conditions for Single Swap Restoration
A single swap of entries at indices $x < y$ can restore sorted order if and only if:
1. **At Most Two Inversion Drops**: The array has either 1 drop (adjacent swap where $y = x+1$) or 2 drops (non-adjacent swap where $y > x+1$).
2. **Boundary Bounds Satisfaction**:
   - $x == 0 \text{ or } A[x-1] \le A[y]$
   - $A[y] \le A[x+1]$ (for $x+1 < y$)
   - $A[y-1] \le A[x]$ (for $y-1 > x$)
   - $y == n-1 \text{ or } A[x] \le A[y+1]$
3. **Interior Monotonicity**: For all $x < k < y$, $A[y] \le A[k] \le A[x]$, and the intermediate subarray remains sorted.

## Risks / Trade-offs

- **[Duplicate Names Handling]** → The algorithm uses non-decreasing comparison ($\le$), safely supporting duplicate employee names.
