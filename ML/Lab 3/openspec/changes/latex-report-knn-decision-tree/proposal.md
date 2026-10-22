## Why

In academic machine learning coursework at SVNIT Surat, lab assignments must be accompanied by a rigorous, publication-grade LaTeX report document formatted according to department guidelines. Following the execution and benchmark of Decision Tree and K-Nearest Neighbors in `knn_vs_decision_tree_analysis.ipynb`, a corresponding LaTeX report file (`main.tex` or `lab3_report.tex`) is required that integrates the department header, mathematical theory, algorithms, syntax-highlighted Python listings, verbatim model outputs, embedded figures (decision tree plot, confusion matrices, error curves), and comparative analysis tables.

## What Changes

- Extract all embedded graphical figures (Decision Tree graph, DT confusion matrix, DT error vs. max_depth curve, KNN confusion matrix, KNN error rate vs. $K$ curve) from `knn_vs_decision_tree_analysis.ipynb` into a dedicated `figures/` directory.
- Create a comprehensive LaTeX report document using the exact department preamble, font configurations (`newtxtext,newtxmath`), listing styles (`code`, `output`), and header details:
  - Header: Kishan Sahu, Enrollment No.: P26DS017.
  - Department Header: Computer Science and Engineering Department, SVNIT, Surat; M.Tech. I -- Semester I; Machine Learning (CSDS105); Lab Assignment 3: Classification using Decision Tree and K-Nearest Neighbors.
  - Formulations for Decision Tree node splitting (Entropy, Information Gain, Gini Impurity) with exact mathematical equations.
  - Formulations for K-Nearest Neighbors (Euclidean, Manhattan, Minkowski metrics, majority voting, feature scaling justification).
  - Code listings for each notebook block using `\lstdefinestyle{code}`.
  - Verbatim text outputs for execution blocks using `\lstdefinestyle{output}`.
  - Included graphic floats for all 5 generated plots with descriptive captions and labels.
  - Formal comparison table with `booktabs` syntax comparing metrics across models.

## Capabilities

### New Capabilities
- `latex-report-generation`: Extraction of notebook assets and generation of a complete LaTeX report matching SVNIT formatting guidelines and encapsulating all codes, mathematical derivations, outputs, images, and comparative analysis from `knn_vs_decision_tree_analysis.ipynb`.

### Modified Capabilities

## Impact

- Creates `main.tex` in the `Lab 3` workspace.
- Creates `figures/` directory containing the extracted high-resolution PNG plots from the executed notebook.
- No impact on existing `.ipynb` files.
