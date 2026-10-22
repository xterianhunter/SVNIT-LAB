## Why

This change provides a clean, minimal Jupyter Notebook (`lab5_solution.ipynb`) that solves all problems in CVIP Lab Assignment 5 (CVIP_Lab5.pdf), covering Part A (Spatial and Frequency Domain Filtering) and Part B (Cross-Correlation for Template Matching). The goal is to keep the code as simple, readable, and concise as possible without unnecessary boilerplate or over-engineering.

## What Changes

- Create a single, self-contained, simple Jupyter notebook `lab5_solution.ipynb` containing:
  - **Part A.1: Spatial Domain Filtering**: Mean, Gaussian, and Laplacian filtering on the Cameraman image across different neighborhood/kernel sizes with concise observations.
  - **Part A.2: Discrete Fourier Transform (DFT)**: 2D DFT computation, magnitude spectrum, phase spectrum, and IDFT reconstruction.
  - **Part A.3: Ideal Low-Pass Filter (ILPF)**: Circular ILPF implementation in frequency domain with varying $D_0$ and observations.
  - **Part A.4: Ideal High-Pass Filter (IHPF)**: Circular IHPF implementation in frequency domain with varying $D_0$ and observations.
  - **Part A.5: Gaussian Low-Pass & High-Pass Filters (GLPF & GHPF)**: Implementation in frequency domain with varying $D_0$ and comparison observations.
  - **Part A.6: Butterworth Low-Pass & High-Pass Filters (BLPF & BHPF)**: Implementation in frequency domain with varying $D_0$ and orders $n$, comparing ILPF, GLPF, and BLPF.
  - **Part B: Cross-Correlation Template Matching**: Template matching using OpenCV / NumPy cross-correlation between shelf image and product template, drawing a blue bounding box around the best match with observations.

## Capabilities

### New Capabilities
- `lab5-filtering-and-matching`: Implements concise spatial domain filtering, 2D DFT analysis, frequency domain filters (Ideal, Gaussian, Butterworth), and template matching via cross-correlation.

### Modified Capabilities
<!-- None -->

## Impact

- **New Files**: `lab5_solution.ipynb`
- **Dependencies**: Uses standard Python data science / CV libraries: `numpy`, `opencv-python`, `matplotlib`, and `scipy`/`skimage` (for cameraman dataset image fallback).
- **Breaking Changes**: None.
