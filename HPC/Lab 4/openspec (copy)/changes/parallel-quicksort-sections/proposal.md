## Why

QuickSort is a classic divide-and-conquer algorithm whose recursive sub-problems are independent — making it a natural fit for OpenMP `sections`. This change creates a single C program that implements both a sequential quicksort and a parallel quicksort (using `#pragma omp sections`), times them on the same random array, and prints a comparison. The parallel version uses a `depth` parameter to limit thread spawning: sections are used only while `depth > 0`, after which it falls back to sequential sorting.

## What Changes

- Create a standalone C program `quicksort_sections.c` containing:
  - A sequential quicksort (`quicksort_sequential`).
  - A parallel quicksort (`quicksort_parallel`) that uses `#pragma omp parallel sections` recursively, accepting `depth` as a 4th argument to control how deep parallelism goes before falling back to sequential.
  - A `main()` that populates an array with random values, sorts a copy with each variant, times both using `omp_get_wtime()`, and prints a comparison.

## Capabilities

### New Capabilities
- `parallel-quicksort-sections`: Sequential vs. parallel (OpenMP sections with depth-limited recursion) quicksort comparison in C.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**: Adds `quicksort_sections.c` to the workspace.
- **Dependencies**: Requires GCC with `-fopenmp`.
- **APIs / Libraries**: Uses `omp.h` (`omp_get_wtime`, `omp_get_thread_num`), `stdlib.h` (`rand`, `srand`), `string.h` (`memcpy`).
