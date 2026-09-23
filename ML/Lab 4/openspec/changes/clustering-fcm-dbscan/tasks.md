## 1. Environment and Notebook Scaffolding

- [x] 1.1 Create `clustering_lab4_fcm_dbscan.ipynb` with library imports (`numpy`, `pandas`, `matplotlib`, `seaborn`, `sklearn`, `scipy`) and verify clean kernel execution.
- [x] 1.2 Implement Iris dataset loading and standard scaling (`StandardScaler`) on the full 150-sample dataset without train/dev/test splits, verifying feature shape and zero mean/unit variance.

## 2. Exploratory Data Analysis (EDA)

- [x] 2.1 Add EDA cells plotting feature distributions (histograms with KDE) and a correlation heatmap to verify initial data characteristics and class separations.

## 3. Fuzzy C-Means (FCM) Implementation and Optimization

- [x] 3.1 Implement a vectorized pure-NumPy `FuzzyCMeans` class featuring soft membership calculation, fuzziness parameter $m$, centroid updating, and crisp assignment via argmax.
- [x] 3.2 Implement hyperparameter diagnostic curves plotting the objective function $J_m$ and Silhouette Score across candidate cluster numbers ($c \in [2, 10]$) and fuzziness values ($m$).
- [x] 3.3 Fit the optimal FCM model ($c=3, m=2.0$), extract soft membership probabilities and crisp labels, and verify that membership probabilities sum to 1.0 for all samples.

## 4. DBSCAN Implementation and Parameter Tuning

- [x] 4.1 Compute and plot the k-nearest-neighbors distance elbow graph using `NearestNeighbors` to determine the optimal neighborhood radius ($\epsilon$).
- [x] 4.2 Perform a parameter sweep over $\epsilon$ and `min_samples` combinations, tabulating resulting cluster counts, noise sample counts, and silhouette scores.
- [x] 4.3 Fit the calibrated DBSCAN model, categorize points into core samples, border samples, and noise points (label -1), and verify resulting cluster counts.

## 5. Label Alignment and Metric Evaluations

- [x] 5.1 Implement Hungarian matching (`linear_sum_assignment`) to map unsupervised cluster assignments to true ground-truth labels for both FCM and non-noise DBSCAN samples.
- [x] 5.2 Compute unsupervised quality metrics (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index) and classification error metrics (MAE, MSE, RMSE, ARI, NMI) in a comparative table.

## 6. Comprehensive Visualizations and Diagnostics

- [x] 6.1 Generate 2D feature-space scatter plots (Petal Length vs Petal Width) and 2D PCA projections highlighting FCM centroids and DBSCAN core vs border vs noise samples.
- [x] 6.2 Render FCM membership probability distribution plots and DBSCAN density comparison plots.
- [x] 6.3 Plot confusion matrices comparing aligned predictions against ground truth labels and summarize analytical comparisons between FCM and DBSCAN.

## 7. Verification and Execution

- [x] 7.1 Execute all cells of `clustering_lab4_fcm_dbscan.ipynb` end-to-end to verify that all figures, tables, and outputs render without errors.
