## 1. Create quicksort_sections.c

- [x] 1.1 Create `quicksort_sections.c` containing: `swap()`, `partition()`, `quicksort_sequential(arr, low, high)`, `quicksort_parallel(arr, low, high, depth)` (uses `#pragma omp parallel sections` when `depth > 0`, falls back to `quicksort_sequential` when `depth == 0`), and a `main()` that fills a random array, copies it, sorts each copy with the two variants using `omp_get_wtime()` for timing, and prints both elapsed times. Verify compilation succeeds with `gcc -fopenmp quicksort_sections.c -o quicksort_sections`.

## 2. Verify execution

- [x] 2.1 Run `OMP_NUM_THREADS=4 ./quicksort_sections` and verify that both sequential and parallel times are printed and the parallel version completes faster (or comparably for small arrays).
