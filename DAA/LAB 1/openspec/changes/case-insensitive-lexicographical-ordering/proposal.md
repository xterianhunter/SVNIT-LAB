## Why

In natural dictionary / lexicographical ordering for employee directories, names should be arranged alphabetically by letters regardless of case (i.e. 'A'/'a' before 'B'/'b' ... before 'N'/'n' ... before 'R'/'r'), rather than grouping all uppercase names before all lowercase names as in raw ASCII ordering. For an input like `['amit', 'Amit', 'rahul', 'Neha', 'Neha', 'Rahul']`, names should be sorted as `amit, Amit, Neha, Neha, rahul, Rahul` while maintaining custom sorting without built-in sorting functions and accurate duplicate detection.

## What Changes

- **Natural Dictionary Comparison**: Update `compare_strings` to perform case-insensitive alphabetical comparison as the primary criterion (comparing lowercase equivalents).
- **Secondary Tie-Breaking**: When two names match case-insensitively (e.g., `"amit"` and `"Amit"`), apply deterministic tie-breaking (e.g. lowercase precedes uppercase, or ASCII comparison) to ensure consistent ordering.
- **Duplicate Reporting**: Retain $O(n)$ duplicate detection, reporting duplicates based on exact or case-aware equivalence (e.g. `'Neha'` appearing 2 times).
- **Documentation & Tests**: Update analysis report, pseudocode, complexity proofs, and test cases in `test_problem1.py`.

## Capabilities

### New Capabilities
- `employee-directory`: Dictionary-order lexicographical sorting (case-insensitive primary, deterministic secondary) and duplicate detection for employee names.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: `problem1_employee_directory.py` custom comparison function and duplicate detection.
- **Tests**: `test_problem1.py` with cases verifying natural dictionary ordering (e.g. `amit, Amit, Neha, Neha, rahul, Rahul`).
- **Documentation**: `problem1_analysis.md` updated with revised case comparison rules and pseudocode.
