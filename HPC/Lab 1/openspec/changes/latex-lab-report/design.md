## Context

See proposal.md. A complete, self-contained LaTeX document (`lab1_report.tex`) must be created following the exact user-specified LaTeX template, preamble, student header, listing styles, and department heading, presenting all 4 dynamic memory allocation programs from Lab 1.

## Goals / Non-Goals

**Goals:**
- Generate `lab1_report.tex` with the exact preamble and listings setup specified by the user.
- Include all 4 Lab 1 programs (`min_max.c`, `matrix_mult.c`, `dot_product.c`, `merge_sort.c`) using `\begin{lstlisting}[style=code]`.
- Include verbatim verified console outputs using `\begin{lstlisting}[style=output]`.
- Provide concise algorithmic analysis for each program (time complexity, auxiliary space, dynamic memory patterns).

**Non-Goals:**
- Modifying the underlying C source code or altering program behavior.
- Generating binary PDF output directly if local TeX engine is not installed (deliverable is a clean, compilable `.tex` file).

## Decisions

- **File Naming**: Name the output file `lab1_report.tex` in the root of the lab workspace.
- **Section Layout**: Consistent 3-part structure for each of the 4 problems:
  1. Source Code (`\begin{lstlisting}[style=code]`)
  2. Execution Output (`\begin{lstlisting}[style=output]`)
  3. Short Analysis (Time Complexity, Space Complexity, Key Observations)
- **Title Block**: Set the title block to reflect Lab Assignment 1 while preserving the exact layout and format provided by the user.

## Risks / Trade-offs

- [Character escaping in listings / LaTeX] → Ensure all listings use verbatim lstlisting environments to avoid compilation issues with special C characters (`#`, `%`, `&`, `_`).
