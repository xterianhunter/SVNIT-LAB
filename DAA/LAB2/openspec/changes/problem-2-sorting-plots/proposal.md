## Why

DAA Lab Assignment 2 (Problem 2) requires students to evaluate sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort) across multiple input sizes and data configurations (Random, Already Sorted, Reverse Sorted), and to generate graphical plots of Input Size vs Execution Time comparing empirical performance with theoretical time complexities. While Problem 1 features a standalone SVG plot (`results/search_complexity_plot.svg`), Problem 2 (`problem2_sorting.py`) currently only outputs tabular text in the terminal and lacks graphical plots.

## What Changes

- Add standalone SVG plot generation for sorting algorithms matching the aesthetic, styling, and structure of `results/search_complexity_plot.svg` (clean vector graphics, multi-series plots for 3 algorithms across 3 input types, labeled axes, gridlines, and legend).
- Add support for generating an interactive HTML report (`results/sorting_analysis.html`) and ASCII terminal charts for quick console visualization.
- Enhance `problem2_sorting.py` to orchestrate benchmarking across sizes (e.g., 50, 100, 200, 500) and distributions, outputting `results/sorting_complexity_plot.svg`, `results/sorting_analysis.html`, and CSV/Markdown metrics.
- Keep implementation zero-dependency (using Python standard library for SVG/HTML rendering and file I/O).

## Capabilities

### New Capabilities
- `sorting-visualization`: Standalone vector SVG plotting (Input Size vs Execution Time), ASCII terminal graphs, and comprehensive HTML report generation for sorting algorithm benchmarks across Random, Sorted, and Reverse input distributions.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**: `problem2_sorting.py` (and optionally supporting modules in `src/`).
- **Generated Artifacts**: `results/sorting_complexity_plot.svg`, `results/sorting_analysis.html`, `results/sorting_metrics.csv`.
- **Dependencies**: Python standard library only (`time`, `random`, `pathlib`, `os`, `argparse`).
