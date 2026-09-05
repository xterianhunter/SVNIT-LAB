# Proposal: LaTeX Report Generation for CVIP Lab 4

## Why

The implementation and empirical results for CVIP Lab 4 (Statistical & Order-Statistic Filtering) have been developed and executed in `cvip_lab4.ipynb`. To fulfill academic submission requirements, a publication-quality LaTeX document needs to be created. This report must integrate all elements from the notebook—including problem formulation, mathematical background, complete Python implementations, textual outputs, high-resolution figures extracted from the notebook execution, comparative summary tables, and in-depth observations—while strictly adhering to the specified LaTeX document class, page layout, fonts, listings styles, and institutional header.

## What Changes

- Create a complete LaTeX document `cvip_lab4_report.tex` utilizing the exact `\documentclass[12pt]{article}`, Times-style font (`newtxtext, newtxmath`), 1-inch margins, fancy header with student metadata (`Kishan Sahu`, `P26DS017`), customized `listings` environments (`code` and `output`), and institutional title block.
- Extract high-resolution image assets from the executed cells of `cvip_lab4.ipynb` into a dedicated `figures/` directory for inclusion via `\includegraphics`.
- Structure the report systematically:
  1. Header & Title Block (SVNIT, CSE Dept, M.Tech I Sem I, CVIP CSCS111/CSDS119 Lab Assignment 4).
  2. Aim, Objectives, and Theoretical Foundations of Statistical & Order-Statistic Filters (Median, Min, Max, Midpoint, Alpha-Trimmed Mean, Percentile).
  3. Experimental Setup & Noise Models (Salt & Pepper, Additive Gaussian).
  4. Vectorized Algorithm Design & Python Implementations using formatted `lstlisting` (code style).
  5. Experimental Results, Embedded Figures, and Console Outputs (formatted using `output` style).
  6. Parameter Study: Neighborhood Size Variations ($3 \times 3, 5 \times 5, 7 \times 7$).
  7. Noise Robustness Analysis: Impulse Noise vs Additive Gaussian Noise.
  8. Comprehensive Comparative Summary Table (filter, complexity, noise type suitability, edge preservation characteristics).
  9. Detailed Critical Observations and Conclusions.
- Ensure the LaTeX file compiles cleanly to PDF using `pdflatex` or `latexmk`.

## Capabilities

### New Capabilities
- `latex-report`: Capability to generate a publication-ready LaTeX lab report with extracted figures, listings, tables, and comparative analysis from a Jupyter Notebook.

### Modified Capabilities
*(None)*

## Impact

- **Files Created**:
  - `cvip_lab4_report.tex`: Standalone LaTeX report.
  - `figures/`: Extracted PNG figures from the notebook (`original_and_noisy.png`, `filters_sp_3x3.png`, `neighborhood_sizes.png`, `gaussian_comparison.png`).
- **Dependencies**: TeX Live distribution (`pdflatex`, `listings`, `graphicx`, `amsmath`, `newtxtext`, `newtxmath`, `fancyhdr`).
