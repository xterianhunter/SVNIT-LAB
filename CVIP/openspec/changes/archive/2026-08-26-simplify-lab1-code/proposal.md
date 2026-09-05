## Why

The current `lab1_analysis.c` implementation spans nearly 600 lines with extensive boilerplate, verbose multi-line ASCII charting, and redundant helper structures that obscure the core image processing logic for an academic CVIP lab assignment. Simplifying the codebase to use a lightweight `Image` struct and concise, focused functions will improve readability, maintainability, and clarity while preserving all required analytical outputs (dimensions, min/max, mean, variance/contrast, dark/medium/bright range classification, 256-bin histograms, comparative evaluation, ROI analysis, brightness transformation, iso-mean demonstration, and thresholding assessment).

## What Changes

- **Streamlined Image Data Structure**: Replace multiple overly complex structures with a clean, minimal `Image` struct (`int w, h; unsigned char *data;`).
- **Concise PGM I/O**: Simplify P5 binary PGM reading and writing into compact routines with robust basic header parsing.
- **Unified Statistical Analysis**: Streamline statistics computation (min, max, mean, variance, std dev, range percentages) into straightforward loops without excessive helper wrappers.
- **Compact Histogram Representation**: Retain 256-bin histogram computation and print concise aggregated interval summaries instead of overly complex graphic rendering.
- **Direct ROI & Brightness Operations**: Keep region-of-interest calculation and pixel clamping transformations direct, short, and clear.
- **Concise Iso-Mean & Suitability Demonstrations**: Express the iso-mean mathematical proof and thresholding suitability assessment cleanly in concise print routines.
- **Drastic Line Count Reduction**: Reduce source code from 576 lines down to under 200 lines while retaining 100% of the lab's required analytical output.

## Capabilities

### New Capabilities
- `image-analysis`: Lightweight grayscale image reading, statistical analysis, histogram evaluation, range categorization, ROI analysis, brightness adjustment, and segmentation suitability assessment.

### Modified Capabilities
<!-- No existing capabilities to modify in main specs. -->

## Impact

- **Affected Code**: `lab1_analysis.c`, `Makefile` (compilation flags/targets remain standard C99 with `-lm`).
- **Dependencies**: Standard C library (`stdio.h`, `stdlib.h`, `math.h`, `string.h`) - zero external dependencies.
- **Output**: Clean, structured, concise terminal report answering all CVIP Lab 1 questions directly.
