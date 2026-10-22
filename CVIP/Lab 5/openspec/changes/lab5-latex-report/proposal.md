## Why

The student needs a publication-quality LaTeX lab report (`report.tex`) for CVIP Lab Assignment 5 ("Spatial and Frequency Domain Filtering") matching the exact departmental header, preamble, and styling guidelines. The document must comprehensively incorporate all content from `lab5_solution.ipynb`: Python code listings, terminal outputs, high-resolution figures, analytical comparison tables, and detailed observations covering Part A (Spatial Filtering, 2D DFT, ILPF, IHPF, GLPF, GHPF, BLPF, BHPF) and Part B (Cross-Correlation Template Matching).

## What Changes

- Create an image export script to extract all output figures from `lab5_solution.ipynb` into a dedicated `figures/` directory.
- Create `report.tex` using the exact user-specified preamble, geometry, fonts, header (`Name: Kishan Sahu`, `Enrollment No.: P26DS017`, `SVNIT, Surat`, `Lab Assignment 5`), listings styles (`code` and `output`), parindent, and parskip.
- Structure the report systematically into:
  - **Part A.1**: Spatial Domain Filtering (Mean, Gaussian, Laplacian, Sharpening, neighborhood size comparisons, output images, and comparison table).
  - **Part A.2**: 2D Discrete Fourier Transform (Mathematical definition, 2D DFT, centered magnitude and phase spectra, IDFT reconstruction, and error metrics).
  - **Part A.3**: Ideal Low-Pass Filter (Transfer function, cutoff $D_0 \in \{20, 50, 80\}$, figures, and Gibbs ringing analysis).
  - **Part A.4**: Ideal High-Pass Filter (Transfer function, cutoff $D_0 \in \{20, 50, 80\}$, figures, and edge isolation analysis).
  - **Part A.5**: Gaussian Low-Pass & High-Pass Filters (Transfer functions, smooth decay without ringing, figures, and comparative observations).
  - **Part A.6**: Butterworth Low-Pass & High-Pass Filters (Transfer functions, order $n \in \{1, 2, 4\}$ effects, comprehensive comparison table of Ideal vs Gaussian vs Butterworth).
  - **Part B**: Exploratory Problem - Cross-Correlation Template Matching (Formulation, scale mismatch explanation, multi-scale normalized cross-correlation algorithm, bounding box detection at $(247, 235)$ with peak correlation $0.968$, and figures).
- Verify compilation of `report.tex` to `report.pdf` using `pdflatex`.

## Capabilities

### New Capabilities
- `latex-report`: Generates and compiles a complete, publication-ready LaTeX lab report with embedded code, outputs, figures, comparison tables, and observations.

### Modified Capabilities
<!-- None -->

## Impact

- **New Files**: `report.tex`, `figures/*.png`, and compiled `report.pdf`.
- **Dependencies**: TeX Live / `pdflatex` (standard Linux packages).
- **Breaking Changes**: None.
