## Why

This change implements Problem 1 from DAA Lab Assignment 2 (CSDS103, SVNIT). It provides clean, modular, and dependency-free implementations of Linear Search and Binary Search, along with a comprehensive benchmarking suite that reads input arrays from files, benchmarks multiple search positions (beginning, middle, end, absent), outputs structured tabular metrics, generates execution time plots, and compares empirical findings against theoretical complexities ($O(1)$, $O(n)$, $O(\log n)$).

## What Changes

- Implement core searching algorithms:
  - **Linear Search**: Sequential scan algorithm ($O(1)$ best, $O(n)$ average/worst).
  - **Binary Search**: Divide-and-conquer search on sorted arrays ($O(1)$ best, $O(\log n)$ average/worst).
- Implement input file generation and parsing for array sizes 10, 50, 100, 200.
- Implement benchmarking harness evaluating 4 target cases per array size:
  - Element near beginning
  - Element near middle
  - Element near end
  - Element absent
- Implement high-resolution timing using `time.perf_counter_ns` with repeated iterations to capture microsecond/nanosecond-scale benchmarks reliably.
- Implement tabular output formatting (ASCII table and markdown/CSV export) and visualization generation (standalone SVG/HTML plot generator and terminal/ASCII graph generator).
- Provide theoretical vs experimental complexity analysis and summary documentation.

## Capabilities

### New Capabilities
- `searching-algorithms`: Implementation of Linear Search and Binary Search algorithms, file-based input processing, benchmark harness covering search position test cases, tabular results reporting, and visualization plotting.

### Modified Capabilities
<!-- None -->

## Impact

- **New files**:
  - `src/linear_search.py` & `src/binary_search.py` (or consolidated modular `src/searching.py`)
  - `src/benchmark.py` (benchmarking runner and table generator)
  - `src/plot_generator.py` (standalone SVG/HTML/ASCII visualizer)
  - `src/file_io.py` (generating and loading input files)
  - `main.py` (CLI entry point)
  - `data/` directory containing test input files (sizes 10, 50, 100, 200)
  - `results/` directory containing generated tables and plots
- **Dependencies**: Python standard library only (`time`, `random`, `math`, `sys`, `pathlib`, `csv`, `os`), ensuring 100% portability without external pip dependencies.
