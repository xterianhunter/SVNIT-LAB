## Context

See `proposal.md` for motivation. The codebase contains `DAA_Lab4.ipynb`, which implements two major Divide-and-Conquer problems:
1. Inversion Counting and Sorting Comparison (Merge Sort Inversion Counter vs Brute Force, Quick Sort, Insertion Sort).
2. Fast Exponentiation (Repeated Multiplication, Naive Recursive, Divide and Conquer, and Iterative Binary Exponentiation).

The user has specified an exact LaTeX documentclass, geometry, typography (`newtxtext, newtxmath`), header (`fancyhdr` with Student Name: Kishan Sahu, Enrollment No.: P26DS017), and `listings` environment configurations (`code` and `output` styles).

## Goals / Non-Goals

**Goals:**
- Provide a modular, clean Python extraction script to execute the notebook benchmarks and generate high-resolution PNG figures (`p1_inversion_benchmark.png`, `p2_exponentiation_benchmark.png`).
- Record concrete timing measurements to populate LaTeX comparison tables.
- Generate `DAA_Lab4_Report.tex` integrating all code, outputs, figures, tables, and theoretical analyses.
- Compile `DAA_Lab4_Report.tex` to `DAA_Lab4_Report.pdf` cleanly using `pdflatex`.

**Non-Goals:**
- Altering the original logic or content of `DAA_Lab4.ipynb`.
- Using external graphical tools; all visual assets are generated programmatically via Python/matplotlib.

## Decisions

- **Decision 1: Benchmark Execution and Asset Output**:
  - *Choice*: Run a lightweight script to generate the exact plots from the notebook and save them as `p1_inversion_benchmark.png` and `p2_exponentiation_benchmark.png` at 300 DPI with tight bounding boxes.
  - *Alternative*: Manual screenshotting (inferior quality, non-reproducible).

- **Decision 2: LaTeX Structure and Styling**:
  - *Choice*: Strictly follow the user's provided preamble: 12pt article, 1-inch margins, `newtxtext` & `newtxmath`, `fancyhdr` configuration, and `lstdefinestyle` for `code` and `output`.
  - *Title Block*: Retain the exact department and course headings, aligning the assignment title with "Lab Assignment 4 \\ Divide and Conquer".

- **Decision 3: Inclusion of All Notebook Content**:
  - *Problem 1*: Problem description, Inversion definition, Python code for Divide-and-Conquer Merge Sort ($O(n \log n)$), Brute Force ($O(n^2)$), Quick Sort, Insertion Sort, verification on `[8, 4, 2, 1]`, execution time table, embedded plot, and recurrence/Master Theorem analysis.
  - *Problem 2*: Problem description, Python code for Repeated Multiplication ($O(n)$), Naive Recursive ($O(n)$), Divide and Conquer ($O(\log n)$), verification on $2^{10}$, execution time table, embedded plot, iterative implementation, and comprehensive answers to all 7 lab questions.

## Risks / Trade-offs

- **[Risk] Missing TeX packages on system** → **Mitigation**: Standard Ubuntu TeX Live distribution usually includes `newtx` and `fancyhdr`. We will verify via `pdflatex` during verification and handle any missing style warnings.
- **[Risk] High-dimension numbers in exponentiation benchmark causing slowdowns** → **Mitigation**: Exponent ranges up to $n=500$ are within standard Python integer handling and benchmark in fractions of a millisecond.
