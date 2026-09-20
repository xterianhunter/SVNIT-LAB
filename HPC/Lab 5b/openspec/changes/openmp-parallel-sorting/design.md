## Context

See `proposal.md` for motivation and background. This design focuses on the architectural structure and technical implementation of sequential and OpenMP-accelerated sorting algorithms in C99.

## Goals / Non-Goals

**Goals:**
- Provide clear, concise, and production-grade C implementations of:
  1. Sequential Merge Sort
  2. Sequential Quick Sort
  3. Parallel Merge Sort using `#pragma omp parallel sections` / `#pragma omp section`
  4. Parallel Quick Sort using `#pragma omp task` and `#pragma omp taskwait`
  5. Depth-limited Parallel Quick Sort with cutoff (depth 4 or 8) falling back to sequential Insertion Sort
- Ensure thread-safe array partitioning and merge operations.
- Provide a single self-contained driver program (`sort_benchmark.c`) that benchmarks all 5 algorithms on identical input data across configurable array sizes (e.g., $10^5$, $5 \times 10^5$, $10^6$ elements).
- Output a clean ASCII comparison table displaying Execution Time (seconds), Speedup factor, and Correctness verification (`PASS`/`FAIL`).

**Non-Goals:**
- Use of external benchmarking or graphing libraries.
- Distributed memory implementations (MPI) or GPU kernel offloading.
- Overcomplicated micro-optimizations that obscure readability.

## Decisions

### 1. Language and Compilation
- **Decision**: Standard C99 compiled with `gcc -O3 -fopenmp`.
- **Rationale**: Minimal footprint, zero third-party dependencies, directly runnable in standard academic/lab Linux environments.

### 2. Parallel Merge Sort with OpenMP Sections
- **Decision**: Use `#pragma omp parallel sections` with depth throttling.
- **Rationale**: Direct recursive invocation of parallel regions without depth control creates $2^d$ threads, causing high thread creation and context-switch overhead. By limiting the parallel section decomposition to depth $\le \log_2(\text{num\_threads})$ (e.g. depth 2 or 3) and calling sequential merge sort below this depth, we maximize CPU utilization while avoiding thread explosion.
- **Alternative Considered**: Flat iteration or work-stealing tasks (rejected because sections was explicitly required by the prompt).

### 3. Parallel Quick Sort with OpenMP Tasks
- **Decision**: Enclose the root quicksort call inside `#pragma omp parallel` and `#pragma omp single nowait`, spawning subproblems with `#pragma omp task`.
- **Rationale**: Tasks are dynamic work units ideally suited for irregular recursive divide-and-conquer trees. One child can be spawned as a task while the parent executes the other, followed by `#pragma omp taskwait`.

### 4. Depth-Limited Hybrid Quick Sort with Insertion Sort
- **Decision**: Track `depth` parameter during recursion. If `depth >= DEPTH_LIMIT` (configurable, default 4 or 8) or partition size $n \le 32$, bypass task creation and switch to sequential Insertion Sort.
- **Rationale**: Depth 4 produces up to $2^4 = 16$ parallel partitions (ideal for 4-8 core machines), while depth 8 produces up to $2^8 = 256$ tasks (ideal for 16-32+ threads). Insertion sort has minimal overhead for small arrays ($n \le 32$) compared to quicksort's partition overhead and OpenMP task queue latency.

### 5. Fair Benchmarking Protocol
- **Decision**: Generate a pseudo-random integer array with a fixed seed. For each sort algorithm, copy the raw master array to a working buffer, run `omp_get_wtime()` around the sort routine, and verify monotonic non-decreasing order via an `is_sorted()` validator.
- **Rationale**: Ensures every algorithm processes identical inputs in the same initial state, guaranteeing scientific fairness and valid speedup calculations.

## Risks / Trade-offs

- **[Excessive Task Overhead on Small Subarrays]** → Mitigated by enforcing a minimum size cutoff ($n > 1000$) before creating parallel tasks.
- **[Thread Oversubscription with Nested Sections]** → Mitigated by bounding section depth to avoid runaway thread spawning.
- **[Worst-case Quick Sort Partitioning]** → Mitigated by choosing the middle element or median pivot to prevent $O(n^2)$ recursion depth on partially sorted arrays.
