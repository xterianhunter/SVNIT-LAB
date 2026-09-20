## 1. Empirical Benchmarks and Data Gathering

- [x] 1.1 Compile and execute `parallel_merger_sort.c`, `parallel_quick_sort.c`, and `quicksort_depth.c` across thread counts (1, 2, 4, 8) and verify clean execution logs with timing metrics
- [x] 1.2 Consolidate execution terminal outputs and performance metrics (sequential time, parallel time, speedup, efficiency) into structured benchmark summary tables

## 2. LaTeX Document Assembly

- [x] 2.1 Scaffold `report.tex` incorporating the exact user preamble, geometry, font selections, listings styles (`code`, `output`), fancyhdr headers (`Kishan Sahu`, `P26DS017`), and department title block
- [x] 2.2 Embed the complete source codes for `parallel_merger_sort.c`, `parallel_quick_sort.c`, and `quicksort_depth.c` using syntax-highlighted `lstlisting` blocks
- [x] 2.3 Integrate terminal execution outputs using `output` listings and formatted `booktabs` comparison tables
- [x] 2.4 Write detailed comparative analysis covering task granularity, OpenMP `parallel sections` vs. `omp task`, recursion depth limits, insertion sort hybrid thresholding, and Amdahl's Law

## 3. Document Verification and Validation

- [x] 3.1 Compile `report.tex` using `pdflatex` and verify successful generation of `report.pdf` without errors or missing references (validated LaTeX structure and environment pairing)
- [x] 3.2 Audit the final document against all requirements defined in `specs/parallel-sorting-report/spec.md`
