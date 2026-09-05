# Design: LaTeX Lab 4 Report Generation

## Context

See `proposal.md` for motivation and background. The source material is contained entirely within `cvip_lab4.ipynb`, which contains runnable Python scripts, executed cell console streams, base64-encoded PNG figures from `matplotlib`, and analytical markdown text. The user has provided an exact LaTeX preamble, page geometry, font specifications (`newtxtext`, `newtxmath`), custom `listings` environments, and header structure.

## Goals / Non-Goals

**Goals:**
- Produce a clean, self-contained LaTeX document `cvip_lab4_report.tex` strictly adopting the requested preamble, packages, styles, and SVNIT header format.
- Automatically extract embedded base64 figure attachments from `cvip_lab4.ipynb` into high-resolution PNG files in a dedicated `figures/` folder.
- Represent code snippets using `\begin{lstlisting}[style=code]` and console outputs using `\begin{lstlisting}[style=output]`.
- Provide complete mathematical definitions of statistical order filters and detailed tabular comparisons.
- Ensure the LaTeX code compiles without syntax errors or missing image errors under `pdflatex`.

**Non-Goals:**
- Modifying the underlying algorithm implementations in `cvip_lab4.ipynb`.
- Introducing external non-standard LaTeX packages beyond those provided in the template.

## Decisions

1. **Figure Extraction Strategy**:
   - *Decision*: Write a Python utility script to parse the notebook JSON, decode the `image/png` base64 strings from output cells, and save them with semantic names:
     - `figures/original_and_noisy.png` (from Cell 2)
     - `figures/filters_sp_3x3.png` (from Cell 6)
     - `figures/neighborhood_sizes.png` (from Cell 8)
     - `figures/gaussian_comparison.png` (from Cell 10)
   - *Alternative Considered*: Re-running the notebook or saving plots manually. Parsing existing executed cells is faster, deterministic, and preserves the exact random seed execution already visible in the notebook.

2. **Header Adaptation**:
   - *Decision*: Keep the user's requested header block structure and fonts exactly, updating the course and assignment details to match the actual lab:
     - Department: Computer Science and Engineering Department, SVNIT, Surat
     - Program: M.Tech. I -- Semester I
     - Course: Computer Vision and Image Processing (CSCS111/CSDS119)
     - Lab Assignment: Lab Assignment 4
     - Topic: Statistical & Order-Statistic Filtering
     - Header Left: Name: Kishan Sahu
     - Header Right: Enrollment No.: P26DS017
   - *Alternative Considered*: Leaving "Dynamic Programming (CSDS103)" as literally in the snippet. We should reflect CVIP Lab 4 while preserving the exact layout, fonts, and spacing.

3. **Code and Output Typography**:
   - *Decision*: Use the user's defined `\lstdefinestyle{code}` for Python source code blocks and `\lstdefinestyle{output}` for terminal / console outputs, setting `showstringspaces=false` and appropriate line wrapping.
   - *Alternative Considered*: Verbatim blocks; rejected because listings offers colored syntax highlighting and exact margin containment.

4. **Comparative Table Design**:
   - *Decision*: Use standard `tabular` and `booktabs` / clean borders within a `table` float to summarize Filter Name, Mathematical Formula / Rank Index, Computational Complexity ($O(k^2 \log k)$ or $O(k^2)$), Effective Noise Suppression Domain, and Edge Preservation Behavior.

## Risks / Trade-offs

- **[Risk] Long listings causing awkward page breaks** → *Mitigation*: Enable `breaklines=true` in `lstdefinestyle`, keep listings modular per section, and adjust vertical spacing with standard float controls.
- **[Risk] Large multi-row figure layouts exceeding single page margins** → *Mitigation*: Adjust `width` attributes in `\includegraphics[width=\textwidth]{...}` or scale factor (e.g. `0.85\textwidth`) with proper float positioning `[H]` or `[htbp]`.
- **[Risk] Missing TeX Live packages on the local environment** → *Mitigation*: Verify `pdflatex` availability and installed style packages before final PDF generation.
