## Purpose

Provides a complete, publication-quality LaTeX report document and associated graphical artifacts for DAA Lab Assignment 4 (Divide and Conquer), encompassing all code implementations, benchmark executions, visual plots, tables, and theoretical analyses.

## ADDED Requirements

### Requirement: Standard Document Architecture and Header Compliance
The LaTeX source file MUST implement the exact required preamble, package configuration, and running header structure. It SHALL use 12pt font with `newtxtext` and `newtxmath`, 1-inch margins on A4 paper, a `fancyhdr` header displaying the student name ("Kishan Sahu") and enrollment number ("P26DS017"), and custom `listings` styles for source code (`style=code`) and terminal execution outputs (`style=output`).

#### Scenario: Document structure verification
- **WHEN** the LaTeX document `DAA_Lab4_Report.tex` is inspected or compiled
- **THEN** it contains the exact specified packages, geometry settings, header information, and listings definitions without syntax errors.

### Requirement: Problem 1 Comprehensive Inversion Counting and Sorting Content
The document MUST include the complete code, verification results, experimental execution times, generated visualization figure, and theoretical analysis for Problem 1 (Counting Inversions and Sorting).

#### Scenario: Problem 1 content inclusion
- **WHEN** the Problem 1 section of the report is reviewed
- **THEN** it presents the Divide-and-Conquer merge sort inversion counter ($O(n \log n)$), Brute Force counter ($O(n^2)$), Quick Sort, and Insertion Sort implementations, verification on sample input `[8, 4, 2, 1]`, an empirical runtime comparison table across input sizes $n \in [100, 3200]$, the embedded plot figure `p1_inversion_benchmark.png`, and a rigorous complexity analysis applying the Master Theorem to $T(n) = 2T(n/2) + \Theta(n)$.

### Requirement: Problem 2 Comprehensive Fast Exponentiation Content
The document MUST include the complete code, verification results, experimental execution times, generated visualization figure, and in-depth answers to all theoretical analysis questions for Problem 2 (Fast Exponentiation).

#### Scenario: Problem 2 content inclusion
- **WHEN** the Problem 2 section of the report is reviewed
- **THEN** it presents Repeated Multiplication ($O(n)$), Naive Recursive ($O(n)$), Divide and Conquer ($O(\log n)$), and Iterative Binary Exponentiation ($O(1)$ space), verification on $2^{10}$, an empirical timing comparison table across exponent values $n \in [50, 500]$, the embedded plot figure `p2_exponentiation_benchmark.png`, and detailed answers to all 7 lab questions including Master Theorem recurrence derivation, auxiliary space, subproblem redundancy, arbitrary-precision bit multiplication scaling, paradigm comparison, and experimental vs theoretical deviation.

### Requirement: Asset Generation and Error-Free PDF Compilation
The system MUST produce the required high-resolution benchmark visualization figures as standalone PNG assets and successfully compile the complete LaTeX source file to PDF without errors or missing figure warnings.

#### Scenario: PDF generation success
- **WHEN** `pdflatex` is executed on `DAA_Lab4_Report.tex`
- **THEN** the compiler completes with return code 0, embedding all referenced images and producing `DAA_Lab4_Report.pdf`.
