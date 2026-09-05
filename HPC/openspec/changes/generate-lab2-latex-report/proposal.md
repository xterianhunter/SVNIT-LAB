## Why

A standardized, publication-quality LaTeX lab report (`Lab2.tex`) is required to document the OpenMP high-performance computing experiments, including source code listings, terminal execution logs, empirical benchmark tables, and comparative analyses without pseudo-code algorithm blocks, adhering strictly to the visual format and layout conventions established in `main.tex`.

## What Changes

- Create `Lab2.tex` using the exact document class, packages, headers, margins, typography (Times font via `newtxtext,newtxmath`), and listing styles defined in `main.tex`.
- Structure the report with the departmental header (SVNIT Surat, M.Tech I, HPC Lab Assignment 2) and student credentials (Kishan Sahu, P26DS017).
- Format all 3 problem statements:
  - **Problem Statement 1**: Unsynchronized Race Condition Demonstration (C code listing, execution output, and race condition analysis).
  - **Problem Statement 2**: Critical Section Synchronization Solution (C code listing, verified output, and mutual exclusion analysis).
  - **Problem Statement 3**: Parallel Matrix-Matrix Multiplication (C code listing, terminal benchmark outputs, comparative empirical performance tables across $N \in \{500, 1000, 1500\}$ with speedup and efficiency metrics, and comprehensive analysis of coarse vs. fine decomposition).
- Omit all algorithmic pseudo-code environments (`\begin{algorithm}...\end{algorithm}`) as requested.
- Ensure automated compilation of `Lab2.tex` to `Lab2.pdf` via `pdflatex`.

## Capabilities

### New Capabilities
- `lab-report-generation`: Generates and compiles the comprehensive LaTeX laboratory report `Lab2.tex` encapsulating OpenMP race condition demos, critical section solutions, parallel matrix multiplication implementations, empirical benchmark tables, and architectural analyses matching the `main.tex` template style.

### Modified Capabilities
<!-- No existing capabilities modified -->

## Impact

- **New Files**: `Lab2.tex` (and compiled `Lab2.pdf`).
- **Dependencies**: TeX Live / `pdflatex` engine.
- **Code Assets**: References `src/race_condition.c`, `src/critical_section.c`, `src/matrix_mult.c`, and `benchmark_results.md`.
