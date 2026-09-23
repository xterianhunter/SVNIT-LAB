# Change Proposal: clustering-latex-report

## Why

Lab Assignment 4 focuses on unsupervised learning with K-Means and Hierarchical Clustering on the Iris dataset. While the implementation and experimental runs in `clustering_lab4.ipynb` are complete, there is no formal academic laboratory report document. A comprehensive LaTeX report using the department's standard academic template (with SVNIT header, 12pt Times font, structured listings for Python code and console outputs, and high-resolution figures) is required for submission.

## What Changes

- Extract and persist all generated evaluation and EDA visualization plots from `clustering_lab4.ipynb` into a dedicated `figures/` directory.
- Create a complete academic LaTeX document `main.tex` formatted to SVNIT Department of Computer Science & Engineering standards.
- Incorporate formatted code snippets (`lstlisting` with `code` style) directly mapped to notebook implementation sections.
- Incorporate verbatim terminal/execution metrics and results (`lstlisting` with `output` style), including inertia, silhouette scores, Davies-Bouldin indices, and contingency tables.
- Integrate theoretical formulations (K-Means objective function, Ward/Complete/Average linkage formulations, distance metrics, evaluation score math) and comparative analytical discussions.

## Capabilities

### New Capabilities
- `clustering-report`: Generation of the comprehensive academic LaTeX report (`main.tex`) and associated figures for Lab Assignment 4 (K-Means and Hierarchical Clustering), containing theoretical formulations, code listings, execution outputs, and rendered plots.

### Modified Capabilities
*(None)*

## Impact

- **Files Created**:
  - `main.tex` in the root of `Lab 4/`
  - High-resolution figure image assets under `Lab 4/figures/` (e.g., EDA pairplots/heatmaps, Elbow curve, Silhouette analysis, K-Means PCA clusters, Hierarchical clustering dendrograms, Agglomerative cluster comparisons)
- **Dependencies**: Uses existing Python environment (`matplotlib`, `seaborn`, `scipy`, `scikit-learn`) to export figures if needed.
- **System Compatibility**: Strict compliance with standard LaTeX packages (`geometry`, `fancyhdr`, `listings`, `graphicx`, `float`, `amsmath`, `newtxtext`, `newtxmath`, `booktabs`, `xcolor`).
