## Why

The current LaTeX laboratory report (`CVIP_Lab7_Report.tex`) contains truncated or missing Python code snippets across multiple sections. Specifically, Questions 2, 3, and 6 contain partial code blocks that end abruptly, while Question 7 (Synthetic Scene Simulation) and Part B (Experimental Investigation of Direct vs. Shadowed Illumination) lack code listings entirely. To ensure academic rigor, completeness, and full reproducibility of the lab results, all Python simulation, analysis, and plotting implementations must be properly and elegantly incorporated into the report.

## What Changes

- Complete and format the Python code listings in `CVIP_Lab7_Report.tex` across all sections:
  - **Part A, Q1**: Ensure complete code for inverse-square law and flux scaling across distances and surface areas.
  - **Part A, Q2**: Replace truncated snippet with complete sensitivity analysis implementation (sweeps for power, distance, angle, and reflectance).
  - **Part A, Q3**: Replace truncated snippet with complete diffuse (Lambertian) vs. specular (Phong) reflection simulation and multi-angle plotting.
  - **Part A, Q6**: Expand snippet to include full image formation pipeline, sensor quantization, saturation clipping, and response curve plotting.
  - **Part A, Q7**: Add complete Python code listing for 3D hemispherical scene generation, direct overhead vs. oblique side lighting, difference mapping, profile slicing, and histogram generation.
  - **Part B**: Add complete Python code listing for experimental direct vs. shadow illumination analysis, metric calculations (mean, std), and comparative visualizations.
- Ensure all listings use LaTeX `listings` environment (`\begin{lstlisting}[style=code]`) with clean indentation, proper line wrapping, and syntax highlighting.
- Verify LaTeX document compilation with `pdflatex` to produce an updated, error-free PDF report.

## Capabilities

### New Capabilities
- `report-code-inclusion`: Complete and structured inclusion of all simulation and experimental Python code listings into the CVIP Lab 7 LaTeX report.

### Modified Capabilities
<!-- None -->

## Impact

- Modifies `CVIP_Lab7_Report.tex` to include complete Python source code for all lab questions.
- Recompiles `CVIP_Lab7_Report.pdf` (or `CVIP_Lab7.pdf`).
- Does not modify simulation logic or output figures.
