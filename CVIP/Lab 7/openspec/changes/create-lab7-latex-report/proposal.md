## Why

The user requires a clean, professional, and well-structured LaTeX lab report for CVIP Lab Assignment 7 (Radiometry and Image Formation) utilizing the institutional header and styling specified for SVNIT Surat (Name: Kishan Sahu, Enrollment No.: P26DS017). The report must cleanly document all solved problems (Part A: Q1, Q2, Q3, Q6, Q7 and Part B), incorporating code listings, outputs, generated visualization figures, and concise analytical observations.

## What Changes

- Create a structured LaTeX document `CVIP_Lab7_Report.tex` incorporating the provided document preamble (geometry, newtxtext/newtxmath, fancyhdr, listings styles `code` and `output`, 12pt font).
- Update the assignment metadata to:
  - Department: Computer Science and Engineering Department, SVNIT, Surat
  - Degree: M.Tech. I -- Semester I
  - Course: Computer Vision and Image Processing (CSCS111/CSDS119)
  - Assignment: Lab Assignment 7 (Radiometry and Image Formation)
  - Header: Kishan Sahu (P26DS017)
- Export generated figures from the solution notebook/script into a dedicated `figures/` directory.
- Incorporate formatted code listings (`lstlisting` with style `code`), terminal outputs (`lstlisting` with style `output`), embedded figures (`figure` environment with `\includegraphics`), and crisp observations for each question.
- Keep the report layout compact, readable, and elegant without unnecessary filler.

## Capabilities

### New Capabilities
- `lab7-latex-report`: Complete LaTeX report generation framework for CVIP Lab 7, including figure generation and compilation-ready LaTeX source.

### Modified Capabilities
<!-- None -->

## Impact

- Adds `CVIP_Lab7_Report.tex` in the workspace root.
- Generates high-resolution plot images in `figures/`.
- No disruption to existing solution code in `CVIP_Lab7.ipynb`.
