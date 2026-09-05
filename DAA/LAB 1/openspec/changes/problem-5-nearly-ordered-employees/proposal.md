## Why

An employee directory containing $n$ names is expected to be in lexicographical order, but due to a data-entry error, some names may have been placed incorrectly. To solve Problem 5 of DAA Lab Assignment 1 (CSDS103), we need an algorithm to:
1. Determine whether the list is already sorted without sorting the complete array.
2. Identify all positions where the lexicographical ordering is violated ($A[i] > A[i+1]$).
3. Determine whether exchanging only two names can restore the sorted ordering.
4. If possible, report the two positions and names to be swapped; otherwise, report that a single swap is insufficient.
5. State the exact mathematical and algorithmic conditions under which a single swap can restore the sorted order.

## What Changes

- Create `problem5_nearly_ordered_directory.py` to check sortedness, record ordering violations, identify swap candidates, and verify single-swap fixability in $O(n)$ linear time and $O(1)$ auxiliary space.
- Implement two-tier lexicographical comparison without calling built-in sort functions.
- Support comma-separated user inputs and demonstration test cases from the lab PDF.
- Create automated unit tests in `test_problem5_nearly_ordered.py`.
- Create `problem5_nearly_ordered_analysis.md` documenting pseudocode, complexity proofs ($O(n \cdot L)$ time, $O(1)$ space), and conditions under which a single swap restores ordering.

## Capabilities

### New Capabilities
- `nearly-ordered-directory`: Linear-time sortedness verification, inversion violation detection, single-swap candidate identification, and swap fixability validation.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New script `problem5_nearly_ordered_directory.py`.
- **Tests**: `test_problem5_nearly_ordered.py` covering already sorted, adjacent swap, non-adjacent swap, multi-violation unfixable, and boundary lists.
- **Documentation**: `problem5_nearly_ordered_analysis.md` detailing algorithm, complexity, and exact swap restoration conditions.
