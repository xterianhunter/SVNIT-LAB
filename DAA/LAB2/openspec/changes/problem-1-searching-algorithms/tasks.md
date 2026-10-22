## 1. Project Setup and File I/O

- [x] 1.1 Create project directory structure (`src/`, `data/`, `results/`) and verify folders exist
- [x] 1.2 Implement `src/file_io.py` to generate and load integer array files for sizes 10, 50, 100, and 200, and verify file reading

## 2. Core Searching Algorithms

- [x] 2.1 Implement `src/searching.py` containing `linear_search` and `binary_search` without built-in libraries and verify basic unit correctness on both present and absent elements

## 3. Benchmarking and Tabular Reporting

- [x] 3.1 Implement `src/benchmark.py` covering 4 search positions (beginning, middle, end, absent) with high-resolution `time.perf_counter_ns` multi-iteration timing
- [x] 3.2 Add tabular result exporters in `src/benchmark.py` for formatted console tables, `results/results_table.md`, and `results/metrics.csv`

## 4. Visualization and Verification

- [x] 4.1 Implement `src/visualizer.py` to generate standalone SVG charts, interactive HTML report, and ASCII terminal graphs
- [x] 4.2 Implement `main.py` entry point orchestrating full execution, verify generated table and plot artifacts, and document theoretical vs empirical complexity comparison
