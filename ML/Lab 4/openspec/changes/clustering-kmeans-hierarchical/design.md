## Context

See `proposal.md` for motivation. The notebook will be created in the current workspace directory as a self-contained `.ipynb` file implementing both K-Means and Hierarchical Clustering with minimal preprocessing, evaluation metrics, error metrics, and visualizations.

## Goals / Non-Goals

**Goals:**
- Provide a clean, minimal, easily runnable Jupyter Notebook (`clustering_lab4.ipynb`).
- Utilize the standard Iris dataset (`sklearn.datasets.load_iris`) as a well-understood multi-class benchmark.
- Perform strictly necessary preprocessing: feature standardization via `StandardScaler`.
- Implement K-Means (`KMeans`) and Agglomerative Hierarchical Clustering (`AgglomerativeClustering`).
- Generate a dendrogram using `scipy.cluster.hierarchy`.
- Map cluster labels to ground truth classes using optimal linear sum assignment (`scipy.optimize.linear_sum_assignment`) for accurate error computation.
- Compute unsupervised clustering metrics: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index.
- Compute error metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE).
- Plot comprehensive charts: 2D PCA cluster visualizations, dendrogram, metric & error comparison bar charts, and confusion matrix heatmaps.

**Non-Goals:**
- Complex hyperparameter sweeps or automated grid searching.
- Heavy custom framework boilerplate or unnecessary utility abstractions.
- Modifying system libraries or external infrastructure.

## Decisions

- **Dataset Selection**: Use `sklearn.datasets.load_iris`.
  - *Rationale*: Pre-packaged, zero external download dependencies, exactly 3 classes and continuous features, ideal for comparing K-Means and Hierarchical clustering with ground truth.
  - *Alternative considered*: Custom CSV or Kaggle dataset. Rejected to keep the notebook completely standalone without external file dependencies.
- **Preprocessing Choice**: Minimal standardization with `StandardScaler`.
  - *Rationale*: Distance-based clustering (Euclidean) is sensitive to feature variance and scale; standardization is the only necessary transformation.
- **Cluster Label Alignment**: `scipy.optimize.linear_sum_assignment` on the negative confusion/contingency matrix.
  - *Rationale*: Unsupervised cluster indices (e.g. 0, 1, 2) do not inherently match arbitrary ground truth label IDs (0, 1, 2). Aligning them guarantees mathematically sound MAE, MSE, RMSE, and confusion matrix calculations without subjective renumbering.
- **Visualizations**: Use `matplotlib` and `seaborn` with concise subplots.
  - *Rationale*: Standard, visually appealing, reproducible inline in Jupyter notebooks.

## Risks / Trade-offs

- **[Risk]** Unsupervised cluster labels mismatch class identities leading to artificially high errors.
  → *Mitigation*: Automatically compute Hungarian assignment via `linear_sum_assignment` before calculating MAE, MSE, RMSE, and confusion matrix.
- **[Risk]** High-dimensional feature plotting ambiguity.
  → *Mitigation*: Use 2D PCA projection to clearly visualize cluster boundaries on a single scatter plot.
