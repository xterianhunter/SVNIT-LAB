## Context

See `proposal.md` for problem description. Problem 2 requires implementing Bubble Sort, Selection Sort, and Insertion Sort from first principles and evaluating them on Random, Already Sorted, and Reverse Sorted inputs across multiple sizes.

## Goals / Non-Goals

**Goals:**
- Provide a clean, short, standalone `problem2_sorting.py` script.
- Implement Bubble Sort (with early exit), Selection Sort, and Insertion Sort without built-in sorting libraries (`sort()`, `sorted()`).
- Test multiple input sizes ($N \in \{50, 100, 200, 500\}$) across 3 distributions: Random, Sorted, Reverse Sorted.
- Measure execution time accurately using `time.perf_counter_ns()` and track exact operation comparisons.
- Format results into clear console tables and provide M.Tech-level theoretical complexity discussion.

**Non-Goals:**
- Advanced divide-and-conquer sorts like Merge Sort or Quick Sort (covered in subsequent lab assignments).

## Decisions

### Decision 1: Self-Contained Single Script Structure
- **Choice**: Structure `problem2_sorting.py` with 4 clear sections:
  1. Algorithms (Pure functions taking `arr` and returning `(sorted_arr, comparisons)`)
  2. Data generation helpers (`generate_input(n, input_type)`)
  3. Benchmarking runner (`run_experiment()`)
  4. Tabulation and Complexity Analysis (`display_results()`, `print_analysis()`)
- **Rationale**: Easy for M.Tech students to review, run, submit, and explain in viva.

### Decision 2: Array Copying During Benchmark
- **Choice**: Always pass a fresh shallow copy (`arr[:]` or `arr.copy()`) to sorting algorithms to prevent mutations affecting subsequent runs.

### Decision 3: Early-Stop Bubble Sort
- **Choice**: Use a `swapped` boolean flag in Bubble Sort. If no swap occurs in pass $i$, break immediately to achieve $\mathcal{O}(n)$ best-case on already sorted inputs.

## Risks / Trade-offs

- **[Risk]** In-place modification contaminating benchmarks → **Mitigation**: Perform `.copy()` before each timed invocation.
- **[Risk]** Large $N$ causing long execution times on $\mathcal{O}(n^2)$ reverse inputs → **Mitigation**: Choose sensible size bounds ($50 \le N \le 500$) with adaptive iteration count for timing.
