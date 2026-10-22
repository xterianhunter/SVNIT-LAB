## Context

See `proposal.md` for motivation and background. The workspace contains three OpenMP parallel sorting programs:
1. `parallel_merger_sort.c`: Uses OpenMP `parallel sections` with recursive depth cutoff (`depth - 1`, cutoff at `depth < 0`) switching to sequential merge sort.
2. `parallel_quick_sort.c`: Uses OpenMP `#pragma omp task` for both sub-partitions inside a `#pragma omp single` region without any depth limit or task throttling.
3. `quicksort_depth.c`: Uses OpenMP `#pragma omp task` with explicit depth tracking (`depth - 1`), stopping task creation when `depth == 0` and switching to sequential `insertionSort()`.

The objective is to produce `report.tex` strictly formatted per the requested LaTeX specification, embedding complete code listings, execution outputs, benchmark summary tables, and comprehensive performance analysis.

## Goals / Non-Goals

**Goals:**
- Implement `report.tex` adhering exactly to the user-specified preamble, geometry, font settings (`newtxtext`, `newtxmath`), fancyhdr headers, and listing styles (`code` and `output`).
- Accurately integrate the full, unmodified C source codes for `parallel_merger_sort.c`, `parallel_quick_sort.c`, and `quicksort_depth.c`.
- Provide authentic benchmark outputs and structured LaTeX tables (`booktabs`) comparing execution times, speedup, and parallel efficiency.
- Deliver in-depth architectural analysis explaining OpenMP task queue overhead, section vs. task semantics, cache locality, and recursion thresholding.
- Ensure the LaTeX file compiles cleanly to PDF using `pdflatex`.

**Non-Goals:**
- Modifying the existing C implementation logic or changing other legacy files (e.g. `quicksort_sections.c`, `task_demo.c`).
- Producing non-LaTeX outputs (e.g., Word, HTML).

## Decisions

1. **LaTeX Header & Title Configuration**:
   - *Decision*: Preserve the exact preamble, geometry, fonts, fancyhdr header (`Name: Kishan Sahu`, `Enrollment No.: P26DS017`), and center banner layout requested by the user, setting the title to **Lab Assignment 4: Parallel Sorting using OpenMP** (while referencing the SVNIT CSDS125 department template).
   - *Rationale*: Maintains academic and institutional consistency while accurately reflecting Lab 4's parallel sorting focus.

2. **Source Code Listing Integration**:
   - *Decision*: Embed the C source files directly into the document using `\begin{lstlisting}[style=code, caption=..., label=...]` environments rather than relying on external `\lstinputlisting` commands.
   - *Rationale*: Direct inclusion guarantees that `report.tex` is completely self-contained and portable when shared or compiled across different environments.

3. **Empirical Benchmarking & Performance Tables**:
   - *Decision*: Run the compiled binaries to obtain empirical timing data for sequential vs. parallel execution across different thread counts ($T \in \{1, 2, 4, 8\}$), and summarize them using high-quality `booktabs` tables.
   - *Rationale*: Delivers concrete quantitative analysis reflecting actual hardware execution instead of hypothetical estimates.

4. **Comparative Analysis Architecture**:
   - *Decision*: Structure the analysis into four rigorous subsections:
     1. Algorithmic Overview and OpenMP Constructs (Sections vs. Tasks).
     2. Empirical Benchmark Results and Tables.
     3. Granularity & Task Scheduling Overhead Analysis (explaining why unconstrained quicksort experiences degradation and why depth limits restore performance).
     4. Amdahl's Law, Memory Bottlenecks (merging bandwidth vs partitioning in-place), and Concurrency Trade-offs.

## Risks / Trade-offs

- **[Risk] Unconstrained Quicksort Slowdown** → Naive OpenMP task creation generates millions of sub-tasks for tiny arrays ($N=10^6$), creating substantial task queue contention and parallel slowdown.
  - *Mitigation*: Highlight this exact empirical phenomenon in the analysis as a key pedagogical finding demonstrating the necessity of cutoff thresholds and hybrid sorting.
- **[Risk] LaTeX Compilation Environment** → `pdflatex` or specific TeX fonts might not be available or might encounter font errors if dependencies are missing.
  - *Mitigation*: Test compilation using `pdflatex -interaction=nonstopmode report.tex` in verification, ensuring all standard packages work properly.
