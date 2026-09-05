## Why

A comprehensive, formal LaTeX laboratory report is required for Design and Analysis of Algorithms (CSDS103) Lab Assignment 4 ("Divide and Conquer"). The report must encapsulate all algorithms, Python code implementations, execution outputs, benchmark comparison tables, generated visualization plots, and detailed theoretical complexity analyses from `DAA_Lab4.ipynb`.

## What Changes

- Create a structured LaTeX document (`DAA_Lab4_Report.tex`) adhering to the user's specific formatting requirements (12pt font, Times-style newtxtext/newtxmath, fancyhdr header with student details, custom code/output listings styles).
- Extract and generate the benchmark visualization images (`p1_inversion_benchmark.png` and `p2_exponentiation_benchmark.png`) from the notebook's experimental scripts.
- Incorporate complete implementations, verification outputs, comparison tables, and rigorous theoretical analyses for both problems:
  - **Problem 1: Counting Inversions**: Divide-and-Conquer Merge Sort ($O(n \log n)$), Brute Force ($O(n^2)$), Quick Sort, Insertion Sort, recurrence relation with Master Theorem, and empirical evaluation.
  - **Problem 2: Fast Exponentiation**: Repeated Multiplication ($O(n)$), Naive Recursive ($O(n)$ with redundant subproblems), Divide-and-Conquer ($O(\log n)$), Iterative Binary Exponentiation ($O(1)$ space), bit complexity analysis, and paradigm comparisons.
- Verify compilation of the LaTeX report to PDF with zero compilation errors.

## Capabilities

### New Capabilities
- `latex-report`: Generation of formal LaTeX document and associated figure artifacts for DAA Lab 4 covering all code, outputs, benchmarks, figures, tables, and theoretical analyses.

### Modified Capabilities
<!-- None -->

## Impact

- Adds new file `DAA_Lab4_Report.tex` (and compiled `DAA_Lab4_Report.pdf`).
- Adds benchmark image assets for inclusion in the document.
- Does not modify existing code in `DAA_Lab4.ipynb`.
