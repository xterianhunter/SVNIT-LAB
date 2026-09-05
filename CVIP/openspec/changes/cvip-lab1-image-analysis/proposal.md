## Why

This change provides a complete, clean, and beginner-friendly C solution for SVNIT CVIP Lab Assignment 1 ("Understanding and Analysing Digital Images Using C"). It enables students to read standard Netpbm grayscale images (PGM format), store pixel matrices in basic arrays, calculate statistical properties (min, max, mean, contrast/variance), compute intensity histograms, partition intensities into dark/medium/bright bands, analyze sub-regions (ROI), modify pixel brightness, and mathematically analyze differences and thresholding feasibility.

## What Changes

- Introduce a modular C program (`lab1_analysis.c`) implementing pure C array-based image analysis operations for grayscale PGM images (`sample_01.pgm` and `sample_02.pgm`).
- Implement PGM (P5/P2) header parsing and raw pixel loading without external dependencies.
- Compute fundamental image statistics: dimensions ($W \times H$), min intensity, max intensity, average intensity, and contrast (standard deviation/variance).
- Compute 256-bin grayscale intensity histograms with an ASCII representation for terminal visualization.
- Categorize pixel intensities into three standard ranges: Dark ($[0, 85]$), Medium ($[86, 170]$), and Bright ($[171, 255]$), calculating exact percentages.
- Perform comparative analysis between the two input images to identify which is brighter, darker, or has higher contrast based on numerical metrics.
- Perform Region of Interest (ROI) extraction and separate statistical profiling on distinct image regions.
- Perform brightness transformation (additive offset with $[0, 255]$ clipping) and compare before/after statistics and histogram shifts, with optional output PGM export.
- Investigate and demonstrate how visually distinct images can share identical average intensity.
- Provide analytical conclusions on thresholding suitability based on histogram bimodality and contrast.

## Capabilities

### New Capabilities
- `image-analysis`: Grayscale PGM image reading, array-based pixel statistics computation, histogram generation, range partitioning, comparative metrics, ROI analysis, brightness adjustment, and thresholding evaluation.

### Modified Capabilities
<!-- None: Initial implementation -->

## Impact

- **Code**: Adds `lab1_analysis.c` and a simple `Makefile` (or build command) for compilation.
- **Dependencies**: None beyond standard C standard library (`stdio.h`, `stdlib.h`, `math.h`, `string.h`).
- **Data**: Reads existing `sample_01.pgm` and `sample_02.pgm` in the workspace.
