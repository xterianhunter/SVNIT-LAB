## Why

An organisation maintains an unsorted list of $n$ employee names. To satisfy Problem 1 of DAA Lab Assignment 1 (CSDS103), we need an algorithm and program to arrange these employee names in lexicographical order without using built-in sorting functions, and detect and display all names occurring more than once (or explicitly report if no duplicates exist). The program must accept comma-separated employee names directly from user input, handle boundary and edge cases gracefully, and provide comprehensive time/space complexity analyses alongside duplicate detection comparisons.

## What Changes

- Create an interactive console application that takes comma-separated employee names as user input, trims whitespace, and processes them.
- Implement a custom sorting algorithm (such as Merge Sort or Quick Sort) written from scratch without any built-in sorting utilities.
- Define and implement clear character comparison semantics for uppercase and lowercase letters (e.g., ASCII-based lexicographical comparison with standard order or case-insensitive grouping).
- Implement duplicate detection on the sorted list to identify and report all duplicate employee names, or report that no duplicates exist.
- Formulate comprehensive algorithmic documentation including pseudocode, time complexity (best, average, worst case), auxiliary space complexity, and a comparative study of duplicate detection without sorting (e.g., hash maps vs. nested loops).

## Capabilities

### New Capabilities
- `employee-directory`: Lexicographical sorting without built-in sort functions and duplicate detection for comma-separated employee directory names.

### Modified Capabilities
<!-- None -->

## Impact

- **Source Code**: New implementation file (e.g. `problem1_employee_directory.py`) containing the sorting algorithm, duplicate detector, and interactive user input handler.
- **Documentation**: Pseudocode, complexity proofs/breakdown, and analysis of alternative duplicate detection methods.
- **Dependencies**: Standard library only (no external dependencies, no built-in sorting functions like `.sort()` or `sorted()`).
