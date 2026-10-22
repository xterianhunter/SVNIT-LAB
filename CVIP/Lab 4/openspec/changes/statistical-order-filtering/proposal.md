## Why

Implement Lab Assignment 4 (Computer Vision and Image Processing - CSCS111/CSDS119) on Statistical Order Filtering. The goal is to provide a clean, concise, and complete Jupyter Notebook demonstrating order statistics filters (median, min, max, midpoint, alpha-trimmed mean, 25th/75th percentiles) on the Cameraman image across neighborhood window sizes ($3 \times 3$, $5 \times 5$, $7 \times 7$) with side-by-side visual comparisons and brief observations.

## What Changes

- Create a single, self-contained Jupyter Notebook (`cvip_lab4.ipynb`) to solve all tasks in `cvip_lab4.pdf`.
- Implement core statistical order filters concisely:
  - Median filter
  - Min and Max filters
  - Midpoint filter: $\frac{\min + \max}{2}$
  - Alpha-trimmed mean filter
  - Ranked percentile filters (25th and 75th percentiles)
- Add noise generation (salt-and-pepper and Gaussian noise) to the Cameraman image (`Filtering-Cameraman.png`).
- Evaluate all filters across $3 \times 3$, $5 \times 5$, and $7 \times 7$ window sizes.
- Display filtered output grids and document observations on noise removal vs. edge and detail preservation.

## Capabilities

### New Capabilities
- `statistical-order-filtering`: Implementation and evaluation of order-statistic filtering algorithms (median, min, max, midpoint, alpha-trimmed mean, percentiles) across window sizes on noisy Cameraman images with visual and comparative analysis.

### Modified Capabilities
None.

## Impact

- Creates `cvip_lab4.ipynb` in the workspace root.
- Uses `Filtering-Cameraman.png` present in the workspace.
- Minimal standard dependencies: `numpy`, `matplotlib`, `opencv-python` / `PIL`.
