## Why

This change implements Problem 2 from DAA Lab Assignment 2 (CSDS103, SVNIT). It provides clean, standalone implementations of three classical comparison-based sorting algorithms—Bubble Sort, Selection Sort, and Insertion Sort—and benchmarks their execution times across multiple input sizes and distinct input configurations (Random, Already Sorted, Reverse Sorted) to experimentally validate theoretical $\mathcal{O}(n)$, $\mathcal{O}(n^2)$ best/worst case complexities.

## What Changes

- Implement core sorting algorithms from first principles:
  - **Bubble Sort**: Adjacent element comparison with early termination optimization ($\mathcal{O}(n)$ best, $\mathcal{O}(n^2)$ worst/average).
  - **Selection Sort**: Minimum element selection and in-place swapping ($\Theta(n^2)$ best/worst/average).
  - **Insertion Sort**: Incremental shifting insertion ($\mathcal{O}(n)$ best, $\mathcal{O}(n^2)$ worst/average).
- Benchmark performance across multiple input sizes (e.g., 50, 100, 200, 500, 1000) on 3 input distributions:
  - Randomly ordered input
  - Already sorted input
  - Reverse sorted input
- Measure high-resolution execution time and operation counts (comparisons and swaps/shifts).
- Tabulate experimental results and generate execution time vs. input size plots.
- Provide a dedicated, clean, and concise single-file script `problem2_sorting.py` suited for M.Tech lab evaluation.

## Capabilities

### New Capabilities
- `sorting-algorithms`: Implementation of Bubble Sort, Selection Sort, and Insertion Sort, benchmark suite across 3 input types, tabular reporting, and complexity analysis.

### Modified Capabilities
<!-- None -->

## Impact

- **New files**:
  - `problem2_sorting.py` (self-contained, clean script for M.Tech student lab submission)
  - Result metrics and plot outputs for Problem 2
- **Dependencies**: Python standard library only (`time`, `random`, `os`), ensuring 100% portability.
