## 1. Core Sorting Algorithms Implementation

- [x] 1.1 Implement sequential Merge Sort and sequential Quick Sort in `sort_benchmark.c` and verify correctness with `is_sorted()`.
- [x] 1.2 Implement parallel Merge Sort using OpenMP `#pragma omp parallel sections` with recursive depth limiting and verify correctness against unsorted arrays.
- [x] 1.3 Implement parallel Quick Sort using OpenMP `#pragma omp task` and `#pragma omp taskwait` within an `#pragma omp parallel` region and verify correctness.
- [x] 1.4 Implement depth-limited parallel Quick Sort with depth threshold (4/8) and sequential Insertion Sort cutoff for small partitions, and verify correctness.

## 2. Benchmarking Harness & Output Formatting

- [x] 2.1 Implement random array generation, deep copy routines, and timing with `omp_get_wtime()` across multiple large array sizes ($10^5$, $5 \times 10^5$, $10^6$).
- [x] 2.2 Build a formatted ASCII/Markdown benchmark comparison table displaying execution time (seconds), speedup relative to sequential baselines, and sort verification status.
- [x] 2.3 Compile with `gcc -O3 -fopenmp sort_benchmark.c -o sort_benchmark` and execute on the target machine to collect empirical benchmark data.

## 3. Report Documentation & Deliverables

- [x] 3.1 Prepare a structured lab report document (`REPORT.md`) containing clean source code, execution outputs, performance comparison table, and analysis of section vs task scalability.
