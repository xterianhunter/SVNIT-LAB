## Why

An element in an array of size $n$ is called a **dominant element** (or majority element) if it occurs strictly more than $\lfloor n/2 \rfloor$ times. To solve Problem 6 of DAA Lab Assignment 1 (CSDS103), we need to develop two distinct solutions to identify whether a dominant element exists:
1. **Approach 1 (Repeated Counting / Comparisons)**: Checks each element's count across the array ($O(n^2)$ time, $O(1)$ space).
2. **Approach 2 (Optimized: Boyer-Moore Voting Algorithm)**: Eliminates repeated work by pairing distinct elements ($O(n)$ time, $O(1)$ space).

We will compare their time and space complexities and demonstrate that the dominant element can indeed be identified without using any additional data structures or extra storage.

## What Changes

- Create `problem6_dominant_element.py` implementing both approaches (`find_dominant_brute_force` and `find_dominant_boyer_moore`).
- Support comma-separated integer input parsing (e.g. `"2, 2, 1, 2, 3, 2, 2"`).
- Add clear demonstration cases comparing both approaches side by side.
- Create automated unit tests in `test_problem6.py`.
- Create `problem6_analysis.md` documenting pseudocode, recurrence/complexity analysis, justification for why $O(1)$ auxiliary storage is sufficient, and comparison with frequency hashing.

## Capabilities

### New Capabilities
- `dominant-element`: Dual-approach detection of majority elements ($> \lfloor n/2 \rfloor$) in integer arrays with time and space complexity comparison.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New script `problem6_dominant_element.py`.
- **Tests**: `test_problem6.py` covering standard cases, no dominant element, single element, even/odd lengths, and negative integers.
- **Documentation**: `problem6_analysis.md` with complete analysis and comparison.
