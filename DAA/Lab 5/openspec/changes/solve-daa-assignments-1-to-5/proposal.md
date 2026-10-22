## Why

CS103 (Design and Analysis of Algorithms) Lab Assignments 1 through 5 require implementing fundamental algorithmic paradigms—Divide and Conquer, vector duplicate resolution with high-resolution timing, selection algorithms (heaps vs. Quicksort partition), and empirical loop cost analysis. Creating a concise, self-contained Jupyter Notebook (`daa_assignments_1_to_5.ipynb`) solves all five assignments while keeping code minimal, clear, and focused strictly on the specified tasks without unnecessary boilerplate.

## What Changes

- Create a single Jupyter Notebook `daa_assignments_1_to_5.ipynb` covering Assignments 1 through 5:
  - **Assignment 1**: Closest Pair of Points in 2D using both brute-force ($O(n^2)$) and divide-and-conquer ($O(n \log n)$) algorithms, benchmarked with execution times and theoretical vs. empirical complexity comparisons.
  - **Assignment 2**: Generation of a vector with $\ge 1,000,000$ positive random integers, duplicate counting, duplicate resolution rounding to nearest free integer, and timing comparison of removal strategies.
  - **Assignment 3**: Microsecond-resolution timing solution using Linux/Python high-resolution timers (`time.perf_counter_ns()` formatted to $\mu\text{s}$) with discussion of timer precision.
  - **Assignment 4**: Finding the element at index $i$ as if the array were sorted using:
    - Min/Max Priority Queue (Heap) approach.
    - Quickselect algorithm using the Quicksort partition routine.
    - Comparison of heap selection, Quickselect, and full sort ($O(n \log n)$).
  - **Assignment 5**: Cost and asymptotic analysis of the 4 provided code loop snippets (Code 1: $O(n^2)$, Code 2: $O(n)$, Code 3: $O(n^3)$, Code 4: $O(n \log n)$) with empirical timing benchmarks against theoretical models.

## Capabilities

### New Capabilities
- `daa-lab-solutions`: Concise, self-contained implementations, benchmarks, and complexity analyses for DAA Lab Assignments 1 through 5 in a single Jupyter Notebook.

### Modified Capabilities
*(None)*

## Impact

- Adds `daa_assignments_1_to_5.ipynb` in the workspace root.
- Requires standard Python 3 runtime with standard modules (`random`, `time`, `math`, `heapq`) and lightweight visualization (`matplotlib`).
