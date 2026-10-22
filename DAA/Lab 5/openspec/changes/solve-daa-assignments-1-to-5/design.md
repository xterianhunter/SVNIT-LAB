## Context

CS103 Lab Assignments 1 through 5 require implementing core algorithmic paradigms, empirical benchmarking, and theoretical comparison. The user explicitly requested a concise, minimalist Jupyter Notebook (`daa_assignments_1_to_5.ipynb`) containing only necessary code without redundant boilerplate or extra complexity.

## Goals / Non-Goals

**Goals:**
- Provide a single, clean `.ipynb` notebook containing five well-organized sections corresponding to Assignments 1 through 5.
- Keep all function implementations simple, readable, and strictly adhering to specified algorithms (Divide & Conquer, Heap selection, Quickselect partition, monotonic timing, and loop analysis).
- Include concise timing routines with microsecond precision and theoretical vs. empirical comparisons.

**Non-Goals:**
- No complex external dependencies or heavy GUI/dashboard frameworks.
- No verbose boilerplate, complex OOP wrappers, or excessive visual artifacts.
- Assignments 6 through 8 are out of scope (user specifically requested 1 to 5).

## Decisions

### Decision 1: Single Self-Contained Jupyter Notebook
- **Choice**: Implement all solutions in `daa_assignments_1_to_5.ipynb` with clear markdown headings and executable code cells.
- **Rationale**: Meets the user's explicit format requirement and enables immediate execution and visualization in lab environments.
- **Alternatives considered**: Separate `.py` scripts (rejected because the user explicitly asked for an `.ipynb` file).

### Decision 2: Implementation of Assignment 1 (Closest Pair of Points)
- **Choice**: Implement brute-force $O(n^2)$ checking all point pairs; implement divide-and-conquer $O(n \log n)$ by pre-sorting points by x-coordinate, recursively finding minimum distances in halves, and checking the vertical strip across the divider sorted by y-coordinate (checking at most 7 neighbors per point in the strip).
- **Rationale**: Standard textbook algorithm (CLRS / Kleinberg-Tardos) ensuring exact $O(n \log n)$ divide-and-conquer behavior.

### Decision 3: Implementation of Assignment 2 & 3 (1M Dataset, Duplicates, and Microsecond Timing)
- **Choice**:
  - Use Python's fast PRNG / POSIX libc `lrand48` simulation to generate $1,000,000$ positive integers.
  - Count duplicates efficiently using set cardinality (`len(arr) - len(set(arr))`).
  - Resolve duplicates by searching the nearest free integral offset ($\pm 1, \pm 2, \dots$) with a visited hash set.
  - Standardize all timing using `time.perf_counter_ns()` reporting in microseconds ($\mu\text{s}$), discussing OS monotonic timers (e.g. `clock_gettime(CLOCK_MONOTONIC)` in Linux).
- **Rationale**: High execution speed for $10^6$ items while satisfying both POSIX/Linux timing concepts and microsecond precision requirements.

### Decision 4: Implementation of Assignment 4 (Order Statistics / i-th Sorted Element)
- **Choice**:
  - Priority Queue: Maintain a max-heap of size $i+1$ (or min-heap of size $n-i$) using Python's `heapq` ($O(n \log k)$ complexity).
  - Quickselect: Implement recursive/in-place Quicksort partition (Lomuto or Hoare) with expected $O(n)$ time complexity.
  - Baseline: Standard Timsort (`sorted(arr)[i]`, $O(n \log n)$).
  - Test across index locations: near $0$ (minimums), median ($n/2$), and near $n-1$ (maximums) to demonstrate heap vs quickselect trade-offs.

### Decision 5: Implementation of Assignment 5 (Loop Complexity Analysis)
- **Choice**: Implement exact loop counters for the 4 snippets:
  - Code 1: $\sum_{i=1}^n i = \frac{n(n+1)}{2} = O(n^2)$.
  - Code 2: Identify the paper's apparent typo `j = n/2` vs intended `j = j // 2`. Explain both and evaluate the intended divide-by-2 loop: $\sum n/2^k = O(n)$.
  - Code 3: $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} = O(n^3)$.
  - Code 4: $\log_2 n \times n = O(n \log n)$.
- **Rationale**: Accurately counts operations and measures wall-clock time against asymptotic theoretical predictions.

## Risks / Trade-offs

- **[Risk] Nearest free integer search on 1M items could be slow if collisions are high**:
  - *Mitigation*: Choose a sufficiently wide random range (e.g., $1$ to $2,000,000$) or limit the resolution benchmark sample to maintain sub-second runtime.
- **[Risk] Code 2 infinite loop if implemented as `j = n/2`**:
  - *Mitigation*: Explicitly document the errata in the assignment sheet; implement both the literal behavior note and the intended logarithmic-step variant ($j = j // 2$).
