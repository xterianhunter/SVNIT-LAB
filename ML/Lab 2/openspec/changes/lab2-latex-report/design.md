## Context

See proposal.md - Why.
The repository contains:
1. `main.tex`: A reference LaTeX document demonstrating the required academic formatting style (12pt Times font via `newtxtext`/`newtxmath`, `fancyhdr` running headers with student info, customized `listings` environments `style=code` and `style=output`, and structured problem breakdown).
2. `assignment_2_naive_bayes.ipynb`: A fully executed Jupyter notebook implementing 7 sentiment classification tasks and an exhaustive final report on the IMDb dataset, including 4 rich visualization plots embedded as PNG data.

## Goals / Non-Goals

**Goals:**
- Extract all 4 embedded PNG figures from the notebook into a local `figures/` directory (`task1_doc_length.png`, `task4_confusion_matrices.png`, `task5_model_comparison.png`, `task6_smoothing_curve.png`).
- Author a comprehensive, publication-ready `lab2.tex` replicating the visual design, preamble, package inclusions, and header metadata (`Kishan Sahu`, `P26DS017`, `SVNIT Surat`) from `main.tex`.
- Represent all notebook code cells in `\begin{lstlisting}[style=code]`, verbatim console outputs in `\begin{lstlisting}[style=output]`, tables in LaTeX `tabular` environments, and plots in LaTeX `figure[H]` floats.
- Include structured algorithms/pseudocode where appropriate (e.g., preprocessing pipeline, Naive Bayes training/prediction algorithms).
- Verify clean, error-free compilation of `lab2.tex` into `lab2.pdf` using `pdflatex`.

**Non-Goals:**
- Modifying the existing `main.tex` template or changing the underlying Python code in `assignment_2_naive_bayes.ipynb`.
- Introducing exotic or non-standard LaTeX packages requiring manual CTAN installation.

## Decisions

### Decision 1: Direct extraction of notebook figure assets
- **Choice**: Extract the base64-encoded PNG figures directly from `assignment_2_naive_bayes.ipynb` JSON cells into `figures/`.
- **Rationale**: Guarantees identical visual fidelity with the experimental execution in the notebook without needing to re-execute lengthy dataset loads or hyperparameter sweeps.
- **Alternatives Considered**: Re-running Python scripts to re-generate plots (unnecessary overhead and risk of subtle rendering discrepancies).

### Decision 2: Architectural layout mirroring `main.tex`
- **Choice**: Replicate the exact preamble of `main.tex`:
  - Font: `\AtBeginDocument{\fontsize{12pt}{14pt}\selectfont}` with `newtxtext` and `newtxmath`.
  - Margins: `\usepackage[a4paper,margin=1in]{geometry}`.
  - Header: `\fancyhead[L]{Name: Kishan Sahu{\hspace{4cm}}}` and `\fancyhead[R]{Enrollment No.: P26DS017{\hspace{3.5cm}}}`.
  - Listings: `\lstdefinestyle{code}` (with line numbers, syntax colors) and `\lstdefinestyle{output}` (shaded box, no line numbers).
  - Title: SVNIT CSE Dept header for Lab Assignment 2 (Sentiment Classification using Naive Bayes).
- **Rationale**: Satisfies the user's strict requirement for identical visual and structural presentation.

### Decision 3: Structured Task Breakdown
- **Choice**: Organize `lab2.tex` into clear sections matching the 7 notebook tasks:
  - Task 1: Dataset Exploration & Statistics (with document length distribution figure)
  - Task 2: Text Preprocessing Pipeline (with pipeline flowchart/pseudocode and before/after stats)
  - Task 3: Feature Extraction (Count vs Bernoulli representations and vocab analysis)
  - Task 4: Multinomial and Bernoulli Naive Bayes Modeling (with classification reports and confusion matrix figures)
  - Task 5: Model Comparison & Metric Evaluation (with metrics table and comparison bar chart)
  - Task 6: Effect of Laplace/Lidstone Smoothing (with hyperparameter sweep curve and underfitting/overfitting discussion)
  - Task 7: Qualitative & Quantitative Error Diagnostics (with comprehensive misclassified sample table and failure mode analysis)
  - Final Synthesis & Conclusions
- **Rationale**: Ensures thorough academic coverage of all experimental results.

## Risks / Trade-offs

- **[Risk] LaTeX special characters in output listings or text** → *Mitigation*: Ensure all raw terminal logs and sample review texts are enclosed in `lstlisting` environments with proper escaping, and sanitize any math/special characters in standard paragraphs.
- **[Risk] Float placement and image overflow** → *Mitigation*: Use `[H]` float specifiers with `\usepackage{float}` and scale graphics with `\centering\includegraphics[width=0.88\textwidth]{...}`.
- **[Risk] Long code or output lines breaking across pages** → *Mitigation*: Configure `breaklines=true` and `breakatwhitespace=false` in `lstdefinestyle` as defined in `main.tex`.
