## Why

A comprehensive, academic lab report in LaTeX is required for Lab Assignment 4 (CSDS125: High Performance Computing, SVNIT Surat) documenting the implementation, empirical performance, and architectural analysis of OpenMP parallel sorting algorithms. The report must specifically evaluate three implementations: `parallel_merger_sort.c`, `parallel_quick_sort.c`, and `quicksort_depth.c`.

## What Changes

- Create a comprehensive LaTeX report (`report.tex`) strictly conforming to the user-specified document preamble, header formatting (student metadata: Kishan Sahu, P26DS017; department details), and styling guidelines.
- Embed complete, syntax-highlighted C source code listings for:
  - `parallel_merger_sort.c` (OpenMP sections-based parallel merge sort)
  - `parallel_quick_sort.c` (OpenMP task-based parallel quicksort without recursion cutoff)
  - `quicksort_depth.c` (OpenMP task-based parallel quicksort with depth cutoff and insertion sort base case)
- Capture and format terminal execution outputs showing timing, speedup, and thread metrics for each program.
- Include structured benchmark analysis tables summarizing execution time, speedup, and parallel efficiency across threads and problem sizes.
- Provide thorough comparative analysis addressing task creation overhead, recursion depth cutoff benefits, OpenMP sections vs. tasks, and Amdahl's law implications.

## Capabilities

### New Capabilities
- `parallel-sorting-report`: LaTeX document specification and reporting pipeline for OpenMP parallel sorting benchmarks and comparative analysis.

### Modified Capabilities
<!-- None -->

## Impact

- Adds `report.tex` in the Lab 4 root directory.
- No modifications or breaking changes to existing C source files (`parallel_merger_sort.c`, `parallel_quick_sort.c`, `quicksort_depth.c`).
