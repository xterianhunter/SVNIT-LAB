## Context

See `proposal.md` for motivation. The notebook `clustering_lab4.ipynb` will be enhanced with dataset exploratory visualizations, clustering training optimization curves, and enhanced cluster scatter plots displaying centroids.

## Goals / Non-Goals

**Goals:**
- Provide clear Exploratory Data Analysis (EDA) visualizations:
  - Feature distributions / KDE histograms for all features.
  - Feature correlation heatmap.
  - 2D feature scatter plot (Petal Length vs. Petal Width) highlighting natural cluster separation.
- Implement training diagnostic plots:
  - Elbow Method plot (Inertia vs. $k$ for $k=1 \dots 10$).
  - Silhouette Score vs. $k$ plot ($k=2 \dots 10$) showing optimal peak at $k=3$.
  - Hierarchical clustering dendrogram with annotated cutoff distance line.
- Enhance cluster visualizations:
  - Plot clusters in feature space with K-Means cluster centers (`kmeans.cluster_centers_`) marked distinctly.
  - Plot 2D PCA projections comparing Ground Truth, K-Means (with transformed centroids `pca.transform(...)`), and Hierarchical clusters.
- Retain full evaluation metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz) and error metrics (MAE, MSE, RMSE) with comparison bar plots and confusion matrices.

**Non-Goals:**
- Unnecessary interactive dashboard libraries (e.g. Plotly/Dash) that complicate standard Jupyter rendering.
- Overcomplicated multi-model pipelines beyond K-Means and Hierarchical clustering.

## Decisions

- **EDA Layout**: Use a $2 \times 2$ grid for individual feature histograms/KDEs and a dedicated correlation heatmap.
  - *Rationale*: Compact, clear, and provides immediate insight into feature variances and separation.
- **Centroid Projection in PCA**: Project centroids into the PCA space using `pca.transform(kmeans.cluster_centers_)`.
  - *Rationale*: Allows plotting cluster centroids directly on the 2D PCA plot, making it easy to visually verify how well K-Means partitioned the data.
- **Training Optimization Diagnostics**: Plot Inertia and Silhouette scores side-by-side for $k \in [1, 10]$ and $k \in [2, 10]$.
  - *Rationale*: Demonstrates the theoretical process of selecting $k=3$ before training the final models.

## Risks / Trade-offs

- **[Risk]** Too many standalone figures making the notebook overly long.
  → *Mitigation*: Combine related plots into clean multi-panel subplots with unified styling.
