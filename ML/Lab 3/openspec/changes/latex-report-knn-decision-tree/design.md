## Context

The user requested a complete LaTeX report file (`main.tex`) adhering to the SVNIT Surat CSE department formatting header, reflecting exclusively the contents of `knn_vs_decision_tree_analysis.ipynb`. The report must incorporate mathematical formulas, Python source code, verbatim model outputs, image floats for all generated plots, and a formatted comparative table.

## Goals / Non-Goals

**Goals:**
- Extract all embedded PNG plots from `knn_vs_decision_tree_analysis.ipynb` into a local `figures/` directory.
- Generate `main.tex` containing the exact preamble, packages, listing styles, running header, and department title block requested by the user.
- Structure content logically into mathematical theory, listings, outputs, and embedded figures for both Decision Tree and KNN models.
- Provide a clean `booktabs` comparison table contrasting accuracy, error rate, precision, recall, and F1 score.

**Non-Goals:**
- Relying on or referencing other notebooks (`knn-and-decision-tree-iris-data-set.ipynb` or `prices-prediction-knn-and-decision-tree.ipynb`).
- Introducing non-standard packages not in standard TeX Live distributions.

## Decisions

### 1. Document Architecture and File Organization
- **Decision**: Store the LaTeX document at `Lab 3/main.tex` and all extracted images at `Lab 3/figures/*.png`.
- **Rationale**: Keeps the report modular, portable, and immediately compatible with local LaTeX compilers or Overleaf without broken paths.

### 2. Image Asset Extraction
- **Decision**: Programmatically parse the notebook JSON, extract the base64-encoded PNG buffers from code cell outputs, and write them to:
  - `figures/dt_tree_structure.png`: Full tree graph visualization.
  - `figures/dt_confusion_matrix.png`: Decision Tree confusion matrix heatmap.
  - `figures/dt_error_vs_depth.png`: Decision Tree misclassification error vs. max depth curve.
  - `figures/knn_confusion_matrix.png`: KNN confusion matrix heatmap.
  - `figures/knn_error_vs_k.png`: KNN error rate vs. $K$ curve.
- **Rationale**: Ensures exact reproduction of visual artifacts with zero manual cropping or screenshotting.

### 3. Listing and Output Formatting
- **Decision**: Wrap Python code snippets in `\begin{lstlisting}[style=code]` and execution stream outputs in `\begin{lstlisting}[style=output]`.
- **Rationale**: Strictly complies with the custom listing definitions provided in the user's header specification.

## Risks / Trade-offs

- **[Risk]** Long code lines or wide outputs wrapping uncomfortably in PDF rendering.
  - **Mitigation**: Pre-configured `breaklines=true` in `lstdefinestyle{code}` and `lstdefinestyle{output}` handles line wraps cleanly.
- **[Risk]** Over-sized figures exceeding page margins.
  - **Mitigation**: Constrain graphic widths (e.g. `width=0.85\textwidth` for tree structure, `width=0.55\textwidth` for confusion matrices) with centered float environments.
