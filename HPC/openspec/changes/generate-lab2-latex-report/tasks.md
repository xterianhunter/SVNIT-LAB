## 1. LaTeX Document Structure & Preamble Setup

- [x] 1.1 Create `Lab2.tex` with document preamble, A4 1-inch margins, 12pt Times typography (`newtxtext,newtxmath`), fancy headers (`Name: Kishan Sahu`, `Enrollment No.: P26DS017`), SVNIT department title block for HPC Lab Assignment 2, and listing styles adapted for C syntax and terminal output matching `main.tex`.

## 2. Problem Statements Content & Benchmark Integration

- [x] 2.1 Implement Problem Statement 1 section in `Lab2.tex` containing the problem description, complete C code for `src/race_condition.c`, terminal output demonstrating lost updates, and analysis of unsynchronized race conditions.
- [x] 2.2 Implement Problem Statement 2 section in `Lab2.tex` containing the problem description, complete C code for `src/critical_section.c`, verified terminal output with zero errors, and analysis of OpenMP `#pragma omp critical` mutual exclusion.
- [x] 2.3 Implement Problem Statement 3 section in `Lab2.tex` containing the problem description, complete C code for `src/matrix_mult.c`, terminal execution output, empirical benchmark comparison tables across matrix sizes ($N = 500, 1000, 1500$) and thread counts ($T = 1, 2, 4, 8$), and in-depth comparative analysis contrasting coarse-grained and fine-grained decomposition.

## 3. PDF Compilation & Verification

- [x] 3.1 Compile `Lab2.tex` using `pdflatex` to generate `Lab2.pdf`, verifying successful compilation with exit code 0, correct page layouts, table formatting, and absence of algorithm environments.
