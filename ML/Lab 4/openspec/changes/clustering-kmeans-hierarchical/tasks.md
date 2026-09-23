## 1. Notebook Environment & Dataset Setup

- [x] 1.1 Create `clustering_lab4.ipynb` notebook structure with required imports (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `sklearn`) and verify dependencies import without error
- [x] 1.2 Implement dataset loading (`load_iris`) and minimal feature standardization via `StandardScaler`, verifying scaled feature matrix shape and summary statistics

## 2. Clustering Models Implementation

- [x] 2.1 Implement K-Means clustering (`KMeans(n_clusters=3, random_state=42)`), fit the model, and verify cluster labels are assigned to each sample
- [x] 2.2 Implement Hierarchical Agglomerative clustering (`AgglomerativeClustering(n_clusters=3)`) and compute hierarchical linkage matrix via `scipy.cluster.hierarchy.linkage`, verifying cluster label array shape

## 3. Cluster Alignment & Metrics Evaluation

- [x] 3.1 Implement optimal cluster label alignment using Hungarian algorithm (`linear_sum_assignment`) to match cluster indices with ground truth classes, verifying mapped label accuracy
- [x] 3.2 Compute unsupervised clustering performance metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index) for both models and print results in a formatted table
- [x] 3.3 Compute error metrics (MAE, MSE, RMSE) between aligned cluster predictions and ground truth labels for both models and print the results

## 4. Visualizations & Execution Validation

- [x] 4.1 Plot 2D PCA cluster visualizations comparing K-Means, Hierarchical clustering, and True labels side-by-side
- [x] 4.2 Plot the Hierarchical clustering dendrogram with clear linkage threshold line
- [x] 4.3 Plot comparative bar charts for evaluation metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz) and error metrics (MAE, MSE, RMSE)
- [x] 4.4 Plot confusion matrix heatmaps comparing mapped cluster predictions to ground truth labels for both K-Means and Hierarchical clustering
- [x] 4.5 Execute all cells of `clustering_lab4.ipynb` sequentially and verify that all cells run without warnings or errors and produce expected plots
