## Why

In `Lab2.tex`, the three empirical performance comparison tables for parallel matrix multiplication (Problem Statement 3) are too wide for standard 1-inch margins on A4 paper. This is primarily caused by long single-line table header titles such as "Decomposition Method" and "Throughput (GFLOPS)". Splitting these headers across two vertical lines significantly reduces table width, eliminates horizontal margin overflow, and improves visual clarity.

## What Changes

- Format table headers across two stacked lines in all three matrix multiplication tables ($500 \times 500$, $1000 \times 1000$, and $1500 \times 1500$):
  - Split `Decomposition Method` into `Decomposition` on line 1 and `Method` on line 2.
  - Split `Throughput (GFLOPS)` into `Throughput` on line 1 and `(GFLOPS)` on line 2.
- Ensure consistent column formatting and compilation cleanly via `pdflatex` without margin clipping or layout distortion.

## Capabilities

### New Capabilities
- `lab-report-formatting`: Defines layout and multi-line header formatting requirements for LaTeX benchmark tables in `Lab2.tex`.

### Modified Capabilities

## Impact

- `Lab2.tex`: Header rows in the matrix multiplication benchmark tables updated to two-line formats.
- `Lab2.pdf`: Generated document reflects compact table column widths within standard margins.
