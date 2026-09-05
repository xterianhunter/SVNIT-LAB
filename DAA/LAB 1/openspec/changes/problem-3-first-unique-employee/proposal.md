## Why

A system records a sequence of $n$ employee access names. An employee is unique if their name occurs exactly once in the entire sequence. To solve Problem 3 of DAA Lab Assignment 1 (CSDS103), we need clean, simple, and instructive algorithms to find the first unique employee using two distinct approaches:
1. **Approach 1 (Repeated Comparisons / In-place)**: Uses only the given list with repeated pairwise comparisons ($O(n^2)$ time, $O(1)$ auxiliary space).
2. **Approach 2 (Additional Data Structure / Frequency Map)**: Uses an auxiliary hash table/frequency map to achieve linear time ($O(n)$ time, $O(n)$ auxiliary space).

We will provide full implementations of both approaches, comparative evaluation for large inputs, edge case handling, and educational CLI output.

## What Changes

- Create `problem3_first_unique_employee.py` implementing both approaches (`find_first_unique_brute_force` and `find_first_unique_hash_map`).
- Support comma-separated user input parsing (e.g. `"Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"`).
- Add clear demonstration cases comparing the two approaches on identical inputs.
- Create unit tests in `test_problem3.py` covering boundary cases (no unique employee, all unique, single name, empty list).
- Create `problem3_analysis.md` comparing time complexity, auxiliary space, and suitability for large inputs.

## Capabilities

### New Capabilities
- `first-unique-employee`: Dual-approach identification of the first unique employee in an access log sequence with time/space complexity comparison.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New script `problem3_first_unique_employee.py`.
- **Tests**: `test_problem3.py` testing both algorithms.
- **Documentation**: `problem3_analysis.md` with pseudocode, recurrence/complexity analysis, and approach comparison.
