## Context

See `proposal.md` and `specs/latex-report/spec.md`. The user provided a specific LaTeX document preamble with styling requirements:
- Document class `[12pt]{article}`
- A4 paper with 1 inch margins (`geometry`)
- Times-style font (`newtxtext, newtxmath`)
- `fancyhdr` with Student Name (`Kishan Sahu`), Enrollment Number (`P26DS017`), Department (`SVNIT Surat`), Course (`CSCS111/CSDS119`), and Title for Lab Assignment 5 ("Spatial and Frequency Domain Filtering")
- Custom listing styles: `code` (with syntax coloring, line numbers) and `output` (with gray background, no numbers)
- Paragraph formatting (`\parindent 0pt`, `\parskip 5pt`)

## Goals / Non-Goals

**Goals:**
- Extract all high-resolution figures from `lab5_solution.ipynb` into a `figures/` directory.
- Create `report.tex` strictly following the requested preamble and header format.
- Embed all code snippets using `style=code`, terminal outputs using `style=output`, figures using `\includegraphics`, and mathematical equations.
- Include comparative tables summarizing filter properties (Mean vs Gaussian vs Laplacian, Ideal vs Gaussian vs Butterworth, and Template Matching scales).
- Provide detailed theoretical descriptions and empirical observations for every task.
- Compile the document into `report.pdf`.

**Non-Goals:**
- Modifying the underlying solution notebook `lab5_solution.ipynb` (which is already finalized and verified).

## Decisions

### Decision 1: Direct figure export from the pre-executed notebook
- **Rationale**: The notebook already has the base64 PNG data for all rendered plots. A simple extraction script writes them into `figures/fig_spatial.png`, `figures/fig_dft.png`, `figures/fig_ilpf.png`, `figures/fig_ihpf.png`, `figures/fig_gauss.png`, `figures/fig_butter.png`, `figures/fig_comp.png`, and `figures/fig_template_matching.png`.

### Decision 2: Systematic sectional structure
- **Rationale**: Organizing each part with:
  1. *Mathematical Formulation & Objective*
  2. *Implementation Code*
  3. *Visual Results (Figures)*
  4. *Terminal Output & Metrics*
  5. *Comparative Analysis & Observations*
  ensures the report is rigorous, complete, and easy to grade.

### Decision 3: Comparative Summary Tables
- **Rationale**: Tables provide quick, structured summaries of noise reduction vs blur vs ringing across filter types and scales.

## Risks / Trade-offs

- **[Risk] LaTeX compiler availability** → *Mitigation*: Verify `pdflatex` is installed on system (`which pdflatex`); if not available, ensure `report.tex` is fully self-contained and ready for immediate compilation on Overleaf or local TeX distributions.
