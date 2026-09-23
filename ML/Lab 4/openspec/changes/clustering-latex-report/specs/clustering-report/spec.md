## Purpose

Provides specification for the compilation and structure of the academic laboratory report for Machine Learning Lab Assignment 4 (Clustering using K-Means and Hierarchical Clustering) adhering to departmental publication formatting standards.

## ADDED Requirements

### Requirement: Document Structure and Departmental Academic Header
The report document SHALL adhere strictly to SVNIT Department of Computer Science and Engineering formatting requirements, including author metadata, course details, 12pt document styling with Times font, and standard running headers.

#### Scenario: Document layout and header verification
- **WHEN** the LaTeX document `main.tex` is inspected or compiled
- **THEN** it contains the specified header configuration with student Name ("Kishan Sahu"), Enrollment No. ("P26DS017"), Course Title ("Machine Learning (CSDS105)"), and Assignment Title ("Lab Assignment 4: Unsupervised Learning -- K-Means and Hierarchical Clustering").

### Requirement: Verbatim Code Segment Inclusion
The report SHALL include complete, runnable Python code listings corresponding to each stage of the unsupervised clustering pipeline using dedicated syntax-highlighted lstlisting blocks.

#### Scenario: Code block presentation
- **WHEN** inspecting the code sections of `main.tex`
- **THEN** code snippets for dataset loading, EDA, K-Means clustering, Elbow/Silhouette sweeps, Dendrogram generation, and Agglomerative clustering are formatted with `style=code`.

### Requirement: Verbatim Numerical and Tabular Output Inclusion
The report SHALL present execution metrics, evaluation statistics, cluster contingency tables, and comparative benchmarks directly from the experiment runs.

#### Scenario: Execution results presentation
- **WHEN** reviewing evaluation and clustering output sections
- **THEN** cluster centroids, inertia values, Silhouette scores, Davies-Bouldin indices, and cluster-to-ground-truth distribution tables appear inside `style=output` lstlisting blocks or formal LaTeX tables.

### Requirement: High-Resolution Graphic Visualization Integration
All generated exploratory and diagnostic plots from the clustering study SHALL be exported to the `figures/` directory and referenced via standard LaTeX figure environments with descriptive captions and labels.

#### Scenario: Visual figure linking
- **WHEN** reading the analysis and result sections
- **THEN** figures including EDA correlation heatmap, pairplot, Elbow/Inertia plot, Silhouette score curve, 2D PCA cluster scatter plots, Dendrograms (Ward, Complete, Average), and Agglomerative cluster comparisons are embedded using `\includegraphics`.

### Requirement: Theoretical and Algorithmic Rigor
The document SHALL articulate the underlying mathematical formulations for the K-Means objective function, linkage criteria equations (Ward, Single, Complete, Average), metric definitions (Euclidean distance, Silhouette score, Davies-Bouldin index), and analytical synthesis of results.

#### Scenario: Mathematical completeness
- **WHEN** examining the theory and methodology sections
- **THEN** formal equations and objective minimization formulations are typeset using AMS math notation.
