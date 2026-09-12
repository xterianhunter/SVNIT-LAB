## Purpose

Provides a complete, reproducible Jupyter Notebook implementation for Lab Assignment 1 restored directly from the documented code listings and analysis in the lab reference document.

## ADDED Requirements

### Requirement: Valid Jupyter Notebook Document Structure
The system SHALL restore `Lab 1/sentiment_analysis.ipynb` as a syntactically valid Jupyter Notebook complying with the nbformat version 4 specification.

#### Scenario: Notebook file validation
- **WHEN** the notebook file `Lab 1/sentiment_analysis.ipynb` is parsed as JSON
- **THEN** it contains standard root keys `cells`, `metadata`, `nbformat: 4`, and `nbformat_minor: 2`, and parses without JSON syntax errors.

### Requirement: Part 1 - 20 Newsgroups Dataset Analysis Restoration
The notebook SHALL contain all 10 code listings and markdown documentation cells for Part 1 (20 Newsgroups dataset) exactly as presented in `machine_learning_lab.pdf`.

#### Scenario: Part 1 code and text cells present
- **WHEN** the notebook is inspected for Part 1 contents
- **THEN** it contains code cells for library imports, dataset loading function (`load_20newsgroups`), dataset overview and first 5 records, document distribution across categories, sample document inspection, feature data types summary, histogram and count plot generation, statistical measures computation, box plot distribution analysis, joint plots and correlation heatmaps, and a markdown summary of key insights.

### Requirement: Part 2 - California Housing Dataset Analysis Restoration
The notebook SHALL contain all 10 code listings and markdown documentation cells for Part 2 (California Housing dataset) exactly as presented in `machine_learning_lab.pdf`.

#### Scenario: Part 2 code and text cells present
- **WHEN** the notebook is inspected for Part 2 contents
- **THEN** it contains code cells for library imports, loading California Housing data (`fetch_california_housing`), descriptive statistical measures computation, correlation heatmap and strong pair analysis, visualization suite (histograms, box plots, scatter plots, bar charts), missing value injection and detection, mean vs. KNN imputation, IQR vs. Z-score outlier detection, IQR-based outlier removal, normalization scaling (Min-Max, Standard, Robust), and a markdown summary of key insights.

### Requirement: Code Sanitization and Clean Syntax
The system SHALL ensure that all restored Python code cells are completely free of PDF formatting artifacts.

#### Scenario: Execution-ready Python syntax
- **WHEN** Python code cells in the notebook are parsed by the Python AST
- **THEN** no syntax errors occur from line numbers, page breaks, header/footer metadata, or Unicode typographical quotes (`’`, `‘`, `”`, `“`).
