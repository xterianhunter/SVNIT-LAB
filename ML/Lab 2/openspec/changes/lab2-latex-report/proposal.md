## Why

The completed Jupyter Notebook `assignment_2_naive_bayes.ipynb` contains comprehensive implementations, visualizations, empirical metrics, and diagnostic analyses for sentiment classification using Naive Bayes on the IMDb dataset. To deliver a complete academic submission adhering to the department's standard formatting, a unified LaTeX report (`lab2.tex`) must be generated matching the typography, styling, header metadata, listings configuration, algorithm blocks, and figure presentation established in `main.tex`.

## What Changes

- Create `lab2.tex` replicating the visual and typographic style of `main.tex` (A4 paper, 12pt Times font via `newtxtext`/`newtxmath`, fancy header with student metadata, code and output `listings` styles, structured problem headings).
- Extract and export all notebook charts and visualizations from `assignment_2_naive_bayes.ipynb` into dedicated image files (e.g., in a `figures/` directory):
  - Document length distribution plot (Task 1)
  - Confusion matrices for Multinomial and Bernoulli Naive Bayes (Task 4)
  - Model comparison metric bar chart (Task 5)
  - Alpha smoothing hyperparameter curve (Task 6)
- Include all cell codes formatted in `\begin{lstlisting}[style=code]`.
- Include all text outputs, classification reports, and tabular metrics formatted in `\begin{lstlisting}[style=output]` and LaTeX tables.
- Structure all 7 tasks and final report sections with detailed problem statements, methodologies, algorithms/pseudocode where applicable, analysis, and discussions.

## Capabilities

### New Capabilities
- `latex-report`: Complete academic LaTeX document (`lab2.tex`) compiling all code, outputs, figures, tables, and analytical explanations from `assignment_2_naive_bayes.ipynb` following the design styling of `main.tex`.

### Modified Capabilities
*(None)*

## Impact

- Adds `lab2.tex` in the root workspace.
- Adds exported figure image files (e.g., `figures/task1_doc_length.png`, `figures/task4_confusion_matrices.png`, `figures/task5_model_comparison.png`, `figures/task6_smoothing_curve.png`).
- Can be compiled to PDF using `pdflatex` or `latexmk`.
