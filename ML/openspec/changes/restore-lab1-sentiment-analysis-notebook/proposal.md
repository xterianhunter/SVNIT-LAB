## Why

The Jupyter notebook `Lab 1/sentiment_analysis.ipynb` accidentally had all of its cells deleted and is currently empty (0 bytes). However, the complete implementation code, markdown sections, outputs, and visualizations for Lab Assignment 1 are documented in `Lab 1/machine_learning_lab.pdf`. Restoring the exact code and structure into the Jupyter notebook is necessary so the lab can be executed, verified, and submitted without loss of work.

## What Changes

- Reconstruct `Lab 1/sentiment_analysis.ipynb` as a valid Jupyter Notebook (IPython Notebook format v4) containing all 20 code listings and accompanying markdown headers/sections from `Lab 1/machine_learning_lab.pdf`.
- Restore **Part 1: Foundational Exercises on 20 Newsgroups Dataset**:
  - Listing 1: Library imports and configuration.
  - Listing 2: Dataset loading function (`load_20newsgroups`) and execution.
  - Listing 3: Dataset overview and first 5 records inspection.
  - Listing 4: Document distribution calculation across categories.
  - Listing 5: Sample document printing.
  - Listing 6: Feature data types and nature summary.
  - Listing 7: Plotting histograms and count plots.
  - Listing 8: Descriptive statistical measures computation.
  - Listing 9: Visual and statistical analysis via box plots.
  - Listing 10: Joint plots and correlation heatmaps.
  - Section 11: Key insights and analytical summary markdown notes.
- Restore **Part 2: California Housing Dataset Analysis and Data Processing**:
  - Listing 11: Library imports and environment setup.
  - Listing 12: Loading California Housing dataset (`fetch_california_housing`).
  - Listing 13: Comprehensive statistical measures computation.
  - Listing 14: Correlation matrix and feature pair relationships.
  - Listing 15: Visualization suite (histograms, box plots, scatter plots, bar charts).
  - Listing 16: Missing value injection and identification.
  - Listing 17: Missing value imputation techniques (Mean vs. KNN).
  - Listing 18: Outlier detection methods comparison (IQR vs. Z-score).
  - Listing 19: Outlier removal execution (IQR-based trimming).
  - Listing 20: Feature normalization techniques (Min-Max, Standard, Robust scaling).
  - Section 11: Key insights and analytical summary markdown notes.
- Clean and sanitize PDF-extracted code: strip interleaved line numbers, remove page header/footer artifacts, and normalize Unicode typographical quotes (`’`, `‘`, `”`, `“`) and dashes to valid Python syntax.

## Capabilities

### New Capabilities
- `lab1-notebook-restoration`: Full restoration of the Lab 1 Jupyter notebook (`Lab 1/sentiment_analysis.ipynb`) comprising all foundational exercises on the 20 Newsgroups dataset and California Housing dataset according to `Lab 1/machine_learning_lab.pdf`.

### Modified Capabilities
<!-- No existing capability requirements are being modified. -->

## Impact

- **Affected files**: `Lab 1/sentiment_analysis.ipynb`.
- **References**: `Lab 1/machine_learning_lab.pdf`.
- **Runtime/Dependencies**: Python environment with `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, and `scikit-learn`.
- **Side effects**: No breaking changes to existing repository components; restores corrupted/emptied notebook file.
