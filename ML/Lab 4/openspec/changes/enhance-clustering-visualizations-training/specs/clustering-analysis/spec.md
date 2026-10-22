## Purpose

Provides comprehensive dataset exploratory analysis, clustering training diagnostic curves (Elbow method and Silhouette sweep), cluster visualization with centroids, evaluation metrics, and confusion matrix analysis.

## ADDED Requirements

### Requirement: Dataset Exploration and Visualizations
The notebook SHALL produce Exploratory Data Analysis (EDA) visualizations of the dataset before model training, including feature distributions, a correlation heatmap, and a scatter plot of primary features colored by true class labels.

#### Scenario: Rendering exploratory data visualizations
- **WHEN** the EDA section of the notebook is executed
- **THEN** feature distribution histograms/KDEs, correlation matrix heatmap, and bivariate feature scatter plots are displayed.

### Requirement: Clustering Training Optimization Curves
The notebook SHALL execute a hyperparameter sweep over cluster counts $k \in [1, 10]$ for K-Means and plot the Elbow Method curve (inertia vs. $k$) and the Silhouette score curve to identify and justify the optimal number of clusters.

#### Scenario: Plotting training optimization curves
- **WHEN** the training diagnostic cells are executed
- **THEN** an Elbow method plot and a Silhouette score sweep plot are rendered with clear indicators for optimal $k$.

### Requirement: Hierarchical Clustering Dendrogram Analysis
The notebook SHALL generate a hierarchical clustering linkage tree and render a dendrogram with an annotated cluster cutoff threshold distance.

#### Scenario: Visualizing hierarchical tree
- **WHEN** the hierarchical clustering linkage is calculated
- **THEN** an annotated dendrogram is displayed showing cluster merge distances and threshold.

### Requirement: Enhanced Cluster Visualizations with Centroids
The notebook SHALL display cluster assignments both in the original feature space and in 2D PCA projected space, explicitly marking and distinguishing cluster centroids for K-Means alongside Ground Truth and Hierarchical cluster assignments.

#### Scenario: Visualizing clusters and centroids
- **WHEN** the cluster visualization cells are run
- **THEN** 2D scatter plots show distinct cluster colors with prominently marked centroid locations.

### Requirement: Performance Metrics and Error Computation
The notebook SHALL compute unsupervised clustering metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz) and error metrics (MAE, MSE, RMSE) between ground truth and Hungarian-aligned cluster predictions, displaying them in a comparative table and bar plots.

#### Scenario: Evaluating models
- **WHEN** evaluation cells are executed
- **THEN** comparative tables and bar graphs of all performance scores and regression errors are displayed.

### Requirement: Confusion Matrix Heatmaps
The notebook SHALL plot confusion matrix heatmaps comparing optimally aligned cluster predictions to true class labels for both K-Means and Hierarchical clustering.

#### Scenario: Displaying confusion matrices
- **WHEN** the confusion matrix cell is executed
- **THEN** annotated heatmaps for both models are rendered side-by-side with true class labels.
