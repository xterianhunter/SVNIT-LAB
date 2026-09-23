## Context

The user provided a specific LaTeX document preamble, page geometry, typography, and listing styles. The report is for:
- Student: Kishan Sahu (Enrollment No.: P26DS017)
- Course: M.Tech. I -- Semester I, Computer Vision and Image Processing (CSCS111/CSDS119)
- Department: Computer Science and Engineering Department, SVNIT, Surat
- Lab: Lab Assignment 6: Image Segmentation

All experimental code, console printouts, and generated visualization plots are located inside `lab6_image_segmentation.ipynb`.

See `proposal.md` and `specs/latex-report-generation/spec.md` for background and behavior specifications.

## Goals / Non-Goals

**Goals:**
- Extract all 6 plot outputs from `lab6_image_segmentation.ipynb` to standalone PNG files in a `figures/` directory.
- Create a complete, self-contained LaTeX document (`lab6_report.tex` and `main.tex`) adhering to the exact preamble and styling requested.
- Present mathematical equations and kernel matrices for:
  - Point detection ($3\times 3$) and Directional line masks ($0^\circ, 90^\circ, \pm 45^\circ$).
  - Edge detection operators (Roberts Cross, Prewitt, Sobel, Laplacian).
  - Iterative Global Thresholding and Otsu variance maximization.
  - Region growing formulation and similarity criterion.
- Include complete Python code blocks using `\begin{lstlisting}[style=code]` and verbatim stdout using `\begin{lstlisting}[style=output]`.
- Include all embedded figures using `\begin{figure}[H]` with clear captions.
- Include comprehensive comparative observations for Part A and Part B (grounding on the black cup vs gray background).

**Non-Goals:**
- Modifying the Jupyter notebook implementation.
- Omitting any code cells or outputs.

## Decisions

### 1. Document Structure & Filenames
- **Decision**: Save the primary LaTeX document as `lab6_report.tex` and provide a symlink/copy as `main.tex`.
- **Rationale**: Facilitates seamless compilation with standard tools (Overleaf, VSCode LaTeX Workshop, `latexmk`, etc.).

### 2. Automated Asset Extraction
- **Decision**: Use a Python extraction script to parse `lab6_image_segmentation.ipynb`, decode base64 PNGs into `figures/`, and retrieve the exact code and output text for insertion.
- **Rationale**: Prevents transcription errors, preserves exact code formatting, and ensures figure resolution is identical to the notebook.

### 3. Listings Style Mapping
- **Decision**: Wrap all Python code blocks with `style=code` and all terminal/standard output streams with `style=output` as defined in the user's template.
- **Rationale**: Directly honors the user's template style definitions.

## Risks / Trade-offs

- **[Special Character Escapes in LaTeX]**: Code or output strings containing `#`, `_`, `%`, `^`, or `$` must be properly handled inside listings blocks.
  - *Mitigation*: Using the `listings` environment (`\begin{lstlisting}`) natively preserves special characters without manual escaping.
