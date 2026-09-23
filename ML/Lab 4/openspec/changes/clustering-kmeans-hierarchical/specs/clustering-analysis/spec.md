## Purpose

Provides an end-to-end clustering pipeline implementing K-Means and Hierarchical Clustering, minimal preprocessing, unsupervised evaluation metrics, error metrics (MAE, MSE, RMSE), and visualizations including confusion matrices.

## ADDED Requirements

### Requirement: Dataset Loading and Minimal Preprocessing
The notebook SHALL load a standard benchmark dataset with ground truth labels and perform only necessary preprocessing, specifically standardizing feature values for distance-based clustering algorithms while preserving true labels for downstream evaluation.

#### Scenario: Preprocessing pipeline execution
- **WHEN** the dataset loading and preprocessing cell is executed
- **THEN** features are normalized using standard scaling and target labels are retained without unnecessary modifications.

### Requirement: K-Means Clustering Implementation
The notebook SHALL implement K-Means clustering to partition the dataset into the appropriate number of clusters and record predicted cluster assignments.

#### Scenario: Running K-Means clustering
- **WHEN** K-Means model is fitted on the preprocessed feature matrix
- **THEN** cluster labels are assigned to each sample and centroids are computed.

### Requirement: Hierarchical Clustering and Dendrogram
The notebook SHALL implement Agglomerative Hierarchical Clustering and render a dendrogram visualizing sample merge distances across hierarchical levels.

#### Scenario: Running Hierarchical clustering and plotting dendrogram
- **WHEN** hierarchical clustering and linkage analysis are executed
- **THEN** cluster labels are assigned to each sample and a clear dendrogram plot is generated.

### Requirement: Cluster Label Alignment with Ground Truth
The notebook SHALL map unsupervised cluster labels to true ground-truth class labels using optimal assignment (Hungarian algorithm / majority voting) to enable fair classification error calculations.

#### Scenario: Mapping cluster labels to true labels
- **WHEN** cluster assignments are compared against ground truth classes
- **THEN** each cluster index is uniquely mapped to the corresponding true class label maximizing accuracy.

### Requirement: Clustering and Error Metrics Computation
The notebook SHALL compute both unsupervised performance metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index) and error metrics (Mean Absolute Error, Mean Squared Error, Root Mean Squared Error) for both clustering algorithms.

#### Scenario: Evaluation metrics display
- **WHEN** the metrics computation cells are run
- **THEN** Silhouette, Davies-Bouldin, Calinski-Harabasz, MAE, MSE, and RMSE values are displayed for both K-Means and Hierarchical clustering.

### Requirement: Graphical Visualizations and Confusion Matrices
The notebook SHALL generate clear visualization plots including cluster scatter plots, metric and error comparison bar charts, and confusion matrix heatmaps comparing mapped cluster predictions to ground truth labels.

#### Scenario: Plot generation
- **WHEN** visualization cells are executed
- **THEN** scatter plots of clusters, comparison charts of metrics/errors, and confusion matrix heatmaps are rendered inline.
