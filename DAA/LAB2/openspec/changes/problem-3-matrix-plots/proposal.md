## Why

DAA Lab Assignment 2 (Problem 3) requires students to implement and benchmark matrix algorithms (Matrix Addition, Matrix Transpose, and Matrix Multiplication) on square matrices of sizes 10x10, 50x50, 100x100, 200x200, and 500x500, and generate plots of Matrix Size vs Execution Time to compare empirical scaling against theoretical $\mathcal{O}(n^2)$ quadratic and $\mathcal{O}(n^3)$ cubic complexities. While Problem 1 and Problem 2 have standalone SVG plots, Problem 3 currently only prints console text tables.

## What Changes

- Add standalone SVG plot generator for matrix operations matching the aesthetic, crisp vector styling, and structure of `results/search_complexity_plot.svg` and `results/sorting_complexity_plot.svg`.
- Plot Matrix Size ($N$) on the X-axis vs Execution Time (ms) on the Y-axis across Matrix Addition ($\mathcal{O}(n^2)$), Matrix Transpose ($\mathcal{O}(n^2)$), and Matrix Multiplication ($\mathcal{O}(n^3)$).
- Add support for generating an interactive HTML report (`results/matrix_analysis.html`) and ASCII terminal charts for console visual verification.
- Enhance `problem3_matrix.py` to automatically execute benchmarks, export Markdown and CSV metrics (`results/matrix_results_table.md`, `results/matrix_metrics.csv`), and output `results/matrix_complexity_plot.svg` and `results/matrix_analysis.html`.
- Maintain zero external dependencies (pure Python standard library).

## Capabilities

### New Capabilities
- `matrix-visualization`: Standalone vector SVG plotting (Matrix Size vs Execution Time), ASCII terminal graphs, and comprehensive HTML report generation for matrix operation benchmarks (Addition, Transpose, Multiplication).

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**: `problem3_matrix.py` (and supporting functions in `src/visualizer.py`).
- **Generated Artifacts**: `results/matrix_complexity_plot.svg`, `results/matrix_analysis.html`, `results/matrix_metrics.csv`, `results/matrix_results_table.md`.
- **Dependencies**: Python standard library only (`time`, `random`, `pathlib`, `csv`, `os`).
