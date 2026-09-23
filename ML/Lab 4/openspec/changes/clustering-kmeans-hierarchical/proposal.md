## Why

Machine learning laboratory exercises require a clear, concise, and complete implementation of unsupervised clustering algorithms. This change provides a clean, well-structured Jupyter Notebook (`clustering_lab4.ipynb`) demonstrating both K-Means and Hierarchical Clustering on a benchmark dataset, including only necessary preprocessing, clustering evaluation metrics, error metrics (MAE, RMSE, MSE), and visualization plots including confusion matrices.

## What Changes

- Create a comprehensive yet minimal Jupyter Notebook implementing:
  - Dataset loading and minimal preprocessing (feature scaling and ground-truth label preservation for evaluation).
  - K-Means clustering implementation and cluster assignment.
  - Hierarchical (Agglomerative) clustering implementation and dendrogram visualization.
  - Optimal cluster alignment with true labels using majority vote / linear sum assignment.
  - Computation of clustering performance metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index).
  - Computation of error metrics (MAE, MSE, RMSE) between aligned cluster labels and true labels.
  - Visualization plots:
    - Cluster scatter plots (with PCA 2D projection if dimensionality > 2).
    - Hierarchical clustering dendrogram.
    - Evaluation metrics and error comparison charts.
    - Confusion matrices for both K-Means and Hierarchical clustering.

## Capabilities

### New Capabilities
- `clustering-analysis`: Provides K-Means and Hierarchical clustering workflows, cluster alignment, error computation (MAE, MSE, RMSE), evaluation metrics, and visualization in an interactive Jupyter notebook.

### Modified Capabilities
<!-- None -->

## Impact

- Adds a new notebook `clustering_lab4.ipynb` to the workspace.
- Requires standard scientific Python libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, and `scikit-learn`.
