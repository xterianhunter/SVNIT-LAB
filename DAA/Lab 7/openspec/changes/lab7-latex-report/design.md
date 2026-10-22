## Context

See `proposal.md` for background. The user provided an exact LaTeX preamble template including package imports, font configurations, page layout, custom listing styles (`code` and `output`), running headers with student details (`Kishan Sahu`, `P26DS017`), and departmental title block.

## Goals / Non-Goals

**Goals:**
- Faithfully apply the user's preamble and header formatting in `report.tex`.
- Provide a rigorous, academic-grade lab report containing all problem formulations, algorithmic theory, complexity derivations, clean code listings, actual console outputs, collision proofs, and experimental visualization figures.
- Extract or export the three benchmark plots as high-resolution PNG images (`plot_time_vs_n.png`, `plot_time_vs_m.png`, `plot_comp_vs_n.png`) so the LaTeX document compiles cleanly with embedded figures.
- Verify compilation with `pdflatex` or ensure syntax cleanliness.

**Non-Goals:**
- Creating custom Beamer slides or changing document layout parameters outside the requested template.

## Decisions

1. **Title Adaptation**:
   - Keep the exact structure and styling from the user's snippet, updating "Assignment 5" to "Assignment 7: String Matching Algorithms" to match Lab 7.
2. **Visual Figures Integration**:
   - Export the 3 matplotlib figures generated during notebook execution into PNG files (`plot_time_vs_n.png`, `plot_time_vs_m.png`, `plot_comp_vs_n.png`).
   - Embed them with `\begin{figure}[H] \centering \includegraphics... \end{figure}`.
3. **Listings Organization**:
   - Format each problem cleanly:
     - Mathematical description & pseudocode/concept
     - Complexity analysis (Time and Space)
     - Implementation block (`style=code`)
     - Terminal output block (`style=output`)
     - In-depth question/analysis discussion (e.g. worst-case comparisons, hash collision spurious hits).

## Risks / Trade-offs

- **[Risk]** Missing LaTeX compiler on system if pdflatex isn't installed.
  - *Mitigation*: Check for pdflatex / tectonic / latexmk. If present, compile `report.tex` into `report.pdf`. Ensure LaTeX syntax is 100% compliant with standard TeX Live.
