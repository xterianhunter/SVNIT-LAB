## Why

Following the exploration of K-Means and Hierarchical Clustering in Lab 4, extending the experimental clustering toolkit with soft/fuzzy partitioning (Fuzzy C-Means) and density-based clustering (DBSCAN) provides deeper comparative insights into handling overlapping cluster boundaries and discovering arbitrary cluster shapes with noise identification. The user requested a new, clean Jupyter Notebook implementing both Fuzzy C-Means (FCM) and DBSCAN on the benchmark Iris dataset, keeping the workflow simple without development set splitting.

## What Changes

- Create a new Jupyter notebook `clustering_lab4_fcm_dbscan.ipynb` providing a streamlined, self-contained end-to-end clustering pipeline for Fuzzy C-Means (FCM) and DBSCAN.
- Implement Fuzzy C-Means (FCM) algorithm in pure NumPy/SciPy (soft membership matrix update, fuzziness parameter $m$, centroid convergence, hard-label assignment via argmax).
- Implement DBSCAN clustering leveraging `sklearn.cluster.DBSCAN` with k-distance (elbow) analysis for selecting optimal `eps` and `min_samples`.
- Map unsupervised cluster assignments to true ground-truth labels using optimal assignment (Hungarian algorithm) while handling DBSCAN noise points (label -1).
- Compute evaluation metrics: unsupervised metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index) and aligned error/agreement metrics (Adjusted Rand Index, Normalized Mutual Information, MAE/MSE/RMSE, Confusion Matrices).
- Generate visualizations:
  - Exploratory feature distributions and correlation heatmap.
  - FCM objective function / hyperparameter sweep and membership probability distributions.
  - DBSCAN k-distance elbow curve and core vs. border vs. noise sample scatter.
  - 2D feature-space and PCA cluster scatter plots with centroids/cluster designations.
  - Evaluation metric comparison bar charts and confusion matrix heatmaps.

## Capabilities

### New Capabilities
- `fcm-dbscan-clustering`: End-to-end clustering analysis implementing Fuzzy C-Means (FCM) and DBSCAN with parameter selection, label alignment, unsupervised and error evaluation metrics, and comprehensive visualizations without train/dev/test splits.

### Modified Capabilities
<!-- None: this is an independent new notebook workflow leaving existing notebooks and capabilities intact. -->

## Impact

- Adds `clustering_lab4_fcm_dbscan.ipynb` in the workspace root.
- Uses existing virtual environment dependencies (`numpy`, `scipy`, `sklearn`, `matplotlib`, `seaborn`) with zero external dependency risks (pure NumPy implementation of FCM).
- No changes to existing notebooks (`clustering_lab4.ipynb`, `clustering_lab4_train_dev_test.ipynb`) or LaTeX report (`main.tex`).
