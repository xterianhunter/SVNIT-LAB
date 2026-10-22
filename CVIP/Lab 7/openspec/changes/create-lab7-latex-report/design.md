## Context

The user provided an institutional LaTeX template from SVNIT Surat with custom styling (geometry, newtxtext/newtxmath, fancyhdr, listings styles for `code` and `output`). The objective is to assemble a short, clean, complete LaTeX report (`CVIP_Lab7_Report.tex`) for Lab Assignment 7 (Radiometry and Image Formation), including codes, outputs, figures, and observations.

## Goals / Non-Goals

**Goals:**
- Faithfully preserve the user-provided preamble, headers (Kishan Sahu, P26DS017), department banner, and listings styles.
- Export all experiment figures from the verified solution pipeline into a dedicated `figures/` directory.
- Incorporate code blocks (`style=code`), terminal/numerical output blocks (`style=output`), and high-resolution figures into `CVIP_Lab7_Report.tex`.
- Keep explanations and observations concise and focused on radiometry principles.

**Non-Goals:**
- Exclude Part A Questions 4 and 5 (as instructed).
- Avoid overly lengthy document padding or unnecessary boilerplate.

## Decisions

### Decision: Dedicated Figures Directory and Image Naming
- **Choice**: Export simulation plots into `figures/` with clear filenames:
  - `figures/q1_illumination.png`
  - `figures/q2_sensitivity.png`
  - `figures/q3_reflection.png`
  - `figures/q6_pipeline.png`
  - `figures/q7_synthetic_scene.png`
  - `figures/part_b_investigation.png`
- **Rationale**: Keeps the project root clean, reproducible, and easy to package for Overleaf or local compilation.

### Decision: Document Layout and Float Management
- **Choice**: Use `[H]` float specifiers with proportional scaling (`width=0.75\textwidth` to `0.85\textwidth`) and tight spacing (`\textfloatsep=10pt`, `\floatsep=10pt`) as configured in the user's template.
- **Rationale**: Prevents float drift, ensuring code, output, figure, and observation stay logically grouped together on the page.

## Risks / Trade-offs

- [Risk] TeX compiler (`pdflatex`) is not installed in the current environment.
  → Mitigation: Validate the `.tex` file structure carefully against standard TeXLive syntax, ensure all referenced figure paths exist, and provide clear compilation instructions for Overleaf / TeXLive.
