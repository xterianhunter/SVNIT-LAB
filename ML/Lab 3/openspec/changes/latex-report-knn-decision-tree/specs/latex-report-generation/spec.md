## Purpose

Generates a complete, publication-ready LaTeX lab report document with extracted image assets, source code listings, verbatim model execution outputs, and comparative tables based exclusively on `knn_vs_decision_tree_analysis.ipynb`.

## ADDED Requirements

### Requirement: Document Preamble and Department Header
The generated LaTeX file SHALL use the exact specified LaTeX preamble, document class, packages (`newtxtext`, `newtxmath`, `fancyhdr`, `listings`, `graphicx`, `booktabs`), custom listing styles (`code`, `output`), and SVNIT header block with student details for Kishan Sahu (Enrollment No.: P26DS017).

#### Scenario: Rendering header and student information
- **WHEN** the LaTeX document header is compiled
- **THEN** it renders the two-sided running header with "Name: Kishan Sahu" on the left, "Enrollment No.: P26DS017" on the right, and the centered department title block for M.Tech I Semester I Machine Learning Lab Assignment.

### Requirement: Complete Notebook Content Ingestion
The LaTeX document SHALL incorporate all content exclusively from `knn_vs_decision_tree_analysis.ipynb`, including dataset description, preprocessing, Decision Tree theory and formulas, KNN theory and distance formulas, code listings, verbatim execution outputs, and performance evaluations.

#### Scenario: Code listings and output reproduction
- **WHEN** any code or execution output from `knn_vs_decision_tree_analysis.ipynb` is translated
- **THEN** code cells are wrapped in `\begin{lstlisting}[style=code]` and execution outputs are formatted in `\begin{lstlisting}[style=output]` or formatted tables without omitting notebook stages.

### Requirement: Asset Extraction and Figure Integration
The system SHALL extract all embedded plot images from `knn_vs_decision_tree_analysis.ipynb` into a dedicated `figures/` folder and include them in the LaTeX document using `figure` float environments with descriptive captions and labels.

#### Scenario: Visual figure embedding
- **WHEN** the LaTeX report references the notebook plots
- **THEN** it includes graphic floats for the Decision Tree structure diagram, the Decision Tree confusion matrix heatmap, the Decision Tree error vs. depth curve, the KNN confusion matrix heatmap, and the KNN error rate vs. $K$ curve from `figures/`.

### Requirement: Comparative Summary Table and Discussion
The LaTeX document SHALL format the model performance summary using a clean `booktabs` table comparing Accuracy, Misclassification Error, Precision, Recall, and F1-score between Decision Tree and KNN, followed by conceptual synthesis.

#### Scenario: Table formatting and compilation
- **WHEN** the comparison section is compiled
- **THEN** a `booktabs` table with `\toprule`, `\midrule`, and `\bottomrule` displays the side-by-side metrics alongside a comparative trade-off matrix.
