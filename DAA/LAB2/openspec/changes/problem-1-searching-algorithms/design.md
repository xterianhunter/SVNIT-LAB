## Context

See `proposal.md` for problem background and motivation. The goal is to implement and experimentally analyze Linear Search and Binary Search on integer arrays of sizes 10, 50, 100, and 200 loaded from files across 4 target cases (beginning, middle, end, absent).

## Goals / Non-Goals

**Goals:**
- Provide clean, simple, standalone Python implementations of Linear Search and Binary Search without relying on built-in search functions.
- Read integer datasets from formatted input files (`data/input_<N>.txt`).
- Execute a rigorous benchmark suite measuring average search latency in nanoseconds using `time.perf_counter_ns()` with repeated trials ($K = 10,000$) to eliminate timing jitter on small arrays.
- Output clean tabular summaries in ASCII, Markdown, and CSV formats.
- Generate high-quality visual plots (SVG, interactive HTML, and ASCII terminal graph) with zero third-party pip dependencies.
- Provide theoretical vs empirical complexity comparison ($O(1)$, $O(n)$, $O(\log n)$).

**Non-Goals:**
- Implementing sorting algorithms or matrix algorithms (these belong to Problem 2 and Problem 3 of Lab 2).
- Requiring heavy third-party plotting frameworks (e.g. mandatory matplotlib) that might fail if pip/GUI packages are missing.

## Decisions

### Decision 1: Architecture & Module Structure
- **Choice**: Separate clean modules under `src/`:
  - `src/searching.py`: Pure implementations of `linear_search` and `binary_search` returning `(index, comparisons)`.
  - `src/file_io.py`: File utilities for creating, writing, and loading array datasets from `data/`.
  - `src/benchmark.py`: Timing harness using `time.perf_counter_ns()` over $10,000$ iterations.
  - `src/visualizer.py`: Standalone SVG and HTML/terminal chart generator.
  - `main.py`: Entry point orchestrating data generation, benchmarking, table printing, and chart output.
- **Alternatives considered**: Single monolithic script. *Rejected* in favor of modular, readable code that separates algorithm logic from benchmarking and visualization.

### Decision 2: High-Precision Benchmark Timing
- **Choice**: For small array sizes ($N \in \{10, 50, 100, 200\}$), individual searches complete in $< 1 \mu s$. To measure accurately without timer resolution noise, execute each test case across $K = 10,000$ iterations and take the mean execution time per operation in nanoseconds ($\text{ns}$).
- **Alternatives considered**: Single execution with `time.time()`. *Rejected* due to coarse timer resolution and high OS scheduler jitter.

### Decision 3: Zero-Dependency Plot Generation
- **Choice**: Generate standalone, vector-crisp SVG files alongside an interactive HTML dashboard and ASCII console graph. If `matplotlib` is detected in the environment, also export PNG; otherwise SVG/HTML ensures rich visual output without requiring `pip install`.
- **Alternatives considered**: Matplotlib only. *Rejected* because matplotlib is not pre-installed in this environment.

## Risks / Trade-offs

- **[Risk]** Clock noise / CPU throttling during benchmarking → **Mitigation**: Warm up CPU cycles before timing, run multiple repeated iterations ($10,000$ loops), and use monotonic high-resolution `perf_counter_ns`.
- **[Risk]** Array unsorted for Binary Search → **Mitigation**: Ensure input arrays loaded for searching are sorted before performing binary search, while linear search runs on both or identical sorted arrays for fair positional comparison.
