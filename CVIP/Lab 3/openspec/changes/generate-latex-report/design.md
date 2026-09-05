## Context

The lab notebook `Lab3_Understanding_Digital_Images.ipynb` has executed all 14 parts successfully, producing verified outputs and plots. To deliver an academic submission, a LaTeX document `Lab3_Understanding_Digital_Images.tex` will be generated incorporating the user's exact preamble, headers, package imports, and listings styles, accompanied by exported high-resolution figure assets in a `figures/` folder.

## Goals / Non-Goals

**Goals:**
- Provide a complete, self-contained LaTeX document `Lab3_Understanding_Digital_Images.tex`.
- Use the exact user-specified LaTeX template, including `\documentclass[12pt]{article}`, 1-inch margins, `newtxtext,newtxmath`, `fancyhdr` with "Name: Kishan Sahu" and "Enrollment No.: P26DS017", and `\lstdefinestyle{code}` / `\lstdefinestyle{output}`.
- Export all plot figures generated during the lab into `figures/` for seamless inclusion via `\includegraphics`.
- Present source code in `\begin{lstlisting}[style=code]` and console outputs in `\begin{lstlisting}[style=output]`.
- Provide complete, thoughtful answers to all conceptual reflection questions ("Think Before Moving Ahead", "Investigation", and "Critical Thinking").

**Non-Goals:**
- Not modifying the user-mandated template styles or header layout.
- Not requiring external proprietary LaTeX packages outside standard TeX Live / Overleaf environments.

## Decisions

### 1. Asset Management & Figure Export
- **Decision**: Save PNG figures directly into `figures/` using descriptive filenames (`fig_part2_original.png`, `fig_part4_grayscale.png`, `fig_part6_modified.png`, `fig_part7_negative.png`, `fig_part8_brightened.png`, `fig_part9_thresholds.png`, `fig_part10_histogram.png`, `fig_part11_crop_resize.png`, `fig_part12_noisy.png`, `fig_part13_filtering.png`).
- **Rationale**: Keeps the workspace clean and ensures the LaTeX document compiles out-of-the-box in local environments or when uploaded to Overleaf.

### 2. Sectional Organization
- Each lab part (Parts 1 to 14) will follow a structured layout:
  1. `\subsection*{Part N — Title}`
  2. Theoretical description and formulas.
  3. Source code in `\begin{lstlisting}[style=code]`.
  4. Execution output in `\begin{lstlisting}[style=output]`.
  5. Visual figure embedded using `\begin{figure}[H]` with `\centering`, `\includegraphics`, and informative caption.
  6. Academic responses to reflection and discussion questions.

### 3. Question Answering Integration
- Answers to questions like "Why can't uint8 store 300?", "Why did the 3rd dimension disappear?", "Why is np.clip() necessary?", and Part 13's 4 critical thinking questions will be explicitly articulated in formatted text blocks.

## Risks / Trade-offs

- **[Risk] Figure float overflow or page stretching**  
  → *Mitigation*: Use `[H]` from the `float` package and relative widths (`0.65\textwidth` to `0.95\textwidth`) to keep elements tightly bound to their respective sections.
- **[Risk] Special characters in terminal output**  
  → *Mitigation*: Enclose all verbatim console outputs in `\begin{lstlisting}[style=output]` which handles characters without TeX escaping errors.
