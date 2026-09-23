## Purpose

Provides an end-to-end clustering pipeline implementing Fuzzy C-Means (FCM) and DBSCAN on the benchmark Iris dataset, including parameter analysis, label alignment with ground truth, comprehensive evaluation metrics, and comparative visualizations without development set splitting.

## ADDED Requirements

### Requirement: Dataset Loading and Standard Preprocessing
The notebook SHALL load the standard benchmark Iris dataset with ground truth labels and perform standard feature scaling (zero mean, unit variance) across all four continuous features without creating train/dev/test splits, retaining true labels for downstream evaluation.

#### Scenario: Preprocessing pipeline execution
- **WHEN** the dataset loading and preprocessing cells are executed
- **THEN** the feature matrix is normalized using standard scaling and target labels are preserved.

### Requirement: Fuzzy C-Means (FCM) Algorithm Implementation
The notebook SHALL implement the Fuzzy C-Means algorithm allowing soft membership degrees between samples and cluster centroids using fuzziness parameter $m$, iterative centroid updates, convergence checks, and crisp cluster assignment via maximum membership.

#### Scenario: Executing Fuzzy C-Means clustering
- **WHEN** Fuzzy C-Means is fitted on the standardized feature matrix with target cluster count $c=3$ and fuzziness $m=2.0$
- **THEN** soft membership values summing to 1.0 per sample, converged cluster centroids, and crisp cluster predictions are produced.

### Requirement: DBSCAN Density-Based Clustering Implementation
The notebook SHALL implement DBSCAN clustering to identify dense core regions, border samples, and noise points without requiring a predetermined number of clusters.

#### Scenario: Executing DBSCAN clustering
- **WHEN** DBSCAN is fitted on the standardized feature matrix with calibrated $\epsilon$ and `min_samples`
- **THEN** cluster labels are assigned to core and border samples while noise points are designated with label -1.

### Requirement: Parameter Tuning and Diagnostic Analysis
The notebook SHALL provide parameter diagnostic analyses: evaluating FCM across varying cluster counts and fuzziness values, and computing the k-nearest-neighbors distance elbow plot to justify the choice of $\epsilon$ for DBSCAN.

#### Scenario: Running diagnostic parameter analysis
- **WHEN** the parameter analysis cells are executed
- **THEN** the k-distance elbow curve for DBSCAN and objective/silhouette curves for FCM are rendered inline.

### Requirement: Hungarian Cluster Label Alignment
The notebook SHALL map unsupervised cluster assignments to ground truth class labels using the Hungarian algorithm (optimal linear sum assignment) to ensure fair calculation of classification error metrics, appropriately handling unclustered noise points in DBSCAN.

#### Scenario: Aligning cluster indices with ground truth classes
- **WHEN** the Hungarian alignment function is invoked on FCM and DBSCAN predictions
- **THEN** cluster indices are mapped to the true target classes that maximize matching agreement.

### Requirement: Performance and Error Metrics Computation
The notebook SHALL compute both unsupervised validation metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index) and supervised alignment error metrics (Mean Absolute Error, Mean Squared Error, Root Mean Squared Error, Adjusted Rand Index, Normalized Mutual Information) for both algorithms.

#### Scenario: Computing clustering evaluation metrics
- **WHEN** the evaluation metrics cell is executed
- **THEN** a structured comparison table containing both unsupervised quality scores and supervised error metrics is displayed for FCM and DBSCAN.

### Requirement: Comprehensive Visualizations and Confusion Matrices
The notebook SHALL generate informative visual plots: exploratory feature distributions and correlations, 2D feature-space and PCA cluster projections, FCM membership distribution heatmaps, DBSCAN core vs. border vs. noise sample scatter plots, and confusion matrix heatmaps.

#### Scenario: Generating visualization plots
- **WHEN** visualization cells are executed
- **THEN** clean matplotlib/seaborn figures illustrating clustering structure, membership probabilities, and confusion matrices are generated inline.
