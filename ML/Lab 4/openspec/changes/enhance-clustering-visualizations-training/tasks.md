## 1. Dataset Exploration Visualizations (EDA)

- [x] 1.1 Add feature distribution histograms and KDE grid (2x2) across all Iris attributes to `clustering_lab4.ipynb` and verify inline plot rendering
- [x] 1.2 Add feature correlation matrix heatmap and Petal Length vs. Petal Width scatter plot colored by class to `clustering_lab4.ipynb` and verify plot rendering

## 2. Model Training Optimization & Diagnostic Curves

- [x] 2.1 Implement K-Means hyperparameter sweep for $k \in [1, 10]$ and plot the Elbow method (Inertia) and Silhouette score curves side-by-side with optimal $k=3$ indicator, verifying training curve generation
- [x] 2.2 Implement Hierarchical clustering linkage analysis and plot annotated dendrogram with cutoff threshold line, verifying dendrogram generation

## 3. Enhanced Cluster Visualizations with Centroids

- [x] 3.1 Plot K-Means clusters in 2D feature space (Petal Length vs. Petal Width) with cluster centroids prominently marked, verifying centroid position accuracy
- [x] 3.2 Plot 2D PCA projected scatter plots comparing True labels, K-Means clusters (with projected centroids), and Hierarchical clusters, verifying plot rendering

## 4. Evaluation Metrics, Errors & Execution Validation

- [x] 4.1 Verify computation of Silhouette, Davies-Bouldin, Calinski-Harabasz, MAE, MSE, and RMSE scores alongside comparative bar charts
- [x] 4.2 Verify confusion matrix heatmaps for K-Means and Hierarchical clustering comparing aligned cluster predictions against ground truth labels
- [x] 4.3 Execute all cells of `clustering_lab4.ipynb` sequentially in the Python environment and verify clean execution with all outputs and figures generated
