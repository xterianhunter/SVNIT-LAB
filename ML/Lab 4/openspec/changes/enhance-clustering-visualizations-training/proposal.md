## Why

To enhance exploratory understanding and model diagnostic rigor in the clustering laboratory exercise, the notebook requires comprehensive dataset exploration, rigorous training optimization graphs (such as the Elbow Method and Silhouette analysis across candidate cluster counts), and rich visualizations showing cluster boundaries and centroids.

## What Changes

- Add Exploratory Data Analysis (EDA) visualizations:
  - Feature distributions and KDE plots for all Iris attributes.
  - Feature correlation matrix heatmap.
  - Feature-pair scatter plot comparing petal and sepal dimensions across classes.
- Add proper clustering model training diagnostics and training curves:
  - K-Means Elbow Method curve (Inertia vs. number of clusters $k \in [1, 10]$).
  - Silhouette Score vs. $k$ curve to demonstrate optimal cluster selection.
  - Hierarchical clustering dendrogram with annotated threshold cut-off line.
- Enhance cluster visualization:
  - Visualizing cluster centroids (`kmeans.cluster_centers_`) on both original feature space (Sepal vs Petal) and 2D PCA projection space.
  - Side-by-side comparisons of True labels, K-Means clusters, and Hierarchical clusters with centroid markers.
  - Cluster size distribution comparisons.
  - Retain all performance metrics, error metrics (MAE, MSE, RMSE), and confusion matrices.

## Capabilities

### New Capabilities
- `clustering-analysis`: Provides comprehensive dataset EDA, clustering training curves (Elbow method & Silhouette sweep), K-Means and Hierarchical clustering with centroid visualization, metrics/error evaluation, and confusion matrices in `clustering_lab4.ipynb`.

### Modified Capabilities
<!-- None -->

## Impact

- Enhances `clustering_lab4.ipynb` with richer visual diagnostics and training progression graphs.
- No new external dependencies required; continues using `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, and `scikit-learn`.
