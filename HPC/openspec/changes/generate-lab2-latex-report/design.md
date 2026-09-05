## Context

The user requires a new LaTeX document `Lab2.tex` formatted identically to `main.tex` (typography, margins, header rules, code listing themes, output blocks, and section structures). It will document the three OpenMP laboratory exercises: race condition demonstration, critical section synchronization, and parallel matrix-matrix multiplication comparing coarse-grained vs. fine-grained data decomposition with empirical performance tables, while omitting pseudo-code algorithm blocks.

## Goals / Non-Goals

**Goals:**
- Replicate the exact visual theme and page formatting of `main.tex` (A4 geometry, 1-inch margins, 12pt Times font via `newtxtext,newtxmath`, `fancyhdr` header, single-frame code and output listings).
- Format Problem Statements 1, 2, and 3 with problem descriptions, complete C source code, actual terminal execution logs, and detailed theoretical and empirical analyses.
- Incorporate formatted LaTeX tables within Problem 3's analysis displaying benchmark metrics (Execution Time, GFLOPS, Speedup, and Efficiency) across matrix dimensions ($500 \times 500, 1000 \times 1000, 1500 \times 1500$) and thread counts ($1, 2, 4, 8$).
- Ensure compilation with `pdflatex Lab2.tex` completes cleanly without warnings or errors.

**Non-Goals:**
- Pseudo-code algorithm blocks (`algorithm` or `algorithmic` environments), which are explicitly excluded.
- Modifying the existing `main.tex` file.

## Decisions

### 1. Document Preamble & Listing Styles
- **Decision**: Adapt `lstdefinestyle{code}` for `language=C` with syntax highlighting for C keywords and OpenMP directives (`#pragma omp`), while maintaining line numbering, single framing, and fonts identical to `main.tex`.
- **Listing `output` Style**: Monospace output block with light gray background (`color{gray!4}`) and single framing matching `main.tex`.

### 2. Header and Title Formatting
- **Student Header**: `\fancyhead[L]{Name: Kishan Sahu{\hspace{4cm}}}` and `\fancyhead[R]{Enrollment No.: P26DS017{\hspace{3.5cm}}}`.
- **Title Block**: Center block for SVNIT Surat, M.Tech I, High Performance Computing, Lab Assignment 2.

### 3. Problem Organization & Structure
- **Problem Statement 1**: Unsynchronized Race Condition (`src/race_condition.c`) $\rightarrow$ Code $\rightarrow$ Output $\rightarrow$ Analysis.
- **Problem Statement 2**: Critical Section Synchronization (`src/critical_section.c`) $\rightarrow$ Code $\rightarrow$ Output $\rightarrow$ Analysis.
- **Problem Statement 3**: Parallel Matrix Multiplication (`src/matrix_mult.c`) $\rightarrow$ Code $\rightarrow$ Output $\rightarrow$ Benchmark Tables ($N=500, 1000, 1500$) $\rightarrow$ Comprehensive Comparative Analysis (Decomposition mechanisms, scheduling overhead, cache locality, scalability).

## Risks / Trade-offs

- **[Risk] LaTeX Special Character Escapes in C Code / Output**:
  - *Mitigation*: Listing environments (`lstlisting`) natively handle underscores, pointers (`*`), and `#pragma` without manual escaping.
- **[Risk] Wide Tables Overflowing Margins**:
  - *Mitigation*: Format tables using standard `tabular` with centered columns (`p{...}` or `c`), fitting cleanly within 1-inch margins.
