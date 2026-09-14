## Context

See `proposal.md` for motivation. The user wants a single, simple C file that contains both a sequential and a parallel quicksort, times them, and prints a comparison. The parallel version must use `#pragma omp sections` with a `depth` parameter as the 4th argument to the parallel quicksort function.

## Goals / Non-Goals

**Goals:**
- Single file `quicksort_sections.c` with everything self-contained.
- `partition()` shared by both variants — standard Lomuto or Hoare partition.
- `quicksort_sequential(arr, low, high)` — plain recursive quicksort.
- `quicksort_parallel(arr, low, high, depth)` — when `depth > 0`, uses `#pragma omp parallel sections` to recurse left/right in parallel with `depth - 1`; when `depth == 0`, calls `quicksort_sequential`.
- `main()` fills an array with random ints, copies it, sorts each copy with the two variants, times with `omp_get_wtime()`, prints both times.

**Non-Goals:**
- Fancy pivoting strategies (median-of-three, etc.).
- External libraries, benchmarking frameworks, or command-line argument parsing.

## Decisions

- **Depth as 4th argument to `quicksort_parallel`**:
  The user explicitly requested `depth` as the 4th argument. When `depth > 0`, the function opens `#pragma omp parallel sections` with two `#pragma omp section` blocks for the left and right sub-arrays, decrementing `depth`. When `depth == 0`, it calls `quicksort_sequential` directly.
  *Rationale*: Avoids exponential thread creation; limits parallelism to the top levels of recursion where sub-problems are large enough to benefit.
  *Alternative considered*: Using a threshold based on array size — rejected for simplicity per user request.

- **Timing with `omp_get_wtime()`**:
  *Rationale*: Portable OpenMP wall-clock timer, no extra dependencies.

- **Array size hardcoded in `main()`**:
  Using a `#define N` constant (e.g., 100000). Keeps the program simple without argument parsing.

## Risks / Trade-offs

- *[Risk]* For small arrays or high `depth`, the overhead of creating parallel sections exceeds the sorting work.
  → *Mitigation*: Default depth of 4 (16 leaf tasks) balances parallelism vs. overhead for typical thread counts.
